import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import gradio as gr

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
today = datetime.now().strftime("%A, %d %B %Y")

gemini_client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

ollama_client = OpenAI(
    api_key="ollama",
    base_url="http://127.0.0.1:11434/"
)

system_prompt = "You are a helpful assistant"

def chat_message(prompt):
    response = gemini_client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}], stream=True
    )
    response_text = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            print(token, end="")
            response_text += token

    yield response_text

prompt = f"""
today date is {today}

user: 
what's today date.
"""
chat_message(prompt)

gr.Interface(fn=chat_message, inputs="textbox", outputs="textbox", flagging_mode="never").launch(share=True)