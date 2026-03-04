import json
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


TEXT_DATA_PATH = "storage/text_data.json"
VECTOR_STORE_DIR = "storage/vector_store"


def load_text_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_vector_store():
    print("Loading extracted text...")
    data = load_text_data(TEXT_DATA_PATH)

    documents = []
    metadatas = []

    print("Splitting into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    for page in data:
        splits = text_splitter.split_text(page["content"])

        for chunk in splits:
            documents.append(chunk)
            metadatas.append({
                "page": page["page"],
                "source": page["source"]
            })

    print("Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Building Chroma vector store...")

    # Ensure directory exists
    os.makedirs(VECTOR_STORE_DIR, exist_ok=True)

    vectorstore = Chroma.from_texts(
        texts=documents,
        embedding=embeddings,
        metadatas=metadatas,
        persist_directory=VECTOR_STORE_DIR
    )

    vectorstore.persist()

    print("Vector store built successfully.")


if __name__ == "__main__":
    build_vector_store()