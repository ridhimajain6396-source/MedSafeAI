# import ollama

# def ask_llm(prompt):
#     response = ollama.chat(
#         model="llama3",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response["message"]["content"]

import os
import requests

SARVAM_URL = "https://api.sarvam.ai/v1/chat/completions"

def ask_llm(prompt: str) -> str:
    try:
        api_key = os.getenv("SARVAM_API_KEY")

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "sarvam-m",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a medical safety assistant. Give educational guidance only. Never diagnose."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3,
            "max_tokens": 400
        }

        response = requests.post(SARVAM_URL, json=payload, headers=headers, timeout=60)

        if response.status_code != 200:
            return f"AI Error: {response.text}"

        data = response.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"AI Error: {str(e)}"
