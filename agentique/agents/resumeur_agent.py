from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompt.resumeur_agent import PROMPT_SYSTEM

import openai


class ResumeurAgent(BaseAgent):
    def __init__(self, id_first_sub_agent: int, id_last_sub_agent: int, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.id_first_sub_agent = id_first_sub_agent
        self.id_last_sub_agent = id_last_sub_agent
        self.system_prompt = PROMPT_SYSTEM
    

    async def process_message(self, liste_resumes: list[str]) -> str:
        resumes ="""Voici les résumés des différentes parties du document : \n\n\n"""
        zipped_data = zip(range(self.id_first_sub_agent, self.id_last_sub_agent + 1), liste_resumes)
        for id_agent, resume in zipped_data:
            resumes += f"Résumé de la partie {id_agent} : \n {resume}\n\n"
        

        messages = [{"role": "system", "content": self.system_prompt}]
        messages.append({"role": "user", "content": resumes})
        return await self.call_openai(messages)



