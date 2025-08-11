from agentique.ModelContextProtocol import ModelContextProtocol


import os
import openai
import asyncio
from dotenv import load_dotenv 
import logging

load_dotenv() 

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs/logs3.txt',
    filemode='a'  # 'w' pour écraser, 'a' pour ajouter
)



if __name__ == "__main__":
    le_client = openai.AsyncOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE")
    )
    
    le_model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

    fichier_texte = "textes/metier.txt"

    with open(fichier_texte, "r", encoding="utf-8") as f:
        texte = f.read()
        
        mon_mcp = ModelContextProtocol.init_from_texte(texte, le_client, le_model)
           
        user_request = """Résume ce document en exactement un paragraphe de 4-5 phrases maximum (150 mots max). 
    Le résumé doit être narratif et fluide, pas une liste d'événements. 
    Concentre-toi sur l'intrigue principale et les enjeux centraux."""
    
        response = mon_mcp.process_message(user_request)
        print(response)






