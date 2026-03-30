import requests


def ask_llm(prompt, max_new_tokens=200, temperature=0.3):
    response = requests.post(
        "http://localhost:5001/api/v1/generate",
        json={
            "prompt": prompt,
            "max_new_tokens": max_new_tokens,
            "temperature": temperature,
        }
    )
    return response.json()["results"][0]["text"]
