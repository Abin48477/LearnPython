# Read company information
with open("company_info.txt", "r") as file:
    company_info = file.read()

# Split the document using empty lines
chunks = company_info.split("\n\n")
# Ask the user
question = input("Ask a question: ").lower()

# Search for important keywords
keywords = ["warranty", "return", "shipping", "products"]

for chunk in chunks:
    chunk_lower = chunk.lower()

    for keyword in keywords:
        if keyword in question and keyword in chunk_lower:
            print("\nRelevant information:")
            print(chunk)
            break