import queue
import sounddevice as sd
import json
import os

from vosk import Model, KaldiRecognizer
from config.config import ROOT


class STT:
    test_model_path = os.path.join(
        ROOT,
        "models/stt_models/vosk-model-small-fr-0.22/"
    )

    def __init__(self, model_path, samplerate=16000, device=None):
        self.model = Model(model_path)
        self.rec = KaldiRecognizer(self.model, samplerate)
        self.rec.SetWords(False)

        self.samplerate = samplerate
        self.device = device

        self.q = queue.Queue()
        self.stream = None

        # 🔥 micro toujours ouvert
        self.stream_started = False

    def _audio_callback(self, indata, frames, time_info, status):
        if status:
            return
        self.q.put(bytes(indata))

    def start_stream(self):
        """Ouvre le micro UNE seule fois"""
        if self.stream_started:
            return

        self.stream = sd.RawInputStream(
            samplerate=self.samplerate,
            blocksize=2000,  # 🔥 latence réduite
            dtype="int16",
            channels=1,
            callback=self._audio_callback,
            device=self.device
        )

        self.stream.start()
        self.stream_started = True
        print("🎙️ Micro prêt")

    def stop_stream(self):
        """Ferme le micro à la fermeture de l'app"""
        if self.stream:
            self.stream.stop()
            self.stream.close()
            self.stream_started = False

    def process_chunk(self):
        """
        Traite un seul chunk audio si disponible
        retourne texte final ou None
        """
        if self.q.empty():
            return None

        data = self.q.get()

        if self.rec.AcceptWaveform(data):
            result = json.loads(self.rec.Result())
            text = result.get("text", "").strip()

            if text:
                return text

        return None

    def get_final_text(self):
        """Récupère le texte restant au relâchement"""
        result = json.loads(self.rec.FinalResult())
        return result.get("text", "").strip()

    def reset(self):
        self.rec.Reset()
