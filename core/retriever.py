from langchain_community.vectorstores import FAISS

from langchain_core.documents import Document


def retrieve(query: str,vector_store: FAISS,k: int = 3) -> list[Document]:
    
    """Retrieve relevant context"""

    print("\n=== retrieve ===")
    print("Query:", query)
    print("Vector Store Type:", type(vector_store))
    print("=================\n")

    return vector_store.similarity_search(query, k=k)

    #return "\n\n".join(doc.page_content for doc in docs)