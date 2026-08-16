from app.agents.compliance_agent import ComplianceAgent


vendor = {

    "company_name": "Microsoft",

    "website": "https://www.microsoft.com",

    "privacy_policy": True,

    "contact_page": True,

    "https_enabled": True

}

agent = ComplianceAgent()

result = agent.run(vendor)

print(result)

print(result.model_dump())