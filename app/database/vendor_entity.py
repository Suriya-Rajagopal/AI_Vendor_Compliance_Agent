from sqlalchemy import Column, Integer, String, Boolean, Text

from app.database.db_connection import Base


class VendorEntity(Base):

    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String(200), nullable=False)

    website = Column(String(500), nullable=False)

    page_title = Column(String(500))

    privacy_policy = Column(Boolean)

    contact_page = Column(Boolean)

    https_enabled = Column(Boolean)

    risk_level = Column(String(50))
    
    verdict = Column(String(50))

    reason = Column(Text)