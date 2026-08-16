# # Step 2.4
# Import Libraries
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from sentence_transformers import SentenceTransformer
# # Step 2.5
# Create Chroma Client
client = chromadb.PersistentClient(path="./rag/chroma_db")
# # Step 2.6
# Create Collection
collection = client.get_or_create_collection(name="policy_collection")
# # Step 2.7
# Load Embedding Model
model = SentenceTransformer( "all-MiniLM-L6-v2")
# # Step 2.8
# Read Policy File
with open( "rag/vendor_compliance_policy.txt",encoding="utf-8"
) as file:

    text = file.read()
# # Step 2.9
# Split into Chunks
splitter = RecursiveCharacterTextSplitter(

    chunk_size=300,

    chunk_overlap=50

)


# # Step 2.10
# Create Embeddings
chunks = splitter.split_text(text)
# # Step 2.11
# Store into ChromaDB
for index, chunk in enumerate(chunks):

    embedding = model.encode(
        chunk
    ).tolist()

    collection.add(

        ids=[str(index)],

        documents=[chunk],

        embeddings=[embedding]

    )
# # Step 2.12
# Print Success
print("Policy Successfully Loaded into ChromaDB")