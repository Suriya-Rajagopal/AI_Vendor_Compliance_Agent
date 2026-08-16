import json

from google import genai

from app.config.settings import (
    GEMINI_API_KEY,
    MODEL_NAME
)


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = MODEL_NAME

    def ask(self, prompt: str) -> str:
        """
        Returns plain text response
        """

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text

    def ask_json(self, prompt: str) -> dict:
        """
        Returns JSON response
        """

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        text = response.text.strip()

        # Remove markdown if Gemini returns it
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)