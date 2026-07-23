from config import GROQ_MODEL

from langchain_groq import ChatGroq

def load_llm():

    return ChatGroq(
        model=GROQ_MODEL,
        temperature=0.2
    )

llm = load_llm()
