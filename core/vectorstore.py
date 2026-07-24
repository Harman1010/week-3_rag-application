from langchain_community.vectorstores import FAISS

from core.chunker import chunking
from core.embeddings import embeddings

from config import VECTOR_DB_PATH

DB_PATH = VECTOR_DB_PATH


def create_vectorstore(text: str) -> FAISS:
    
    chunks = chunking(text)

    return FAISS.from_texts(
        texts=chunks,
        embedding=embeddings,
    )


def save_vectorstore(vector_store: FAISS):

    vector_store.save_local(DB_PATH)


def load_vectorstore() -> FAISS:
    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True,
    )