from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompts import PROMPT_SYSTEM_COMMUNICATION_AGENT as PROMPT_SYSTEM

import openai

class ComAgent(BaseAgent):
    def __init__(self, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.system_prompt = PROMPT_SYSTEM

    async def process_message(self, user_message: str, pensees: list[str]) -> str:
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.append({"role": "user", "content": user_message})

        for message in pensees:
            messages.append({"role": "assistant", "content": message})
        
        response = await self.call_openai(messages)
        return response
    


    

