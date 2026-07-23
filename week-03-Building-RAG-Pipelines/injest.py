from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.config import vectorStore

def injest():
    print("Loading pdf...")

    loader = PyPDFDirectoryLoader("./data")
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print(chunks[0].page_content)

    vectorStore.add_documents(chunks)

    print("Successfully stored into Chroma DB")

if __name__ == "__main__":
    injest()