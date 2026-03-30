import keyboard
from core.stt import vosk_stt


class PushToTalk:
    def __init__(self, stt, key="space", on_text=None):
        self.stt = stt
        self.key = key
        self.on_text = on_text

        self.recording = False
        self.texts = []
        self.cur_text = ""

    def run(self):
        print(f"Maintiens '{self.key}' pour parler")

        # 🔥 micro prêt une seule fois
        self.stt.start_stream()

        while True:
            # 🎤 START logique
            if keyboard.is_pressed(self.key) and not self.recording:
                print("🎤 Parle...")
                self.recording = True
                self.texts = []
                self.cur_text = ""

            # 🧠 traitement continu
            if self.recording:
                text = self.stt.process_chunk()

                if text:
                    text = text.capitalize() + "."
                    print("📝", text)
                    self.texts.append(text)

            # ⏹️ STOP logique
            if not keyboard.is_pressed(self.key) and self.recording:
                print("⏹️ Fin")
                self.recording = False

                final_text = self.stt.get_final_text()

                if final_text:
                    final_text = final_text.capitalize() + "."
                    self.texts.append(final_text)

                full_text = " ".join(self.texts).strip()

                if full_text:
                    self.cur_text = full_text
                    print("🧠 Texte final:", full_text)

                    # 🔥 envoi à l’orchestrateur
                    if self.on_text:
                        self.on_text(full_text)

                self.stt.reset()

    def get_cur_text(self):
        return self.cur_text

    def stop(self):
        self.stt.stop_stream()


if __name__ == "__main__":
    stt = vosk_stt.STT(vosk_stt.STT.test_model_path)
    ptt = PushToTalk(stt, key="space")
    ptt.run()
