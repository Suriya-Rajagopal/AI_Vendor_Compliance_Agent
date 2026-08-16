from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db_connection import get_db
from app.database.vendor_repository import VendorRepository
from app.models.vendor_model import VendorModel


router = APIRouter()


@router.get(
    "/vendors/",
    response_model=list[VendorModel]
)
def get_all_vendors(
    db: Session = Depends(get_db)
):
    try:
        repository = VendorRepository(db)

        vendors = repository.get_all()

        return vendors

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


@router.get(
    "/vendors/{vendor_id}",
    response_model=VendorModel
)
def get_vendor(
    vendor_id: int,
    db: Session = Depends(get_db)
):
    try:
        repository = VendorRepository(db)

        vendor = repository.get_by_id(vendor_id)

        if vendor is None:
            raise HTTPException(
                status_code=404,
                detail="Vendor not found"
            )

        return vendor

    except HTTPException:
        raise

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )