from fastapi import APIRouter , UploadFile, File, HTTPException

from core.loader import read_document

from core.retriever import retrieve

from core.generation import generate

from core.vectorstore import create_vectorstore , save_vectorstore , load_vectorstore

from backend.schemas import UserRequest , UserResponse

router = APIRouter()

@router.get("/")

async def health():

    return {
        "message" : "running"
    }

@router.post("/upload")

async def upload(file:UploadFile = File(...)):

    try:

        read_doc = await read_document(file)

        vectorstore = create_vectorstore(read_doc)

        save_vectorstore(vectorstore)

        return {
            "message" : "Document uploaded successfully"
        }

    except Exception as e:

        raise HTTPException(status_code=500,detail=str(e))

@router.post("/chat",response_model=UserResponse)

async def chat(request:UserRequest)->UserResponse:

    try:

        vectorstore = load_vectorstore()

        docs = retrieve(request.query,vectorstore)

        context = "\n\n".join(doc.page_content for doc in docs)

        answer = generate(request.query,context)

        return UserResponse(answer=answer)

    except Exception as e:

        raise HTTPException(status_code=500,detail=str(e))

