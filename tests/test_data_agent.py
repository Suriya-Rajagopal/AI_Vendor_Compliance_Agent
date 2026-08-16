from app.agents.data_agent import DataAgent


vendor = {
    "company_name": "Microsoft",
    "website": "https://www.microsoft.com",
    "page_title": "Microsoft",
    "privacy_policy": True,
    "contact_page": True,
    "https_enabled": True
}


compliance = {
    "risk_level": "LOW",
    "verdict": "COMPLIANT",
    "reason": (
        "Vendor satisfies mandatory "
        "compliance requirements."
    )
}


agent = DataAgent()

saved_vendor = agent.save_vendor_result(
    vendor,
    compliance
)


print("Vendor saved successfully.")

print("Database ID:", saved_vendor.id)

print("Company:", saved_vendor.company_name)

print("Verdict:", saved_vendor.verdict)

print("Risk:", saved_vendor.risk_level)