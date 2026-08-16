from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.agents.orchestrator_agent import Orchestrator
from app.api.schemas import (
    AgentRunRequest,
    AgentRunResponse
)
from app.database.db_connection import get_db
from app.database.vendor_repository import VendorRepository


router = APIRouter()

orchestrator = Orchestrator()


@router.post(
    "/agent/run",
    response_model=AgentRunResponse
)
def run_agent(
    request: AgentRunRequest
):

    try:

        # Convert Pydantic HttpUrl to normal Python string
        website = str(request.website)

        result = orchestrator.run(
            website
        )

        return result

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


@router.get("/vendors")
def get_all_vendors(
    db: Session = Depends(get_db)
):

    repository = VendorRepository(db)

    return repository.get_all_vendors()


@router.get("/vendors/{vendor_id}")
def get_vendor(
    vendor_id: int,
    db: Session = Depends(get_db)
):

    repository = VendorRepository(db)

    vendor = repository.get_vendor_by_id(
        vendor_id
    )

    if vendor is None:

        raise HTTPException(
            status_code=404,
            detail="Vendor not found"
        )

    return vendor