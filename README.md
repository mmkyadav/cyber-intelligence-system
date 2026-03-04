\# Cyber Intelligence Agentic System



\*\*Technical Assessment Implementation\*\*



An \*\*agentic data intelligence backend\*\* built to analyze the \*\*Cyber Ireland 2022 report\*\* using a hybrid architecture that combines:



\* Document retrieval (RAG)

\* Structured data analytics

\* Deterministic mathematical tools

\* Autonomous tool routing

\* REST API access



The system extracts insights from a complex report by orchestrating multiple specialized tools instead of relying on a single model.



---



\# Table of Contents



1\. Project Overview

2\. Problem Statement

3\. System Architecture

4\. Approach and Design Decisions

5\. Technologies Used

6\. Alternatives Considered

7\. ETL Pipeline

8\. Retrieval System (RAG)

9\. Structured Analytics Layer

10\. Mathematical Reasoning Tool

11\. Agent Routing Logic

12\. API Interface

13\. Installation

14\. Running the Pipeline

15\. Usage Examples

16\. Project Structure

17\. Limitations

18\. Future Improvements

19\. License



---



\# Project Overview



This project implements an \*\*agentic intelligence system\*\* capable of answering analytical questions from the \*Cyber Ireland Cybersecurity Sector Report 2022\*.



The system processes the report through an ETL pipeline and exposes a \*\*query interface capable of handling different types of analytical questions\*\*, including:



\* factual document questions

\* regional comparisons

\* forecasting calculations



Instead of relying solely on a language model, the system integrates:



\* semantic document retrieval

\* structured SQL queries

\* deterministic mathematical tools



This hybrid approach improves \*\*accuracy, transparency, and reliability\*\*.



---



\# Problem Statement



The Cyber Ireland report contains:



\* unstructured narrative text

\* structured tables

\* numerical projections

\* regional comparisons



Traditional document QA systems struggle with this because they require:



1\. document search

2\. structured analytics

3\. numerical reasoning



The goal of this assignment was to design a system that can:



\* extract knowledge from the report

\* answer analytical queries

\* reference supporting evidence

\* compute derived metrics



---



\# System Architecture



```

Cyber Ireland Report (PDF)

&nbsp;           │

&nbsp;           ▼

&nbsp;       ETL Pipeline

&nbsp;┌────────────────────────────┐

&nbsp;│ Text Extraction             │

&nbsp;│ Table Extraction            │

&nbsp;│ Metrics Warehouse Creation  │

&nbsp;└────────────────────────────┘

&nbsp;           │

&nbsp;           ▼

&nbsp;    Vector Embedding Layer

&nbsp;    (Sentence Transformers)

&nbsp;           │

&nbsp;           ▼

&nbsp;       Vector Database

&nbsp;          Chroma

&nbsp;           │

&nbsp;           ▼

&nbsp;       Agent Router

&nbsp;┌────────────┼────────────┐

&nbsp;│            │            │

&nbsp;▼            ▼            ▼

Retriever   SQL Tool    Math Tool

(RAG)      (Analytics)  (CAGR)

&nbsp;           │

&nbsp;           ▼

&nbsp;        FastAPI

&nbsp;           │

&nbsp;           ▼

&nbsp;       Client Queries

```



---



\# Approach and Design Decisions



A \*\*hybrid intelligence architecture\*\* was implemented.



Instead of relying exclusively on LLM reasoning, the system separates responsibilities:



| Capability            | Implementation   |

| --------------------- | ---------------- |

| Document search       | Vector retrieval |

| Regional analytics    | SQL warehouse    |

| Forecast calculations | Math tool        |



This design improves:



\* correctness

\* reproducibility

\* explainability



Each tool is deterministic and transparent.



---



\# Technologies Used



| Technology            | Purpose                   |

| --------------------- | ------------------------- |

| Python                | Core programming language |

| FastAPI               | REST API framework        |

| LangChain             | Retrieval abstraction     |

| Sentence Transformers | Embedding generation      |

| Chroma                | Vector database           |

| SQLite                | Metrics warehouse         |

| Camelot               | PDF table extraction      |

| pdfminer / pypdf      | PDF text extraction       |

| Pandas                | Data processing           |

| Uvicorn               | ASGI server               |



---



\# Why These Technologies Were Chosen



\## Python



Python was chosen due to its strong ecosystem for:



\* machine learning

\* document processing

\* data engineering

\* AI frameworks



---



\## FastAPI



FastAPI provides:



\* high performance

\* automatic OpenAPI documentation

\* simple async API development



Alternative considered:



\*\*Flask\*\*



Why not Flask:



\* slower

\* lacks automatic schema documentation

\* less suited for production APIs



---



\## Sentence Transformers



Embedding model used:



```

sentence-transformers/all-MiniLM-L6-v2

```



Reasons:



\* lightweight

\* fast inference

\* strong semantic performance

\* works well on CPU



Alternative considered:



OpenAI embeddings



Rejected because:



\* paid API dependency

\* network latency

\* quota limitations



Local embeddings provide better \*\*reproducibility and cost control\*\*.



---



\## Chroma Vector Database



Chroma was selected because:



\* easy local setup

\* tight LangChain integration

\* persistent storage

\* lightweight



Alternative considered:



FAISS



Reasons FAISS was not used:



\* FAISS does not natively provide persistence

\* requires additional management

\* more suited for large-scale production systems



For this assignment, Chroma provides \*\*simpler persistence and usability\*\*.



---



\## SQLite



SQLite was used for the analytics warehouse because:



\* lightweight

\* serverless

\* zero configuration

\* ideal for analytical prototypes



Alternative considered:



PostgreSQL



PostgreSQL would be preferred in production but adds operational complexity for a local assignment.



---



\## Camelot



Camelot provides reliable table extraction from PDFs.



Alternative considered:



Tabula



Camelot was chosen because:



\* better Python integration

\* more control over extraction

\* better table detection



---



\# ETL Pipeline



The ETL pipeline prepares the report for analysis.



Steps:



1\. Extract document text

2\. Extract tabular data

3\. Store metrics in database

4\. Create vector embeddings



---



\## Text Extraction



Extracts narrative sections from the report for semantic retrieval.



Tools used:



```

pypdf

pdfminer

```



Output:



\* cleaned text corpus

\* page metadata



---



\## Table Extraction



Tables are extracted using Camelot and stored with metadata:



| Field        | Description       |

| ------------ | ----------------- |

| table\_name   | identifier        |

| page\_number  | source page       |

| row\_count    | rows extracted    |

| column\_count | columns extracted |



---



\## Metrics Warehouse



Important metrics were normalized and stored in SQLite.



Example metrics:



| Metric                   | Value |

| ------------------------ | ----- |

| Total firms              | 489   |

| Dedicated firms          | 160   |

| Diversified firms        | 329   |

| Cybersecurity employment | 7351  |



---



\# Retrieval Augmented Generation (RAG)



Document text is split into chunks and embedded using Sentence Transformers.



These embeddings are stored in a \*\*Chroma vector store\*\*.



When a query arrives:



1\. embeddings are computed

2\. nearest document chunks are retrieved

3\. relevant citation and page are returned



Example output:



```

jobs\_reported: 7351

page: 23

citation: workforce section of the report

```



---



\# Structured Analytics Layer



Certain queries require structured calculations rather than document retrieval.



Example:



```

Compare the concentration of Pure-Play cybersecurity firms in the South-West against the National Average

```



These are answered through SQL queries against the metrics warehouse.



Benefits:



\* deterministic

\* explainable

\* auditable



---



\# Mathematical Tool



Growth projections require mathematical reasoning.



Example query:



```

What CAGR is needed to reach 17000 jobs by 2030?

```



Formula used:



```

CAGR = (Final / Initial)^(1 / Years) - 1

```



Output:



```

9.76% CAGR required

```



Using deterministic code avoids potential numerical errors from LLM reasoning.



---



\# Agent Routing Logic



The system uses a routing layer to determine which tool should answer a query.



Routing rules:



| Query Pattern           | Tool      |

| ----------------------- | --------- |

| jobs / workforce        | Retriever |

| compare / concentration | SQL tool  |

| CAGR / growth           | Math tool |



Example:



```

Query: What CAGR is needed to reach 17000 jobs by 2030?

Tool Used: math\_tool

```



---



\# API Interface



The system exposes a REST API built with FastAPI.



Start the API server:



```

uvicorn api.main:app --reload

```



Open interactive documentation:



```

http://127.0.0.1:8000/docs

```



---



\# Installation



Clone the repository:



```

git clone https://github.com/mmkyadav/cyber-intelligence-system.git

```



Navigate to project:



```

cd cyber-intelligence-system

```



Create virtual environment:



```

python -m venv venv

```



Activate environment:



```

venv\\Scripts\\activate

```



Install dependencies:



```

pip install -r requirements.txt

```



---



\# Running the Pipeline



Run ETL steps in order.



\### Extract text



```

python etl/extract\_text.py

```



\### Build vector store



```

python etl/build\_vector\_store.py

```



\### Extract tables



```

python etl/extract\_tables.py

```



\### Build metrics warehouse



```

python etl/build\_metrics\_layer.py

```



---



\# Run the API



```

uvicorn api.main:app --reload

```



---



\# Example Queries



\### Employment



```

What is the total number of jobs reported?

```



Output



```

7351 jobs

```



---



\### Regional comparison



```

Compare the concentration of Pure-Play cybersecurity firms in the South-West against the National Average

```



---



\### Growth projection



```

What CAGR is needed to reach 17000 jobs by 2030?

```



---



\# Project Structure



```

cyber-intelligence-system

│

├── agent

│   └── agent\_router.py

│

├── api

│   └── main.py

│

├── etl

│   ├── extract\_text.py

│   ├── extract\_tables.py

│   └── build\_vector\_store.py

│

├── rag

│   ├── retriever.py

│   ├── structured\_query.py

│   └── math\_tools.py

│

├── database

│   ├── schema.sql

│   └── inspect\_tables.py

│

├── storage

│

├── requirements.txt

├── README.md

└── .gitignore

```



---



\# Limitations



\* Only a single report is indexed

\* Some regional breakdowns were unavailable in the source document

\* Query routing is rule-based rather than model-driven



---



\# Future Improvements



Possible extensions:



\* LLM-based query planner

\* multi-document indexing

\* automated SQL generation

\* dashboard visualization

\* deployment with Docker



---



\# License



This repository is provided solely for \*\*technical evaluation purposes\*\* as part of a coding assessment.



Commercial use or redistribution without permission is not permitted.



