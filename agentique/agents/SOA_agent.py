from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompts import PROMPT_SYSTEM_SOA_AGENT as PROMPT_SYSTEM
import openai

class SOA_agent(BaseAgent):
    def __init__(self, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.system_prompt = PROMPT_SYSTEM

    async def process_message(self, user_message: str) -> str:
        return await self.call_openai([
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_message}
        ])