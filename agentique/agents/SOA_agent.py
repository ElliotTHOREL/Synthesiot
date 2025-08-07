from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompt.SOA_agent import PROMPT_SYSTEM
import openai

class SOA_agent(BaseAgent):
    def __init__(self, resume : str, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.resume = resume
        self.system_prompt = PROMPT_SYSTEM.format(self.resume)

    async def process_message(self, user_message: str) -> str:
        return await self.call_openai([
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"La demande de l'orchestrateur est la suivante : {user_message}"}
        ])