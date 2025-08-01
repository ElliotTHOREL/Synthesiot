import openai
from abc import ABC, abstractmethod

from agentique.historique_message import ConversationHistory


class BaseAgent(ABC):
    def __init__(self, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        self.client = openai_client
        self.model = model
        self.historic = ConversationHistory()
        self.system_prompt = ""


    async def call_openai(self, messages):
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()

