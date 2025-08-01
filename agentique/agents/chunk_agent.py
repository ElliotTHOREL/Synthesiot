from agentique.agents.base_agent import BaseAgent
from agentique.banque_de_prompts import PROMPT_SYSTEM_CHUNK_AGENT as PROMPT_SYSTEM
from agentique.historique_message import Message, MessageRole
import openai

class ChunkAgent(BaseAgent):
    def __init__(self, texte_du_chunk:str, openai_client: openai.AsyncOpenAI, model: str = "gpt-3.5-turbo"):
        super().__init__(openai_client, model)
        self.system_prompt =  PROMPT_SYSTEM.format(texte_du_chunk=texte_du_chunk)

    async def process_message(self, user_message: str) -> str:
        self.historic.add_message(Message(role=MessageRole.USER, content=user_message))
        
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Ajout de l'historique récent
        recent_messages = self.historic.get_recent_messages(5)
        for msg in recent_messages:
            messages.append({
                "role": msg.role.value,
                "content": msg.content
            })
        
        response = await self.call_openai(messages)

        self.historic.add_message(Message(role=MessageRole.ASSISTANT, content=response))
        return response


