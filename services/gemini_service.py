import os
import logging

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

logger = logging.getLogger("CareerGenie")


class GeminiService:

    def __init__(self):

        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY is missing. Please add it to your .env file."
            )

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=api_key,
            temperature=0.4,
            max_tokens=1000
        )

    def generate_response(self, messages):

        try:

            response = self.llm.invoke(messages)

            logger.info("Gemini response generated successfully.")

            return response.content

        except Exception as error:

            logger.exception("Gemini API error occurred.")

            raise error
