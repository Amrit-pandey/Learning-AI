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

message = """
 You are an expert JavaScript teacher.

 Explain closures with one real-world example and one coding example.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=message
)

print(response.text)