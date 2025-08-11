from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompt.auxtrans_agent import PROMPT_SYSTEM
from agentique.tools import extract_json_list_from_response
from agentique.agents.synthe_agent import SyntheAgent

import openai
import asyncio
import logging

class AuxTransAgent(BaseAgent):
    def __init__(self, list_of_sub_agents: list[BaseAgent],id_first_agent: int, id_last_agent: int, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.list_of_sub_agents=list_of_sub_agents
        self.id_first_agent=id_first_agent
        self.id_last_agent=id_last_agent
        self.system_prompt = None
        
        self.synthe_agent = SyntheAgent(openai_client, model)

    
    def get_system_prompt(self):
        if self.system_prompt is not None:
            return self.system_prompt
        else:
            sub_agents_list = self.list_of_sub_agents[self.id_first_agent:self.id_last_agent+1]
            
            zip_sub_agents_id = zip(sub_agents_list, range(self.id_first_agent, self.id_last_agent+1))
            resume_agents ="\n".join([f"Agent {id} : {agent.summary}" for (agent,id) in zip_sub_agents_id])

            self.system_prompt = PROMPT_SYSTEM.format(id_first_agent=self.id_first_agent, id_last_agent=self.id_last_agent, resume_agents=resume_agents)
            return self.system_prompt


    async def _appel_sub_agent(self, id_sub_agent: int, request: str) -> str:
        """Appel l'agent sub_agent correspondant à l'id_sub_agent"""
        if id_sub_agent >= self.id_first_agent and id_sub_agent <= self.id_last_agent:
            return await self.list_of_sub_agents[id_sub_agent].process_message(request)
        else:
            return "Echec de la requête, seuls les agents {} à {} peuvent répondre à la requête".format(self.id_first_agent, self.id_last_agent)

    
    async def generate_liste_dict(self, user_message: str) -> str:
        messages = [{"role": "system", "content": self.get_system_prompt()}]
        messages.append({"role": "user", "content": user_message})
        

        for _ in range(3):
            response = await self.call_openai(messages)
            liste_de_dict = extract_json_list_from_response(response)

            if liste_de_dict is not None:
                break
            else:
                logging.warning(f"Echec de la génération de la liste de dict")
                liste_de_dict = []

        return liste_de_dict
    


    async def process_message(self, user_message: str) -> str:

        liste_de_dict = await self.generate_liste_dict(user_message)

        tasks=[]
        for dict in liste_de_dict:
            tasks.append(self._appel_sub_agent(dict["id_agent"], dict["request"]))
            
        results = await asyncio.gather(*tasks)

        for idx in range(len(liste_de_dict)):
            dict = liste_de_dict[idx]
            res=results[idx]
            dict["result"] = res

        return await self.synthe_agent.process_message(user_message, liste_de_dict)
