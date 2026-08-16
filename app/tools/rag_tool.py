import chromadb
from sentence_transformers import SentenceTransformer


class RAGTool:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./rag/chroma_db"      # ✅ Same as ingest.py
        )

        self.collection = self.client.get_or_create_collection(
            name="policy_collection"    # ✅ Same as ingest.py
        )

        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    def search(self, query):

        embedding = self.embedding_model.encode(query).tolist()

        result = self.collection.query(
            query_embeddings=[embedding],
            n_results=2
        )

        return result["documents"][0]