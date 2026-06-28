import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(
    api_key = api_key
)

if not api_key:
    print("Please provide a valid api key")
elif not api_key.startswith("AQ."):
    print("It seems like it's not a valid api key")
else:
    print("Api key found!")

system_prompt = "You are an expert ReactJS teacher"
user_prompt = "explain useState in react"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_prompt,
    config={
        "system_instruction": system_prompt
    }
)

print(response.text)