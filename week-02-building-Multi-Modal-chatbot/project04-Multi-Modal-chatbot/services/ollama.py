from config.clients import ollama_client, system_prompt

def stream_ollama(prompt):
    response = ollama_client.chat.completions.create(
        model="llama3.2:1b",
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}], stream=True
    )
    response_text = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            response_text += token
        yield response_text