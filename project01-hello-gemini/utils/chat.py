from google import genai

conversations = []

def chat(client: genai.Client, user_msg: str, system_prompt: str):
    conversations.append(
        {
            "role": "user",
            "parts": [{"text": user_msg}]
        }
    )
    # call Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversations,
        config={
            "system_instruction": system_prompt,
        }
    )

    # Save AI response
    conversations.append(
        {
            "role": "model",
            "parts": [{"text": response.text}]
        }
    )

    return response.text