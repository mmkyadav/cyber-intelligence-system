from fastapi import FastAPI
from pydantic import BaseModel
from agent.agent_router import route_query


app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
def query_endpoint(request: QueryRequest):

    response = route_query(request.query)

    return response