from sentence_transformers import SentenceTransformer

# Load a free embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

text = "Laptops have a 1-year warranty."

# Convert text into numbers
embedding = model.encode(text)

print(embedding)
print("Number of values:", len(embedding))