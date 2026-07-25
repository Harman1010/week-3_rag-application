from config import PROMPT

from langchain_community.vectorstores import FAISS

from core.retriever import retrieve

from core.llm import llm

def generate(query: str,context: str) -> str:

    """Provides the answer based on the context"""

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