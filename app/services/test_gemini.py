from app.services.gemini_service import GeminiService   

gemini = GeminiService()
response = gemini.generate_text("Hello!")

print(response) 

