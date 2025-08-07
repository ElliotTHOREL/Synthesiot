from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompt.synthe_agent import PROMPT_SYSTEM

import openai


class SyntheAgent(BaseAgent):
    def __init__(self, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.system_prompt = PROMPT_SYSTEM

    async def process_message(self, user_message: str, liste_de_dict: list[dict]) -> str:
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.append({"role": "user", "content": "Question de l'utilisateur : \n" + user_message})

        enquete = "Questions de l'orchestrateur et réponses des agents : \n \n"
        for dict in liste_de_dict:
            enquete += "[Orchestrateur à l'agent {}] : {}\n".format(dict["id_agent"], dict["request"])
            enquete += "[Réponse de l'agent {}] : {}\n".format(dict["id_agent"], dict["result"])

        messages.append({"role": "user", "content": enquete})

        return await self.call_openai(messages)