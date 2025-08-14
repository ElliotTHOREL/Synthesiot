import openai
from abc import ABC

import logging


class BaseAgent(ABC):
    call_count = 0

    def __init__(self, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        self.client = openai_client
        self.model = model
        self.system_prompt = ""

    async def async_init(self):
        pass


    async def call_openai(self, messages):
        BaseAgent.call_count += 1

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
        )
        logging.info("------------------------------------------------------------------------------------------")
        logging.info("------------------------------------------------------------------------------------------")
        logging.info("------------------------------------------------------------------------------------------")
        logging.info("=========== Début d'une nouvelle conversation ====================================================")
        for i, msg in enumerate(messages):
            role = msg.get("role", "unknown").capitalize()
            content = msg.get("content", "").strip()
            logging.info(f"MESSAGE {i+1} ({role}):\n{content}")
        logging.info(f"Response : {response.choices[0].message.content.strip()}")
        logging.info("=========== Fin de la conversation ================================================================")
        logging.info("------------------------------------------------------------------------------------------")
        logging.info("------------------------------------------------------------------------------------------")
        logging.info("------------------------------------------------------------------------------------------")

        return response.choices[0].message.content.strip()

