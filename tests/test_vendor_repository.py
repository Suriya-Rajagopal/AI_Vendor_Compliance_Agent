from app.database.db_connection import SessionLocal
from app.database.vendor_repository import VendorRepository
from app.database.vendor_entity import VendorEntity


def test_vendor_repository():

    db = SessionLocal()

    repository = VendorRepository(db)

    vendor = VendorEntity(
        company_name="Microsoft",
        website="https://www.microsoft.com",
        page_title="Microsoft",
        privacy_policy=True,
        contact_page=True,
        https_enabled=True,
        risk_level="LOW",
        verdict="COMPLIANT",
        reason="Vendor satisfies all mandatory compliance requirements."
    )

    saved_vendor = repository.save(vendor)

    print("Vendor saved successfully.")
    print("Vendor ID:", saved_vendor.id)

    retrieved_vendor = repository.get_by_id(saved_vendor.id)

    print("\nRetrieved Vendor:")
    print("Company:", retrieved_vendor.company_name)
    print("Website:", retrieved_vendor.website)
    print("Risk:", retrieved_vendor.risk_level)
    print("Verdict:", retrieved_vendor.verdict)
    print("Reason:", retrieved_vendor.reason)

    db.close()


if __name__ == "__main__":
    test_vendor_repository()