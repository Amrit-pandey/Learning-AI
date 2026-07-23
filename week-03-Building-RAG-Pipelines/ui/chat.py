import gradio as gr
from services.rag import answer_question

def create_ui():
    return gr.ChatInterface(
        fn=answer_question
    )