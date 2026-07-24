from langchain_community.vectorstores import FAISS

from core.chunker import chunking

from core.embeddings import embeddings

def storage(text:str)->FAISS:

    chunks = chunking(text)

    vector_store = FAISS.from_texts(
        texts = chunks,
        embedding = embeddings
    )

    return vector_store

