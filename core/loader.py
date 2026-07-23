import fitz

import re

from typing import BinaryIO

def clean_text(text:str)->str:

    """Clean extracted text"""

    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(r"\n{2,}", "\n", text)

    return text.strip()

def read_document(file:BinaryIO)->str:

    """Extract text from the document"""

    text = ""

    with fitz.open(stream=file.read(),filetype="pdf") as pdf:
        for page in pdf:
            page_text = page.get_text("text")
            if page_text:
                text += clean_text(page_text) + "\n"

    return text



