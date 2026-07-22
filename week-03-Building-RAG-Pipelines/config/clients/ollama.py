from openai import OpenAI

ollama_client = OpenAI(
    api_key="ollama",
    base_url="http://127.0.0.1:11434/v1"
)