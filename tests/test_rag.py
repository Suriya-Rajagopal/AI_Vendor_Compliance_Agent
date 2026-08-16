from app.tools.rag_tool import RAGTool

rag = RAGTool()
result = rag.search("Privacy policy")
print(result)