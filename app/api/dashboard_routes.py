from fastapi import APIRouter

from app.database.db_connection import SessionLocal
from app.database.vendor_repository import VendorRepository
from app.api.schemas import ComplianceSummaryResponse


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/summary",
    response_model=ComplianceSummaryResponse
)
def get_compliance_summary():

    db = SessionLocal()

    try:

        repository = VendorRepository(db)

        total_vendors = repository.count_all()

        compliant = repository.count_by_verdict(
            "COMPLIANT"
        )

        non_compliant = repository.count_by_verdict(
            "NON_COMPLIANT"
        )

        needs_review = repository.count_by_verdict(
            "NEEDS_REVIEW"
        )

        high_risk = repository.count_by_risk(
            "HIGH"
        )

        medium_risk = repository.count_by_risk(
            "MEDIUM"
        )

        low_risk = repository.count_by_risk(
            "LOW"
        )

        return {
            "total_vendors": total_vendors,
            "compliant": compliant,
            "non_compliant": non_compliant,
            "needs_review": needs_review,
            "high_risk": high_risk,
            "medium_risk": medium_risk,
            "low_risk": low_risk
        }

    finally:

        db.close()