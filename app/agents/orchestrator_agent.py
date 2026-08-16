from app.agents.browser_agent import BrowserAgent
from app.agents.compliance_agent import ComplianceAgent
from app.agents.data_agent import DataAgent


class Orchestrator:

    """
    Coordinates the complete vendor compliance workflow.
    """

    def __init__(self):

        self.browser_agent = BrowserAgent()

        self.compliance_agent = ComplianceAgent()

        self.data_agent = DataAgent()

    def run(self, website: str):

        print("\nStarting vendor compliance workflow...")

        # --------------------------------------------------
        # Step 1: Browser Agent
        # --------------------------------------------------

        print("\n[1/3] Running Browser Agent...")

        vendor = self.browser_agent.run(website)

        print("Vendor information collected.")

        # --------------------------------------------------
        # Step 2: Compliance Agent
        # --------------------------------------------------

        print("\n[2/3] Running Compliance Agent...")

        compliance = self.compliance_agent.run(vendor)

        print("Compliance evaluation completed.")

        # --------------------------------------------------
        # Step 3: Data Agent
        # --------------------------------------------------

        print("\n[3/3] Saving result to database...")

        saved_vendor = self.data_agent.save_vendor_result(
            vendor,
            compliance.model_dump()
        )

        print("Result saved successfully.")

        # --------------------------------------------------
        # Final Response
        # --------------------------------------------------

        return {
            "vendor_id": saved_vendor.id,
            "vendor": vendor,
            "compliance": compliance.model_dump()
        }