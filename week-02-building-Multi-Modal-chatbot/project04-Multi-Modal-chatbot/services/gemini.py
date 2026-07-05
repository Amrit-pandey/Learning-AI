from config.clients import gemini_client, system_prompt

def stream_gemini(prompt):
    response = gemini_client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}], stream=True
    )
    response_text = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            response_text += token
        yield response_text