import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

system_prompt = """
You are a helpful assistant.

Whenever the user asks about weather,
ALWAYS call the get_current_weather tool.

Whenever the user asks about GitHub repositories,
ALWAYS call the get_latest_repo tool.

Never guess weather information yourself.
"""

gemini_client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

ollama_client = OpenAI(
    api_key="ollama",
    base_url="http://127.0.0.1:11434/v1"
)