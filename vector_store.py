from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

index = None
chunks = []

def create_vector_store(text_chunks):
    global index, chunks
    chunks = text_chunks

    embeddings = model.encode(text_chunks)
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    print("Vector store created with", len(text_chunks), "chunks")


def search_vector_store(query, k=5):
    global index, chunks

    if index is None:
        return ""

    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, k)

    results = []
    for i in indices[0]:
        if i < len(chunks):
            results.append(chunks[i])

    return "\n".join(results)