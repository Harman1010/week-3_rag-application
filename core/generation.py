from config import PROMPT

from langchain_community.vectorstores import FAISS

from core.retriever import retrieve

from llm import llm

def generate(query:str,vector_store:FAISS) -> str:

    """Provides the answer based on the context"""

    context = retrieve(query,vector_store)

    prompt = f"""

    PROMPT:

    {PROMPT}

    Context:

    {context}

    Question:

    {query}

    Response:

"""

    response = llm.invoke(prompt)

    return response.content