from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

intent_examples = {

    "retrieval": [
        "How many cybersecurity professionals work in Ireland",
        "What is the workforce size",
        "Where is the employment number stated",
        "How many people work in the cyber security sector",
        "What is the employment number",
        "What is the workforce size of cybersecurity",
        "How many jobs are reported"
    ],

    "analytics": [
        "Compare regional concentration",
        "Compare South-West and national firms",
        "What proportion of firms are in Cork",
        "What percentage of firms are in Kerry",
        "How concentrated is the cybersecurity sector",
        "Regional distribution of cybersecurity firms",
        "What share of firms are in South-West"
    ],

    "math": [
    "What CAGR is required",
    "What growth rate is needed",
    "How fast must employment grow",
    "Calculate CAGR to reach a target",
    "How quickly must jobs increase",
    "growth needed to reach 17000 jobs",
    "annual growth rate to reach target",
    "increase to hit 2030 goal",
    "growth required to reach employment target",
    "how quickly must employment grow",
    "what growth rate is required",
    "employment growth needed"
]
}

intent_embeddings = {
    intent: model.encode(examples)
    for intent, examples in intent_examples.items()
}

def classify_intent(query: str):

    query_embedding = model.encode([query])

    scores = {}

    for intent, embeddings in intent_embeddings.items():

        similarity = cosine_similarity(query_embedding, embeddings)

        scores[intent] = np.max(similarity)

    best_intent = max(scores, key=scores.get)

    return best_intent