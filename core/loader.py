import fitz

import re

from fastapi import UploadFile

def clean_text(text:str)->str:

    """Clean extracted text"""

    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(r"\n{2,}", "\n", text)

    return text.strip()

async def read_document(file:UploadFile)->str:

    """Extract text from the document"""

    pdf_bytes = await file.read()

    text = ""

    with fitz.open(stream=pdf_bytes,filetype="pdf") as pdf:
        for page in pdf:
            page_text = page.get_text("text")
            if page_text:
                text += clean_text(page_text) + "\n"

    return text



