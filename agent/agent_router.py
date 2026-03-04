import json

from rag.retriever import retrieve_answer
from rag.structured_query import compare_pureplay_concentration
from rag.math_tools import calculate_cagr


def route_query(query: str):

    q = query.lower()

    # CAGR queries
    if "cagr" in q or "growth rate" in q or "2030" in q:

        result = calculate_cagr(
            start_value=7351,
            end_value=17000,
            years=9
        )

        return {
            "tool_used": "math_tool",
            "result": result
        }

    # Comparison queries
    elif "compare" in q or "concentration" in q or "south-west" in q:

        result = compare_pureplay_concentration()

        return {
            "tool_used": "structured_query",
            "result": result
        }

    # Employment queries
    elif "job" in q or "employment" in q or "workforce" in q:

        result = retrieve_answer(query)

        return {
            "tool_used": "retriever",
            "result": result
        }

    else:

        return {
            "tool_used": None,
            "result": "Query not recognized."
        }


if __name__ == "__main__":

    queries = [
        "What is the total number of jobs reported?",
        "Compare the concentration of Pure-Play cybersecurity firms in the South-West against the National Average",
        "What CAGR is needed to reach 17000 jobs by 2030?"
    ]

    for q in queries:

        print("\n=================================")
        print("QUERY:", q)

        response = route_query(q)

        print("TOOL USED:", response["tool_used"])

        print("\nRESULT:")
        print(json.dumps(response["result"], indent=4))