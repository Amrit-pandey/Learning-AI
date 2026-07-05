import gradio as gr
from app.chatbot import chat

def create_ui():
    return gr.ChatInterface(
        fn=chat,
    )