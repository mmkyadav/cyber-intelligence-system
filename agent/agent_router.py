from agent.intent_classifier import classify_intent
from rag.retriever import retrieve_answer
from rag.structured_query import analyze_region
from rag.math_tools import calculate_cagr


def route_query(query: str):

    intent = classify_intent(query)

    if intent == "retrieval":

        result = retrieve_answer(query)

        tool = "retrieval"

    elif intent == "analytics":

        result = analyze_region(query)

        tool = "analytics"

    elif intent == "math":

        result = calculate_cagr()

        tool = "math_tool"

    else:

        result = {"error": "Intent not recognized"}

        tool = "unknown"

    return {
        "query": query,
        "tool_used": tool,
        "result": result
    }