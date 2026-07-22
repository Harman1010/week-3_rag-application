from config import GEMINI_MODEL

from langchain_google_genai import ChatGoogleGenerativeAI

def load_llm():

    return ChatGoogleGenerativeAI(
        model = GEMINI_MODEL,
        temperature=0.2
    )

llm = load_llm()
