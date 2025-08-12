from app.connection import get_db_cursor
from agentique.ModelContextProtocol import ModelContextProtocol
from agentique.historique_message import ConversationHistory, Message
from agentique.agents.lieutenant_agent import LieutenantAgent
from agentique.agents.SOA_agent import SOA_agent
from agentique.agents.chunk_agent import ChunkAgent

import logging
import openai

async def retrieve_mcp_from_bdd(id_fichier: int, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
    """
    Récupère un MCP à partir de l'id du fichier ou en crée un nouveau si aucun n'existe
    """
    with get_db_cursor() as cursor:
        cursor.execute("""SELECT COUNT(id) 
        FROM MCP
        WHERE id_fichier = %s""",
         (id_fichier,))
        nb_mcp = cursor.fetchone()[0]
        if nb_mcp == 0:
            logging.info(f"Aucun MCP trouvé pour le fichier {id_fichier} -> Création d'un nouveau MCP")
            
            texte = _get_text_from_bdd(id_fichier)
            mon_mcp = await ModelContextProtocol.init_from_texte(texte, openai_client, model)
            return mon_mcp

        elif nb_mcp == 1:
            cursor.execute("""SELECT id 
            FROM MCP 
            WHERE id_fichier = %s""",
             (id_fichier,))
            id_mcp = cursor.fetchone()[0]

            logging.info(f"1 MCP trouvé pour le fichier {id_fichier} -> Récupération du MCP (id = {id_mcp})")
            return  _get_mcp_from_bdd(id_mcp, openai_client, model)
        
        else:
            cursor.execute("""SELECT MAX(id) 
            FROM MCP 
            WHERE id_fichier = %s""",
             (id_fichier,))
            id_mcp = cursor.fetchone()[0]

            logging.info(f"{nb_mcp} MCP trouvés pour le fichier {id_fichier} -> Récupération du MCP le plus récent (id = {id_mcp})")
            return  _get_mcp_from_bdd(id_mcp, openai_client, model)

def _get_text_from_bdd(id_fichier: int):
    with get_db_cursor() as cursor:
        cursor.execute("""SELECT texte 
        FROM fichiers 
        WHERE fichiers.id = %s""",
         (id_fichier,))
        return cursor.fetchone()[0]

def _get_mcp_from_bdd(id_mcp: int, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
    with get_db_cursor() as cursor:

        #Récupération du texte
        cursor.execute("""SELECT fichiers.texte 
        FROM MCP
        JOIN fichiers ON MCP.id_fichier = fichiers.id
        WHERE MCP.id = %s""",
         (id_mcp,))
        texte = cursor.fetchone()[0]

        mon_mcp = ModelContextProtocol(texte, openai_client, model)

        #A initialiser : 
        mon_mcp.liste_chunk_agents = []
        mon_mcp.liste_lieutenant_agents = []
        mon_mcp.orchestrateur_agent = None



        #Récupération des chunk_agents
        cursor.execute("""  
            SELECT id
            FROM chunk_agents
            WHERE id_mcp = %s
            ORDER BY position
        """, (id_mcp,))
        liste_id_chunk_agents = [row[0] for row in cursor.fetchall()]


        for id_chunk_agent in liste_id_chunk_agents:
            chunk_agent = _get_chunk_agent_from_bdd(id_chunk_agent, openai_client, model)
            mon_mcp.liste_chunk_agents.append(chunk_agent)


        #Récupération des lieutenant_agents (+ orchestrateur)
        cursor.execute("""
            SELECT id
            FROM lieutenant_agents
            WHERE id_mcp = %s
            ORDER BY position
        """, (id_mcp,))
        liste_id_lieutenant_agents = [row[0] for row in cursor.fetchall()]

        mon_mcp.liste_lieutenant_agents = [] #Liste des lieutenant_agents de niveau 1 (chefs de chunk_agents)

        for (id_lieutenant_agent,) in liste_id_lieutenant_agents:
            lieutenant_agent, state_orchestrateur = _get_lieutenant_agent_from_bdd(id_lieutenant_agent, list_of_chunk_agents=mon_mcp.liste_chunk_agents, openai_client=openai_client, model=model)
            if state_orchestrateur in (0,1):
                #le lieutenant_agent est de niveau 1 (chef de chunk_agents)
                mon_mcp.liste_lieutenant_agents.append(lieutenant_agent)
            elif state_orchestrateur == 2:
                #le lieutenant_agent est de niveau 2 (chef de lieutenant_agents de niveau 1)
                lieutenant_agent.liste_sub_agents = mon_mcp.liste_lieutenant_agents #On pointe sur les lieutenant_agents de niveau 1
            
            if state_orchestrateur in (1,2):
                #C'est un orchestrateur (petit ou gros)
                mon_mcp.orchestrateur_agent = lieutenant_agent
        
        return mon_mcp

def _get_chunk_agent_from_bdd(id_chunk_agent: int, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
    with get_db_cursor() as cursor:
        cursor.execute("""SELECT position, contexte, texte, summary
        FROM chunk_agents 
        WHERE id = %s""",
         (id_chunk_agent,))
        position, context, texte, summary = cursor.fetchone()

        if position == 0:
            is_premier_chunk = True
        else:
            is_premier_chunk = False

        chunk_agent = ChunkAgent(context, is_premier_chunk, texte, openai_client, model)
        chunk_agent.historic = _get_historic_from_bdd(id_chunk_agent)
        chunk_agent.system_prompt =  chunk_agent.get_system_prompt()
        chunk_agent.summary = summary
        return chunk_agent

def _get_historic_from_bdd(id_chunk_agent: int):
    with get_db_cursor() as cursor:
        cursor.execute("""SELECT message.numero_message, message.auteur, message.content
        FROM historique
        JOIN message ON historique.id = message.id_historique
        WHERE historique.id_chunk_agent = %s""",
         (id_chunk_agent,))
        liste_messages = cursor.fetchall()

        liste_messages_sorted = sorted(liste_messages, key=lambda x: x[0])

        historic = ConversationHistory()
        for message in liste_messages_sorted:
            historic.add_message(Message( auteur=message[1], content=message[2]))
        return historic

def _get_lieutenant_agent_from_bdd(id_lieutenant_agent: int, list_of_chunk_agents: list[ChunkAgent], openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
    with get_db_cursor() as cursor:
        cursor.execute("""SELECT id_first_sub_agent, id_last_sub_agent, summary, state_orchestrateur
        FROM lieutenant_agents 
        WHERE id = %s""",
         (id_lieutenant_agent,))
        id_first_sub_agent, id_last_sub_agent, summary, state_orchestrateur = cursor.fetchone()
        

        lieutenant_agent = LieutenantAgent(list_of_chunk_agents, id_first_sub_agent, id_last_sub_agent, openai_client, model)   
        lieutenant_agent.summary = summary
        lieutenant_agent.soa_agent = SOA_agent(lieutenant_agent.summary, openai_client, model)
        return lieutenant_agent, state_orchestrateur