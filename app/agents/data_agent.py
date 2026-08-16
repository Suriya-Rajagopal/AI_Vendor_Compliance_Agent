from app.database.db_connection import SessionLocal
from app.database.vendor_repository import VendorRepository


class DataAgent:
    """
    Responsible for persisting vendor and compliance data.
    """

    def save_vendor_result(
        self,
        vendor: dict,
        compliance: dict
    ):
        """
        Combines vendor information and compliance result
        and saves the final record into the database.
        """

        vendor_data = {
            "company_name": vendor["company_name"],
            "website": vendor["website"],
            "page_title": vendor.get("page_title"),

            "privacy_policy": vendor.get(
                "privacy_policy"
            ),

            "contact_page": vendor.get(
                "contact_page"
            ),

            "https_enabled": vendor.get(
                "https_enabled"
            ),

            "risk_level": compliance.get(
                "risk_level"
            ),

            "verdict": compliance.get(
                "verdict"
            ),

            "reason": compliance.get(
                "reason"
            )
        }

        db = SessionLocal()

        try:

            repository = VendorRepository(db)

            saved_vendor = repository.save_vendor(
                vendor_data
            )

            return saved_vendor

        finally:

            db.close()