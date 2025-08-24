import subprocess
import json

def ask_ai(prompt: str) -> str:
    # Appelle le modèle LLaMA3 via Ollama (doit être installé : https://ollama.ai)
    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
