from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentence1 = "Laptops have a 1-year warranty."
sentence2 = "How long is the laptop warranty?"

# Convert both sentences into embeddings
embedding1 = model.encode([sentence1])
embedding2 = model.encode([sentence2])

# Compare their meanings
similarity = cosine_similarity(embedding1, embedding2)

print("Similarity:", similarity[0][0])