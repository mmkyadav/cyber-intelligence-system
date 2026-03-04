import re
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTORSTORE_DIR = "vectorstore"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="vectorstore",
    embedding_function=embeddings,
    collection_name="cyber_docs"
)

retriever = vectorstore.as_retriever(search_kwargs={"k":3})


def extract_employment_number(text):

    # prioritize workforce number
    patterns = [
        r"(\d{1,3},\d{3})",     # 7,351
        r"\b(\d{4})\b"          # fallback for 7351
    ]

    for pattern in patterns:

        matches = re.findall(pattern, text)

        if matches:
            for m in matches:

                num = int(m.replace(",", ""))

                # ignore numbers that are clearly not workforce values
                if num < 1000:
                    continue

                if num > 50000:
                    continue

                return num

    return None


def retrieve_answer(query: str):

    docs = retriever.invoke(query)

    if not docs:
        return {"error": "No relevant document found"}

    text = docs[0].page_content
    metadata = docs[0].metadata

    jobs = extract_employment_number(text)

    return {
        "jobs_reported": jobs,
        "page": metadata.get("page"),
        "citation": text
    }