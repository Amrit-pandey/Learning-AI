import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.count_tokens(
    model="gemini-2.5-flash",
    contents="Hi, my name is Amrit"
)

print(response.total_tokens)