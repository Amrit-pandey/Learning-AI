from config.config import retriever, llm
from prompt import SYSTEM_PROMPT_TEMPLATE
from langchain_core.messages import SystemMessage, HumanMessage

def answer_question(question: str, history):
    docs = retriever.invoke(question)
    print("=" * 60)
    print("Retrieved Chunks")
    print("=" * 60)
    for i, doc in enumerate(docs, start=1):
        print(f"\nChunk {i}")
        print("-" * 50)
        print(doc.page_content[:300])
    context = "\n\n".join(doc.page_content for doc in docs)
    print(context, "CONTEXT")
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(context=context)
    response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=question)])
    print(response, "RESPONSE")