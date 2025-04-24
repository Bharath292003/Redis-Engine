import requests


def generate_summary(user_prompt, llm_response):
    prompt = f"Summarize the following user-AI interaction in one sentence:\n\nUser: {user_prompt}\nAI: {llm_response}\n\nSummary:"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    try:
        return response.json()["response"].strip()
    except KeyError:
        print("[ERROR] Unexpected Ollama response format:")
        print(response.json())
        return "(summary unavailable)"


def generate_response(prompt):
    """
    Sends the full prompt to LLaMA (via Ollama) and returns its replysssss.
    """
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()
