import os
from google import genai
from dotenv import load_dotenv
from utils.gemini import generate_brochure
from utils.scraper import Fetch_website

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)

if not api_key:
    print("It seems like you haven't provide a valid api key yet. please provide!")
elif not api_key.startswith("AQ."):
    print("Invalid api key")
else:
    print("Api key found, Great!")

website = Fetch_website("https://www.apple.com/")
brochure =  generate_brochure(client, website)
print(brochure)