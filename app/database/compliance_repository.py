from sqlalchemy.orm import Session

from app.models.compliance_check_entity import ComplianceCheckEntity


class ComplianceRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, compliance: ComplianceCheckEntity):

        self.db.add(compliance)

        self.db.commit()

        self.db.refresh(compliance)

        return compliance

    def get_by_vendor_id(self, vendor_id: int):

        return (
            self.db.query(ComplianceCheckEntity)
            .filter(
                ComplianceCheckEntity.vendor_id == vendor_id
            )
            .order_by(
                ComplianceCheckEntity.checked_at.desc()
            )
            .all()
        )