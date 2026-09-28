# from openai import OpenAI

# client = OpenAI()

# # Read company information
# with open("company_info.txt", "r") as file:
#     company_info = file.read()

# # Ask the AI a question
# question = input("Ask a question: ")

# response = client.responses.create(
#     model="gpt-5-mini",
#     input=f"""
# You are a customer support assistant for ABC Electronics.

# Use ONLY the company information below to answer the customer's question.

# Company information:
# {company_info}

# Customer question:
# {question}

# If the answer is not in the company information, say:
# "I don't have that information."
# """
# )

# print("\nAI:", response.output_text)

# COMMENTED BECAUSE I HAVE NO CREDITS YET SO THE ERROR OCCUR

#Read company information
# with open("company_info.txt","r") as file:
#     company_info = file.read()

# #Get question from user

# question = input("Ask a Question:").lower()

# if "warranty" in question:
#     print("AI:","Laptops have a 1-year warranty.")

# elif "return" in question:
#     print("AI:","Customers can retun products within 30 days of purchase.")

# elif "shipping" in question:
#     print("AI:","Orders are normally deliverd within 3 to 5 business days.")

# else:
#     print("AI","I don't have that information.")

# Read company information
with open("company_info.txt", "r") as file:
    company_info = file.read()

# Split the document using empty lines
chunks = company_info.split("\n\n")

#Ask the user
question = input("Ask a question:").lower()
#Search each chunk
for chunk in chunks:
    words = question.split()
    # pthon breaks the question into words:
    # ["how", "long", "is", "the", "laptop", "warranty"]

# Show each chunk
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)

    