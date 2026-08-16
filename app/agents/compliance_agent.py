from app.services.gemini_service import GeminiService
from app.tools.rag_tool import RAGTool
from app.models.compliance_model import ComplianceModel


class ComplianceAgent:
    """
    AI Agent responsible for evaluating vendor compliance
    using RAG + Gemini.
    """

    def __init__(self):
        self.gemini = GeminiService()
        self.rag = RAGTool()

    def run(self, vendor: dict) -> ComplianceModel:
        """
        Evaluates vendor compliance.
        """

        # Retrieve relevant policy from ChromaDB
        policy = self.rag.search("Vendor Compliance Policy")
            
        # Build prompt
        prompt = f"""
You are an Enterprise Vendor Compliance Officer.

Below is the vendor information collected by the Browser Agent.

Vendor Information:
{vendor}

Relevant Company Policy:
{policy}

Analyze the vendor against the policy.

Return ONLY valid JSON.

Example:

{{
    "company_name": "Microsoft",
    "risk_level": "LOW",
    "verdict": "COMPLIANT",
    "reason": "Vendor satisfies HTTPS, Privacy Policy and Contact Information requirements."
}}

Rules:
1. Return ONLY JSON.
2. Do NOT return markdown.
3. Do NOT return explanations.
4. Do NOT wrap JSON inside ```json.
"""

        # Get structured JSON directly from Gemini
        response_json = self.gemini.ask_json(prompt)

        # Convert JSON into Pydantic model
        compliance = ComplianceModel(**response_json)

        return compliance