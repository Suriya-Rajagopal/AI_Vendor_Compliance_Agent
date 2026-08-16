from sqlalchemy.orm import Session

from app.database.vendor_entity import VendorEntity


class VendorRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, vendor: VendorEntity):

        self.db.add(vendor)
        self.db.commit()
        self.db.refresh(vendor)

        return vendor

    def get_by_id(self, vendor_id: int):

        return (
            self.db.query(VendorEntity)
            .filter(VendorEntity.id == vendor_id)
            .first()
        )

    def get_all(self):

        return self.db.query(VendorEntity).all()

    def count_all(self):

        return self.db.query(VendorEntity).count()

    def count_by_verdict(self, verdict: str):

        return (
            self.db.query(VendorEntity)
            .filter(
                VendorEntity.verdict == verdict
            )
            .count()
        )

    def count_by_risk(self, risk_level: str):

        return (
            self.db.query(VendorEntity)
            .filter(
                VendorEntity.risk_level == risk_level
            )
            .count()
        )