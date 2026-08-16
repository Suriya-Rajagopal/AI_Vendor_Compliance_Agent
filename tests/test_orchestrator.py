from app.agents.orchestrator_agent import Orchestrator


orchestrator = Orchestrator()

result = orchestrator.run(
    "https://www.microsoft.com"
)

print("\n")
print("=" * 60)
print("FINAL COMPLIANCE RESULT")
print("=" * 60)

print(result)