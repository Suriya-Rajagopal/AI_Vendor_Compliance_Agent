from pydantic import BaseModel, ConfigDict


class VendorModel(BaseModel):
    company_name: str
    website: str
    page_title: str | None = None
    privacy_policy: bool | None = None
    contact_page: bool | None = None
    https_enabled: bool | None = None
    risk_level: str | None = None
    verdict: str | None = None
    reason: str | None = None

    model_config = ConfigDict(from_attributes=True)