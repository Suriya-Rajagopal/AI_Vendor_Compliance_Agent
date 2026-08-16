from app.agents.browser_agent import BrowserAgent

agent = BrowserAgent()

response = agent.run("https://www.microsoft.com")

print(response)