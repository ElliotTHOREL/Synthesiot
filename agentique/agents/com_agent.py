from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompt.com_agent import PROMPT_SYSTEM
from agentique.historique_message import ConversationHistory

import openai


class ComAgent(BaseAgent):
    def __init__(self, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.system_prompt = PROMPT_SYSTEM

    async def process_message(self, user_message: str, historic: ConversationHistory) -> str:
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.append({"role": "user", "content": "[Demande de l'orchestrateur] : " + user_message})

        for message in historic.messages:
            if message.auteur == "lieutenant":
                messages.append({"role": "assistant", "content": "[Message du lieutenant] : \n\n{}".format(message.content)})
            elif message.auteur == "synthetiseur":
                messages.append({"role": "assistant", "content": "[Réponse de l'agent subalterne] : \n\n{}".format(message.content)})
        

        response = await self.call_openai(messages)
        return response
    


    

