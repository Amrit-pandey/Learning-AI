from google import genai
from utils.scraper import Fetch_website

def generate_brochure(client: genai.Client, website: Fetch_website):
    prompt = f"""
    You are an expert marketing assistant.

    Create a professional sales brochure.

    Use markdown.

    Keep the tone friendly.

    Mention products.

    Mention strengths.

    Finish with a call to action.

    Company: 
    {website.title}

    Website Content:
    {website.text}
    """
    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents= prompt
    )
    final_text = ""

    for chunk in response:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            final_text += chunk.text

    return final_text