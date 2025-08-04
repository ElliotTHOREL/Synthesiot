from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompts import PROMPT_SYSTEM_AUXTRANS_AGENT as PROMPT_SYSTEM
from agentique.tools import extract_json_list_from_response
from agentique.agents.chunk_agent import ChunkAgent


import openai
import asyncio

class AuxTransAgent(BaseAgent):
    def __init__(self, list_of_chunk_agents: list[ChunkAgent],id_first_agent: int, id_last_agent: int, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.list_of_chunk_agents=list_of_chunk_agents
        self.id_first_agent=id_first_agent
        self.id_last_agent=id_last_agent
        self.system_prompt = PROMPT_SYSTEM.format(id_first_agent=self.id_first_agent, id_last_agent=self.id_last_agent)



    async def _appel_chunk_agent(self, id_chunk_agent: int, request: str) -> str:
        """Appel l'agent chunk_agent correspondant à l'id_chunk_agent"""
        if id_chunk_agent >= self.id_first_agent and id_chunk_agent <= self.id_last_agent:
            return await self.list_of_chunk_agents[id_chunk_agent].process_message(request)
        else:
            return "Echec de la requête, seuls les agents {} à {} peuvent répondre à la requête".format(self.id_first_agent, self.id_last_agent)

    
    async def process_message(self, user_message: str, pensees: list[str]) -> str:
        messages = [{"role": "system", "content": self.system_prompt}]
        for message in pensees:
            messages.append({"role": "assistant", "content": message})
        
        messages.append({"role": "user", "content": user_message})

        for _ in range(3):
            response = await self.call_openai(messages)
            liste_de_dict = extract_json_list_from_response(response)

            if liste_de_dict is not None:
                pensees.append(response)
                break
        
        tasks=[]
        for dict in liste_de_dict:
            tasks.append(self._appel_chunk_agent(dict["id_agent"], dict["request"]))
            
        results = await asyncio.gather(*tasks)

        for idx in range(len(liste_de_dict)):
            dict = liste_de_dict[idx]
            res=results[idx]
            pensees.append ("""[Agent {}] : {} """.format(dict["id_agent"],res))

        return pensees
