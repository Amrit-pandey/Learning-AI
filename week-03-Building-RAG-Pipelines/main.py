from config.clients.ollama import ollama_client

system_prompt = """
You are the helpfull assistant.
"""

response = ollama_client.chat.completions.create(
    model="qwen2.5:7b",
    messages=[{"role": "system", "content": system_prompt}]
)
print(response,"response")

result = response.choices[0].message.content
print(result)