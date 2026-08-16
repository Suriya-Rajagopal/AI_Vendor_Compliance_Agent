from pydantic import BaseModel, HttpUrl


class AgentRunRequest(BaseModel):
    website: HttpUrl


class AgentRunResponse(BaseModel):
    vendor_id: int
    vendor: dict
    compliance: dict

class ComplianceSummaryResponse(BaseModel):

    total_vendors: int

    compliant: int

    non_compliant: int

    needs_review: int

    high_risk: int

    medium_risk: int

    low_risk: int