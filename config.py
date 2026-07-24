import os

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = "llama-3.3-70b-versatile"

PROMPT = """

You are a helpful assistant.

Provide a concise explanation of the user queries from the external document and the context provided.

Instructions:

- Do not hallucinate
- Do not fabricate information
- Do not invent new information
- If the answer is not present, simple inform the user that the answer is not present in the document

"""