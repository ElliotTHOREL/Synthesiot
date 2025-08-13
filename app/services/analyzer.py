from app.database.read import retrieve_mcp_from_bdd, get_fichier_from_texte
from app.database.update import save_mcp_in_bdd
from app.config import openai_client, openai_model

from agentique.ModelContextProtocol import ModelContextProtocol

async def quickly_summarize_file(id_fichier: int):
    mon_mcp = await retrieve_mcp_from_bdd(id_fichier, openai_client, openai_model)
    save_mcp_in_bdd(mon_mcp)
    return mon_mcp.orchestrateur_agent.summary

async def ask_file(id_fichier: int, user_request: str):
    mon_mcp = await retrieve_mcp_from_bdd(id_fichier, openai_client, openai_model)
    answer = await mon_mcp.process_message(user_request)

    save_mcp_in_bdd(mon_mcp)
    return answer

async def quickly_summarize_text(texte: str):
    id_fichier = get_fichier_from_texte(texte)
    if id_fichier is not None:
        return await quickly_summarize_file(id_fichier)
    else:
        mon_mcp = await ModelContextProtocol.init_from_texte(texte, openai_client, openai_model)
        save_mcp_in_bdd(mon_mcp)
        return mon_mcp.orchestrateur_agent.summary

async def ask_text(texte: str, user_request: str):
    id_fichier = get_fichier_from_texte(texte)
    if id_fichier is not None:
        return await ask_file(id_fichier, user_request)
    else:
        mon_mcp = await ModelContextProtocol.init_from_texte(texte, openai_client, openai_model)
        answer = await mon_mcp.process_message(user_request)
        save_mcp_in_bdd(mon_mcp)
        return answer