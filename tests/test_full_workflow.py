from app.agents.browser_agent import BrowserAgent
from app.agents.compliance_agent import ComplianceAgent

from app.database.db_connection import SessionLocal
from app.database.vendor_repository import VendorRepository
from app.database.vendor_entity import VendorEntity


def main():

    # Step 1 - Browser Agent
    browser = BrowserAgent()

    vendor = browser.run(
        "https://www.microsoft.com"
    )

    print("\n===== BROWSER RESULT =====")
    print(vendor)

    # Step 2 - Compliance Agent
    compliance_agent = ComplianceAgent()

    compliance = compliance_agent.run(vendor)

    print("\n===== COMPLIANCE RESULT =====")
    print(compliance)

    # Step 3 - Database
    db = SessionLocal()

    repository = VendorRepository(db)

    vendor_entity = VendorEntity(
        company_name=compliance.company_name,
        website=vendor["website"],
        page_title=vendor["page_title"],
        privacy_policy=vendor["privacy_policy"],
        contact_page=vendor["contact_page"],
        https_enabled=vendor["https_enabled"],
        risk_level=compliance.risk_level,
        verdict=compliance.verdict,
        reason=compliance.reason
    )

    saved_vendor = repository.save(vendor_entity)

    print("\n===== DATABASE RESULT =====")
    print("Vendor saved successfully.")
    print("Vendor ID:", saved_vendor.id)

    db.close()


if __name__ == "__main__":
    main()