import sqlite3
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTOR_DB_PATH = "storage/vector_store"
DB_PATH = "database/cyber_sector.db"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory=VECTOR_DB_PATH,
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 5})


def get_total_jobs():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT value FROM metrics
        WHERE metric_name='employment'
        AND region='Ireland'
        LIMIT 1
    """)

    result = cursor.fetchone()
    conn.close()

    if result:
        return int(result[0])

    return None


def retrieve_answer(query):

    jobs = get_total_jobs()

    docs = retriever.invoke(query)

    best_doc = docs[0]

    return {
        "jobs_reported": jobs,
        "page": best_doc.metadata.get("page"),
        "citation": best_doc.page_content
    }