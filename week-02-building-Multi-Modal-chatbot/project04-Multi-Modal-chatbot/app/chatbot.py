from pprint import pprint
from config.clients import system_prompt, gemini_client

def chat(message, history):
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    for h in history:
        messages.append(
            {
                "role": h["role"],
                "content": h["content"][0]["text"]
            }
        )

    messages.append(
        {
            "role": "user",
            "content": message
        }
    )
    pprint(messages)
    stream = gemini_client.chat.completions.create(model="gemini-2.5-flash", messages=messages, stream=True)
    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            response +=chunk.choices[0].delta.content
        yield response