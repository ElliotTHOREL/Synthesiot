from pydantic import BaseModel, Field
from typing import List



class Message(BaseModel):
    """Modèle pour un message de conversation"""
    auteur: str
    content: str


class ConversationHistory(BaseModel):
    """Historique complet d'une conversation"""
    messages: List[Message] = Field(default_factory=list)

    def add_message(self, message: Message):
        self.messages.append(message)
    
    def get_recent_messages(self, limit: int = 10) -> List[Message]:
        """Récupère les N derniers messages"""
        return self.messages[-limit:] if len(self.messages) > limit else self.messages
    