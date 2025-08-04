from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompts import PROMPT_SYSTEM_LIEUTENANT_AGENT as PROMPT_SYSTEM
from agentique.agents.auxtrans import AuxTransAgent
from agentique.agents.com_agent import ComAgent
from agentique.agents.chunk_agent import ChunkAgent

import openai
import re
import logging

class LieutenantAgent(BaseAgent):
    def __init__(self, list_of_chunk_agents: list[ChunkAgent], id_first_chunk : int, id_last_chunk : int, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.list_of_chunk_agents = list_of_chunk_agents
        self.id_first_chunk=id_first_chunk
        self.id_last_chunk=id_last_chunk
        self.system_prompt = PROMPT_SYSTEM.format(id_first_agent=self.id_first_chunk, id_last_agent=self.id_last_chunk)
        
        self.auxtrans_agent = AuxTransAgent(list_of_chunk_agents, id_first_chunk, id_last_chunk, openai_client, model)
        self.com_agent = ComAgent(openai_client, model)
    
    @staticmethod
    def parse_lieutenant_response(texte: str):
        texte = texte.strip()

        # Cas exact "CHOIX: TERMINER"
        if re.fullmatch(r"CHOIX:\s*TERMINER", texte, flags=re.IGNORECASE):
            return {"type": "terminer"}

        # Cas "QUESTION: ..." avec contenu
        match_question = re.match(r"QUESTION:\s*(.+)", texte, flags=re.IGNORECASE | re.DOTALL)
        if match_question:
            contenu = match_question.group(1).strip()
            if contenu:
                return {"type": "question", "contenu": contenu}

        # Si aucun des cas ne matche : erreur
        return {
            "type": "erreur",
            "message": "Format invalide : la réponse n'est ni un choix valide ni une question identifiable.",
            "brut": texte,
        }




    async def process_message(self, user_message: str, plan_of_action: str, max_steps: int = 10) -> str:
        pensees = []

        fini = False
        nb_ite = 0
        while not fini and nb_ite < max_steps:
            nb_ite += 1
            fini, pensees =await self._process_one_step(user_message, plan_of_action, pensees)
        
        synthese = await self.com_agent.process_message(user_message, pensees)
        return synthese

    async def _process_one_step(self, user_message: str, plan_of_action : str, pensees : list[str]):
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content":"[Planificateur] : {}".format(plan_of_action)})
        
        for message in pensees:
            messages.append({"role": "assistant", "content": message})
        
        for try_number in range(5):
            response = await self.call_openai(messages)
            lieutenant_response = self.parse_lieutenant_response(response)
            if lieutenant_response["type"] == "terminer":
                return True, pensees
            elif lieutenant_response["type"] == "question":
                pensees = await self.auxtrans_agent.process_message(lieutenant_response["contenu"], pensees)
                return False, pensees
            else:
                logging.warning(f"Format invalide : {lieutenant_response['message']}, brut : {lieutenant_response['brut']}")

        raise ValueError("Nombre d'essais maximal atteint. Le lieutenant ne renvoit pas un format valide.")



    



