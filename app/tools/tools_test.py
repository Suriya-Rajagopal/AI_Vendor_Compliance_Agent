from app.agents.orchestrator_agent import OrchestratorAgent

agent = OrchestratorAgent()

print(agent.run("What is the current time?"))

print("--------------------------------")

print(agent.run("Tell me about Microsoft"))