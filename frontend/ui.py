import requests
import gradio as gr

BASE_URL = "http://127.0.0.1:8000"


def upload_document(file):
    if file is None:
        return "Please upload a document."

    try:
        with open(file.name, "rb") as f:
            response = requests.post(
                f"{BASE_URL}/upload",
                files={"file": (file.name, f)}
            )

        if response.status_code == 200:
            return "Document uploaded and processed successfully."

        return f"{response.json()['detail']}"

    except Exception as e:
        return f"{str(e)}"


def chat(message, history):
    try:
        response = requests.post(
            f"{BASE_URL}/chat",
            json={"query": message}
        )

        if response.status_code == 200:
            return response.json()["response"]

        return f"{response.json()['detail']}"

    except Exception as e:
        return f"{str(e)}"


with gr.Blocks(title="RAG Document Chatbot") as demo:

    gr.Markdown(
        """
        #vRAG Document Chatbot

        Upload a document once, then ask questions about it.
        """
    )

    with gr.Row():
        file = gr.File(
            label="Upload Document",
            file_types=[".pdf", ".docx", ".txt"]
        )

    upload_btn = gr.Button("📤 Process Document", variant="primary")

    upload_status = gr.Textbox(
        label="Status",
        interactive=False
    )

    upload_btn.click(
        upload_document,
        inputs=file,
        outputs=upload_status
    )

    gr.Markdown("---")

    gr.ChatInterface(
        fn=chat,
        title="Ask Questions",
        description="Ask anything related to the uploaded document."
    )

demo.launch()