from langchain_community.vectorstores import FAISS


def retrieve(query: str,vector_store: FAISS,k: int = 3) -> str:
    
    """Retrieve relevant context"""

    docs = vector_store.similarity_search(query, k=k)

    return "\n\n".join(doc.page_content for doc in docs)