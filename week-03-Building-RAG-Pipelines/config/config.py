import os
from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv(override=True)

token = os.getenv("HF_TOKEN")

DB_NAME = "./vector_db"

# connect to chroma db with huggingface model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorStore = Chroma(persist_directory=DB_NAME, embedding_function=embeddings)