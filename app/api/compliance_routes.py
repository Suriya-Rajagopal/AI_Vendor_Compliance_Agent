from fastapi import APIRouter

from app.database.db_connection import SessionLocal
from app.database.compliance_repository import ComplianceRepository


router = APIRouter(
    prefix="/compliance",
    tags=["Compliance"]
)


@router.get("/vendor/{vendor_id}")
def get_vendor_compliance_history(
    vendor_id: int
):

    db = SessionLocal()

    try:

        repository = ComplianceRepository(db)

        history = repository.get_by_vendor_id(
            vendor_id
        )

        return history

    finally:

        db.close()