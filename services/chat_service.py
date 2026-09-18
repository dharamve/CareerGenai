from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from config.prompts import SYSTEM_PROMPT
from services.gemini_service import GeminiService


class ChatService:

    def __init__(self):

        self.gemini = GeminiService()

    def get_response(self, conversation):

        messages = [
            SystemMessage(content=SYSTEM_PROMPT)
        ]

        for message in conversation:

            if message["role"] == "user":

                messages.append(
                    HumanMessage(
                        content=message["content"]
                    )
                )

            elif message["role"] == "assistant":

                messages.append(
                    AIMessage(
                        content=message["content"]
                    )
                )

        try:

            response = self.gemini.generate_response(messages)

            return response

        except Exception:

            return (
                "I'm sorry, but I'm currently unable to connect "
                "to the AI service. Please check your API configuration "
                "and try again."
            )
