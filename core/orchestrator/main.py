import json

from ..stt.vosk_stt import STT
from ..llm.kobold_client import ask_llm
from ..llm.prompts import PROMPTS
from tools.create_task import create_task


stt = STT("models/stt_models/vosk-model-small-fr-0.22")


def main():
    while True:
        text = stt.listen()
        print("Compris:", text)

        prompt = PROMPTS.get("planner", "Quelque chose ne va pas.")

        response = ask_llm(prompt)

        try:
            data = json.loads(response)
        except:
            print("Erreur parsing LLM: ", response)
            continue

        for action in data["actions"]:
            if action["tool"] == "create_task":
                path = create_task(
                    action["title"],
                    action["description"]
                )
                print(f"Tâche créée: {path}")

        print("En attente...\n")


if __name__ == "__name__":
    main()
