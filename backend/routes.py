from fastapi import APIRouter,FileUpload

from core.loader import read_document

from core.vectorstore import storage

from backend.schemas import UserRequest , UserResponse

router = APIRouter()

@router.get("/")

def health():

    return {
        "message" : "running"
    }

@router.post("/upload")

def upload(file:FileUpload(...))->BinaryIO:

    read_doc = read_document(file)

    if not read_doc:
        return "Document could not be uploaded. Please Try Again"

    return read_doc

@router.post("/chat")

def chat(query:UserRequest)->str:

    vectorstore = storage()



    response = UserResponse(query)

    return response

