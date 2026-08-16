from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.db_connection import Base


class ComplianceCheckEntity(Base):

    __tablename__ = "compliance_checks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    vendor_id = Column(
        Integer,
        ForeignKey("vendors.id"),
        nullable=False
    )

    risk_level = Column(
        String,
        nullable=False
    )

    verdict = Column(
        String,
        nullable=False
    )

    reason = Column(
        Text,
        nullable=True
    )

    checked_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )