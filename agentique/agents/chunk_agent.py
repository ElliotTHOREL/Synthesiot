from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompt.chunk_agent import PROMPT_SYSTEM_GENERAL
from agentique.banque_de_prompt.chunk_agent import PROMPT_SYSTEM_PREMIER
from agentique.banque_de_prompt.chunk_agent import PROMPT_SYSTEM_CONTEXTUALISE
from agentique.banque_de_prompt.chunk_agent import PROMPT_USER_CONTEXTE
from agentique.banque_de_prompt.chunk_agent import PROMPT_USER_SUMMARY
from agentique.historique_message import Message, ConversationHistory
import openai

class ChunkAgent(BaseAgent):

    #2 types d'initialisation :
    #   1. from scratch : code ci-dessous (init_from_texte + async_init)
    #   2. from bdd : code dans le fichier app/services/database/read.py (get_mcp_from_bdd)

    def __init__(self, context:str, is_premier_chunk:bool, texte_du_chunk:str, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.context = context
        self.is_premier_chunk = is_premier_chunk
        self.texte_du_chunk = texte_du_chunk
        self.historic = None #selon l'initialisation
        self.system_prompt =  None #selon l'initialisation
        self.summary = None #selon l'initialisation

    #Initialisation from scratch
    @classmethod
    def init_from_texte(cls, context:str, is_premier_chunk:bool, texte_du_chunk:str, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        chunk_agent = cls(context, is_premier_chunk, texte_du_chunk, openai_client, model)
        chunk_agent.historic = ConversationHistory()
        chunk_agent.system_prompt =  chunk_agent.get_system_prompt()
        return chunk_agent

    async def async_init(self):
        self.summary = await self.get_summary()




    def get_system_prompt(self):
        if self.is_premier_chunk:
            info_context = PROMPT_SYSTEM_PREMIER
        else:
            info_context = PROMPT_SYSTEM_CONTEXTUALISE.format(context=self.context)

        return PROMPT_SYSTEM_GENERAL.format(info_context=info_context, texte_du_chunk=self.texte_du_chunk)

    async def process_message(self, user_message: str) -> str:
        self.historic.add_message(Message(auteur="user", content=user_message))
        
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Ajout de l'historique récent
        recent_messages = self.historic.get_recent_messages(5)
        for msg in recent_messages:
            messages.append({
                "role": msg.auteur,
                "content": msg.content
            })
        
        response = await self.call_openai(messages)

        self.historic.add_message(Message(auteur="assistant", content=response))
        return response

    async def generate_next_context(self):
        user_prompt = PROMPT_USER_CONTEXTE
        response = await self.process_message(user_prompt)
        return response

    async def get_summary(self):
        user_prompt = PROMPT_USER_SUMMARY
        response = await self.process_message(user_prompt)
        return response






