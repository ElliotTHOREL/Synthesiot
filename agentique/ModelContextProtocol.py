from agentique.agents.chunk_agent import ChunkAgent
from agentique.agents.lieutenant_agent import LieutenantAgent
from agentique.agents.SOA_agent import SOA_agent

import openai
import time
import logging
from typing import Optional




class ModelContextProtocol:
    def __init__(self, texte : str,  openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo", indice_fichier: Optional[int] = None):
        self.texte = texte
        self.client = openai_client
        self.model = model

        self.indice_bdd = None #Correspond à mcp_id dans la base de données
        self.indice_fichier = indice_fichier #Correspond à id_fichier dans la base de données

    
    @classmethod
    async def init_from_texte(cls, texte: str, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        mcp = cls(texte, openai_client, model)
        mcp.liste_chunk_agents = await mcp._init_chunk_agents()
        mcp.liste_lieutenant_agents = mcp._init_lieutenant_agents()
        mcp.orchestrateur_agent = mcp._get_orchestrateur_agent()
        await mcp.orchestrateur_agent.async_init()
        print(mcp.orchestrateur_agent.summary)
        return mcp



    def _get_chunks(self, chunk_size: int = 3000, overlap: int = 150) -> list[str]:
        mots = self.texte.split()
        logging.info(f"Nombre de mots : {len(mots)}")

        chunks = []
        for i in range(0, len(mots), chunk_size-overlap):
            chunk = mots[i:i+chunk_size]
            chunks.append(" ".join(chunk))
        return chunks


    async def _init_chunk_agents(self):
        time_start = time.time()
        chunks = self._get_chunks()
        list_of_chunk_agents=[]
        is_premier_chunk = True
        context = ""
        for chunk in chunks:
            new_chunk_agent = ChunkAgent.init_from_texte(context, is_premier_chunk, chunk, openai_client=self.client, model=self.model)
            list_of_chunk_agents.append(new_chunk_agent)

            is_premier_chunk = False
            context = await new_chunk_agent.generate_next_context()
        time_end = time.time()
        logging.info(f"Temps d'initialisation des agents de chunk : {time_end - time_start} secondes")
        logging.info(f"Nombre de chunks : {len(chunks)}")

        return list_of_chunk_agents

    def _init_lieutenant_agents(self, nb_subalternes =5):
        liste_lieutenant_agents=[]
        n = len(self.liste_chunk_agents)
        for i in range(0, n , nb_subalternes):
            id_first_agent = i
            id_last_agent = min((i + nb_subalternes), n)-1
            new_agent = LieutenantAgent(self.liste_chunk_agents, id_first_agent, id_last_agent, openai_client = self.client, model=self.model)
            liste_lieutenant_agents.append(new_agent)

        return liste_lieutenant_agents        
    
    def _get_orchestrateur_agent(self):
        if len(self.liste_lieutenant_agents) ==1:
            return self.liste_lieutenant_agents[0]
        else:
            orchestrateur_agent = LieutenantAgent(self.liste_lieutenant_agents, 0, len(self.liste_lieutenant_agents)-1, openai_client = self.client, model=self.model)
            return orchestrateur_agent


    async def process_message(self, user_request: str):
        response = await self.orchestrateur_agent.process_message(user_request)
        return response

