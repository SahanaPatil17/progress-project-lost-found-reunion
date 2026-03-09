import faiss
import pickle
import numpy as np
import ollama
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize

# Load vector database
index = faiss.read_index("vector.index")

# Load dataset
df = pickle.load(open("data.pkl", "rb"))

# Load text model
text_model = SentenceTransformer("all-MiniLM-L6-v2")

def search(query, k=3):

    query_embedding = text_model.encode([query], normalize_embeddings=True)

    # Pad image part with zeros
    padding = np.zeros((1, 512))

    combined_query = np.hstack((query_embedding, padding))

    combined_query = normalize(combined_query)

    distances, indices = index.search(combined_query, k)

    results = df.iloc[indices[0]].copy()

    # cosine similarity already returned
    results["confidence"] = distances[0]

    return results


def explain_match(query, description):

    prompt = f"""
A student reported losing this item:
{query}

A potential match from the lost & found database:
{description}

Explain in 1-2 sentences why this could be the same item.
Only use the given information.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role":"user","content":prompt}]
    )

    return response["message"]["content"]