import os
from dotenv import load_dotenv
from google import genai
from utils.chat import chat

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if not api_key:
    print("Please provide a valid api key")
elif not api_key.startswith("AQ."):
    print("It seems like it's not a valid api key")
else:
    print("Api key found!")

SYSTEM_PROMPT = "You are a helfull assistant, "

print(chat(client, "Hi, i'm amrit", SYSTEM_PROMPT)) 
print()
print(chat(client, "what's my name?", SYSTEM_PROMPT))
print()