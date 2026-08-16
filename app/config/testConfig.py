import app.config.settings as settings

print("Imported settings successfully!")

print("API Key:", settings.GEMINI_API_KEY)
print("Model Name:", settings.MODEL_NAME)
print("Database Name:", settings.DATABASE_NAME)
print("Chroma Collection:", settings.CHROMA_COLLECTION)