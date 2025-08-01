from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompts import PROMPT_SYSTEM_LIEUTENANT_AGENT as PROMPT_SYSTEM
from agentique.banque_de_prompts import PROMPT_EXECUTE_PLAN_OF_ACTION_LIEUTENANTS_AGENT as PROMPT_EXECUTE_PLAN_OF_ACTION
from agentique.banque_de_prompts import PROMPT_FINAL_RESPONSE_LIEUTENANTS_AGENT as PROMPT_FINAL_RESPONSE
from agentique.historique_message import Message, MessageRole
from agentique.agents.chunk_agent import ChunkAgent
from agentique.tools import extract_json_list_from_response


import openai
import asyncio

class LieutenantsAgent(BaseAgent):
    def __init__(self, list_of_chunk_agents: list[ChunkAgent], id_first_chunk : int, id_last_chunk : int, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.list_of_chunk_agents = list_of_chunk_agents
        self.id_first_agent=id_first_chunk
        self.id_last_agent=id_last_chunk

    
    
    def _get_system_prompt(self) -> str:
        return PROMPT_SYSTEM.format(id_first_agent=self.id_first_agent, id_last_agent=self.id_last_agent)

    def _get_plan_of_action_prompt(self) -> str:
        return PROMPT_EXECUTE_PLAN_OF_ACTION.format(id_first_agent=self.id_first_agent, id_last_agent=self.id_last_agent)

    def _get_final_response_prompt(self) -> str:
        return PROMPT_FINAL_RESPONSE


    async def _appel_chunk_agent(self, id_chunk_agent: int, request: str) -> str:
        """Appel l'agent chunk_agent correspondant à l'id_chunk_agent"""
        if id_chunk_agent >= self.id_first_agent and id_chunk_agent <= self.id_last_agent:
            return await self.list_of_chunk_agents[id_chunk_agent].process_message(request)
        else:
            return "Echec de la requête, seuls les agents {} à {} peuvent répondre à la requête".format(self.id_first_agent, self.id_last_agent)




    async def _process_one_step(self, plan_of_action : str, pensees : list[str]):
        messages = [{"role": "system", "content": self._get_system_prompt()}]
        messages.append({"role": "system", "content": self._get_plan_of_action_prompt()})
        messages.append({"role": "user", "content": plan_of_action})
        
        for message in pensees:
            messages.append({"role": "assistant", "content": message})
        
        for try_number in range(3):
            response = await self.call_openai(messages)
            liste_de_dict = extract_json_list_from_response(response)

            if liste_de_dict is not None:
                pensees.append(response)
                print(response)
                break


    
        if len(liste_de_dict) > 0:
            tasks=[]
            for dict in liste_de_dict:
                tasks.append(self._appel_chunk_agent(dict["id_agent"], dict["request"]))
            
            results = await asyncio.gather(*tasks)


            for idx in range(len(liste_de_dict)):
                dict = liste_de_dict[idx]
                res=results[idx]
                pensees.append ("""[Agent {}] : {} """.format(dict["id_agent"],res))
                print(pensees[-1])
                
            return False
        else:
            return True

    async def _generate_reponse_finale(self, user_request: str, plan_of_action: str, pensees: list[str]) -> str:
        messages = [{"role": "system", "content": self._get_system_prompt()}]
        messages.append({"role": "system", "content": self._get_final_response_prompt()})
        messages.append({"role": "user", "content": user_request})
        messages.append({"role": "assistant", "content": f"[PLanificateur] {plan_of_action}"})
        for message in pensees:
            messages.append({"role": "assistant", "content": message})
        response = await self.call_openai(messages)
        return response


    async def execute_plan_of_action(self, user_request: str, plan_of_action: str) -> str:
        """Le message vient de l'orchestrateur"""
        max_steps = 10

        pensees = []
        num_step = 0
        while not await self._process_one_step(plan_of_action, pensees) and num_step < max_steps:
            print(f"Etape {num_step}/{max_steps}")
            num_step += 1
        
        return await self._generate_reponse_finale(user_request, plan_of_action, pensees)

    



