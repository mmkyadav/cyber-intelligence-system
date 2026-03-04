from fastapi import FastAPI
from pydantic import BaseModel
from agent.agent_router import route_query

app = FastAPI(
    title="Cyber Intelligence Agent",
    description="Agentic backend for querying the Cyber Ireland 2022 report",
    version="1.0"
)


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def root():
    return {
        "message": "Cyber Intelligence Agent is running",
        "endpoint": "/query"
    }


@app.post("/query")
def query_agent(request: QueryRequest):

    result = route_query(request.query)

    return {
        "query": request.query,
        "tool_used": result["tool_used"],
        "result": result["result"]
    }