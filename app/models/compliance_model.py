from pydantic import BaseModel


class ComplianceModel(BaseModel):

    company_name: str

    risk_level: str

    verdict: str

    reason: str