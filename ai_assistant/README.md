 1st-->i have call the api for chats for this i take api keys that is sectret and save in noteboook namead as api keys for 7 days only.

2nd-->i have apply but no response because i donot have enough credits to access or call that api so i am doning manaully.

3rd-->Now i am normally doing how the word from user gets the output from ai which is ai concepts only.
Customer question
       ↓
Find relevant information
       ↓
Give answer

4th--> i understand chunk as separating the document by finding the empty lines.like this 
--- Chunk 1 ---
Company: ABC Electronics

--- Chunk 2 ---
Products:
ABC Electronics sells laptops, phones, headphones, and keyboards.

--- Chunk 3 ---
Return Policy:
Customers can return products within 30 days of purchase.

--- Chunk 4 ---
Shipping:
Orders are normally delivered within 3 to 5 business days.

5th-->currently i am doing the embedding for every chunk as the flow of the program
Company document
       ↓
Split into chunks
       ↓
Create embedding for every chunk
       ↓
Customer asks question
       ↓
Create embedding for question
       ↓
Compare question with ALL chunks
       ↓
Find the most relevant chunk

NOTE:
1.0  → very similar meaning
0.0  → not similar
-1.0 → opposite direction
Customer question
       ↓
   Embedding
       ↓
Compare with document embeddings
       ↓
Find the closest meaning
       ↓
Relevant information