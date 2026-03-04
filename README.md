# Cyber Intelligence System

## Agentic Backend for Dynamic Knowledge Extraction from the Cyber Ireland 2022 Report

---

# 1. Project Overview

This project implements an **agentic AI backend** capable of transforming a static industry report into a **dynamic, queryable intelligence system**.

The system processes the **Cyber Ireland 2022 Report**, extracts structured and unstructured information, and enables users to query the data through a unified API endpoint.

Unlike traditional Retrieval Augmented Generation (RAG) systems, this architecture supports:

- Evidence-backed document retrieval
- Structured analytics over tabular data
- Mathematical reasoning
- Tool‑based agent orchestration

The goal is to build a **reliable intelligence system** capable of answering complex queries with **verifiable citations and accurate calculations**.

---

# 2. Assignment Objectives

The assignment required building a system capable of:

1. **Ingesting a complex PDF report** containing text and tables.
2. **Transforming the document into structured and searchable data.**
3. **Designing an agentic backend capable of tool usage.**
4. **Answering three categories of questions:**

### Verification Queries
Retrieve exact facts with page citations.

Example:

> "What is the total number of jobs reported, and where exactly is this stated?"

---

### Data Synthesis Queries
Extract structured data and compute comparisons.

Example:

> "Compare the concentration of Pure‑Play cybersecurity firms in the South‑West against the National Average."

---

### Forecasting Queries
Combine retrieved values with mathematical calculations.

Example:

> "What CAGR is required to reach 17000 cybersecurity jobs by 2030?"

---

# 3. High Level System Architecture

```
Cyber Ireland Report (PDF)
            │
            ▼
        ETL Pipeline
            │
   ┌────────┴─────────┐
   ▼                  ▼
Structured Tables   Text Content
(SQL Database)      (Vector Store)
   │                  │
   ▼                  ▼
Analytics Tool     Retrieval Tool
        │
        ▼
      Agent Router
(Intent Classification + Tool Selection)
        │
        ▼
      FastAPI API
        │
        ▼
      /query endpoint
```

---

# 4. Architecture Rationale

Traditional RAG pipelines only retrieve text.

However the assignment requires:

- Structured table analysis
- Mathematical calculations
- Multi‑step reasoning

Therefore the system separates tasks into **specialized tools**.

| Tool | Responsibility |
|-----|-----|
| Retrieval Tool | Extract factual evidence from document |
| Analytics Tool | Query structured metrics from SQL |
| Math Tool | Perform reliable calculations |

An **agent router** decides which tool should handle the query.

This approach increases reliability and prevents hallucinated results.

---

# 5. Technology Stack

## Backend Framework

**FastAPI**

Why used:

- High performance
- Automatic API documentation
- Ideal for microservice architectures

Alternatives considered:

| Alternative | Reason Rejected |
|----|----|
Flask | Lacks built‑in API documentation |
Django | Overly heavy for this project |

---

## Vector Database

**ChromaDB**

Why used:

- Lightweight
- Local storage
- Fast semantic search

Alternatives considered:

| Alternative | Reason Not Used |
|----|----|
Pinecone | Requires external service |
Weaviate | Overkill for assignment |
FAISS | No native metadata persistence |

---

## Embedding Model

**sentence-transformers/all-MiniLM-L6-v2**

Why used:

- Fast inference
- High semantic similarity performance
- Lightweight model

Alternatives considered:

| Alternative | Reason Not Used |
|----|----|
OpenAI embeddings | Requires API key |
BERT large models | Too computationally heavy |

---

## Database

**SQLite**

Why used:

- Simple local database
- Zero configuration
- Ideal for structured metrics

Alternatives considered:

| Alternative | Reason Not Used |
|----|----|
PostgreSQL | Unnecessary complexity |
MongoDB | Less suitable for relational metrics |

---

## NLP Intent Classification

**Sentence Transformers + Cosine Similarity**

Used to classify queries into:

- retrieval
- analytics
- math

Alternatives considered:

| Alternative | Reason Not Used |
|----|----|
Rule based routing | Too brittle |
LLM based routing | Requires external APIs |

---

# 6. ETL Pipeline

The ETL pipeline converts the report into two usable knowledge layers.

---

## Step 1 — Text Extraction

Script:

```
etl/extract_text.py
```

Responsibilities:

- Extract text from PDF
- Preserve page numbers
- Store data in JSON format

Output:

```
storage/text_data.json
```

---

## Step 2 — Table Extraction

Script:

```
etl/extract_tables.py
```

Responsibilities:

- Identify tabular content
- Extract firm counts by region
- Convert tables into structured data

---

## Step 3 — Metrics Database

Script:

```
etl/build_metrics_layer.py
```

Responsibilities:

- Load extracted tables
- Create SQLite schema
- Store structured metrics

Database:

```
database/cyber_sector.db
```

Example metrics stored:

| Metric | Value |
|------|------|
Total firms | 489 |
Cork firms | 129 |
Kerry firms | 5 |
South West firms | 134 |
Employment | 7351 |

---

## Step 4 — Vector Embeddings

Script:

```
etl/build_vector_store.py
```

Responsibilities:

- Chunk document text
- Generate embeddings
- Store vectors in ChromaDB

Output directory:

```
vectorstore/
```

---

# 7. Agent System

The agent acts as the **decision layer** of the system.

Responsibilities:

1. Understand query intent
2. Select appropriate tool
3. Execute tool
4. Return structured response

---

## Intent Classification

Script:

```
agent/intent_classifier.py
```

Uses sentence embeddings to compare queries against predefined intent examples.

This provides semantic routing instead of brittle keyword matching.

---

## Agent Router

Script:

```
agent/agent_router.py
```

Responsibilities:

- Receive query
- Identify intent
- Call correct tool
- Return response

---

## Execution Logger

Script:

```
agent/execution_logger.py
```

Logs tool usage and reasoning traces.

This provides visibility into how the agent reached the answer.

---

# 8. Tools

## Retrieval Tool

Script:

```
rag/retriever.py
```

Responsibilities:

- Perform semantic search
- Retrieve most relevant document chunk
- Extract numerical values
- Return page citation

Used for **verification queries**.

---

## Structured Query Tool

Script:

```
rag/structured_query.py
```

Responsibilities:

- Query SQLite database
- Compute regional comparisons
- Calculate firm distribution

Used for **data synthesis queries**.

---

## Math Tool

Script:

```
rag/math_tools.py
```

Responsibilities:

- Perform numerical calculations
- Compute CAGR

Formula used:

```
CAGR = (End / Start)^(1 / Years) - 1
```

Used for **forecasting queries**.

---

# 9. API Layer

Script:

```
api/main.py
```

Responsibilities:

- Start FastAPI server
- Provide `/query` endpoint
- Forward queries to agent router

Example request:

```
POST /query
{
  "query": "How many cybersecurity professionals work in Ireland?"
}
```

Example response:

```
{
  "query": "...",
  "tool_used": "retrieval",
  "result": {
    "jobs_reported": 7351,
    "page": 17,
    "citation": "..."
  }
}
```

---

# 10. Repository Structure

```
cyber-intelligence-system

agent/
 ├ intent_classifier.py
 ├ agent_router.py
 ├ execution_logger.py

api/
 └ main.py

etl/
 ├ extract_text.py
 ├ extract_tables.py
 ├ build_metrics_layer.py
 └ build_vector_store.py

rag/
 ├ retriever.py
 ├ structured_query.py
 └ math_tools.py

storage/
 └ text_data.json

database/
 └ cyber_sector.db

vectorstore/

requirements.txt
README.md
```

---

# 11. Setup Instructions

## Install dependencies

```
pip install -r requirements.txt
```

---

## Run ETL Pipeline

```
python etl/extract_text.py
python etl/extract_tables.py
python etl/build_metrics_layer.py
python etl/build_vector_store.py
```

---

## Start Backend

```
uvicorn api.main:app --reload
```

---

## Open API

```
http://127.0.0.1:8000/docs
```

---

# 12. Evaluation Results

## Verification Query

"What is the total number of jobs reported?"

Result:

7351 cybersecurity professionals with page citation.

---

## Data Synthesis Query

"What proportion of cybersecurity firms are located in Cork?"

Result:

129 / 489 = 26.38%

---

## Forecasting Query

"What CAGR is required to reach 17000 jobs by 2030?"

Result:

9.76%

---

# 13. Limitations

1. Intent classifier is lightweight.
2. Some queries may retrieve approximate context.
3. Table extraction required manual validation.

---

# 14. Future Improvements

For production deployment the system could be improved with:

- LLM based tool planning
- automatic SQL generation
- streaming document ingestion
- distributed vector databases
- observability tools like LangSmith

---

# 15. Conclusion

This project demonstrates how an **agentic architecture can transform static documents into dynamic knowledge systems**.

By combining retrieval, structured analytics, and mathematical reasoning, the system provides reliable and explainable intelligence extraction from complex reports.

