from app.connection import get_db_cursor
from agentique.ModelContextProtocol import ModelContextProtocol

from datetime import datetime
import uuid
import logging

def add_file_in_bdd(name, texte):
    with get_db_cursor() as cursor:
        cursor.execute("""INSERT INTO fichiers 
            (name, texte) VALUES (%s, %s)""",
            (name, texte))

def save_mcp_in_bdd(mon_mcp: ModelContextProtocol):
    #Update fichier
    if mon_mcp.indice_fichier is None:
        logging.info("Création d'un nouveau fichier")
        with get_db_cursor() as cursor:
            name = f"fichier_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
            cursor.execute("""INSERT INTO fichiers 
                (name, texte) VALUES (%s, %s)""",
                (name, mon_mcp.texte))
            mon_mcp.indice_fichier = cursor.lastrowid

    if mon_mcp.indice_bdd is None:
        logging.info("Création d'un nouveau MCP")
        _load_mcp_in_bdd(mon_mcp)
    else:
        logging.info("Mise à jour d'un MCP existant")
        _update_mcp_in_bdd(mon_mcp)

def _load_mcp_in_bdd(mon_mcp: ModelContextProtocol):
    with get_db_cursor() as cursor:
        #Update MCP
        cursor.execute("""INSERT INTO MCP 
            (id_fichier, nb_chunk_agents, nb_lieutenant_agents) VALUES (%s, %s, %s)""",
            (mon_mcp.indice_fichier, len(mon_mcp.liste_chunk_agents), len(mon_mcp.liste_lieutenant_agents)))
        mon_mcp.indice_bdd = cursor.lastrowid

        #Update chunk_agents
        for i, chunk_agent in enumerate(mon_mcp.liste_chunk_agents):
            cursor.execute("""INSERT INTO chunk_agents 
                (id_mcp, position, texte, contexte, summary) VALUES (%s, %s, %s, %s, %s)""",
                (mon_mcp.indice_bdd, i, chunk_agent.texte, chunk_agent.contexte, chunk_agent.summary))
            id_chunk_agent = cursor.lastrowid

        #Update historique
            historique = chunk_agent.historic
            cursor.execute("""INSERT INTO historique 
                (id_chunk_agent) VALUES (%s)""",
                (id_chunk_agent,))
            id_historique = cursor.lastrowid

        #Update messages
            for i, message in enumerate(historique.messages):
                cursor.execute("""INSERT INTO message 
                    (id_historique, numero_message, auteur, content) VALUES (%s, %s, %s, %s)""",
                    (id_historique, i, message.auteur, message.content))

        
        #Update lieutenant_agents
        if len(mon_mcp.liste_lieutenant_agents) == 1:
            lieutenant_agent = mon_mcp.liste_lieutenant_agents[0]
            cursor.execute("""INSERT INTO lieutenant_agents 
                (id_mcp, id_first_sub_agent, id_last_sub_agent, state_orchestrateur, summary, position) VALUES (%s, %s, %s, %s, %s, %s)""",
                (mon_mcp.indice_bdd, lieutenant_agent.id_first_sub_agent, lieutenant_agent.id_last_sub_agent, 1, lieutenant_agent.summary, 0))
        else:
            for i, lieutenant_agent in enumerate(mon_mcp.liste_lieutenant_agents):
                cursor.execute("""INSERT INTO lieutenant_agents 
                    (id_mcp, id_first_sub_agent, id_last_sub_agent, state_orchestrateur, summary, position) VALUES (%s, %s, %s, %s, %s, %s)""",
                    (mon_mcp.indice_bdd, lieutenant_agent.id_first_sub_agent, lieutenant_agent.id_last_sub_agent, 0, lieutenant_agent.summary, i))
            
            oa = mon_mcp.orchestrateur_agent
            cursor.execute("""INSERT INTO lieutenant_agents 
                (id_mcp, id_first_sub_agent, id_last_sub_agent, state_orchestrateur, summary, position) VALUES (%s, %s, %s, %s, %s, %s)""",
                (mon_mcp.indice_bdd, oa.id_first_sub_agent, oa.id_last_sub_agent, 2, oa.summary, len(mon_mcp.lieutenant_agents)))

def _update_mcp_in_bdd(mon_mcp: ModelContextProtocol):
    # Il n'y a qu'à update les historiques pour l'instant (11/08/2025)
    
    with get_db_cursor() as cursor:
        for position_chunk_agent, chunk_agent in enumerate(mon_mcp.liste_chunk_agents):
            cursor.execute("""SELECT id
                FROM historique
                JOIN chunk_agents ON historique.id_chunk_agent = chunk_agents.id
                WHERE chunk_agents.position = %s and chunk_agents.id_mcp = %s""",
            (position_chunk_agent, mon_mcp.indice_bdd))
            id_historique = cursor.fetchone()[0]

            cursor.execute("""SELECT MAX(numero_message)
            FROM message
            WHERE id_historique = %s""",
            (id_historique))
            max_numero_message = cursor.fetchone()[0]

            historique = chunk_agent.historic

            for i in range(max_numero_message+1, len(historique.messages)):
                message = historique.messages[i]

                cursor.execute("""INSERT INTO message 
                (id_historique, numero_message, auteur, content) VALUES (%s, %s, %s, %s)""",
                (id_historique, i, message.auteur, message.content))