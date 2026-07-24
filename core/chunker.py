#RecursiveTextSplitter

from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunking(text:str,chunk_size:int=1000,chunk_overlap:int=200)->list[str]:

    """Splits text into overlapping chunks"""

    splitter = RecursiveCharacterTextSplitter(text,chunk_size=chunk_size,chunk_overlap=chunk_overlap)

    return splitter.split_text(text)