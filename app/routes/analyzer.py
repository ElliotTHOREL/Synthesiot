from app.services.analyzer import quickly_summarize_file, quickly_summarize_text, ask_file, ask_text


from fastapi import APIRouter, Body
from pydantic import BaseModel

router = APIRouter()

# Schemas pour les requêtes avec plusieurs paramètres
class FileAskRequest(BaseModel):
    id_fichier: int
    user_request: str

class TextAskRequest(BaseModel):
    texte: str
    user_request: str

class TextRequest(BaseModel):
    texte: str

# Import ou définis ici tes fonctions métier
# quickly_summarize_file(id_fichier: int)
# ask_file(id_fichier: int, user_request: str)
# quickly_summarize_text(texte: str)
# ask_text(texte: str, user_request: str)

@router.post("/quickly_summarize_file")
async def quickly_summarize_file_endpoint(id_fichier: int = Body(...)):
    return await quickly_summarize_file(id_fichier)

@router.post("/ask_file")
async def ask_file_endpoint(req: FileAskRequest):
    return await ask_file(req.id_fichier, req.user_request)

@router.post("/quickly_summarize_text")
async def quickly_summarize_text_endpoint(req: TextRequest):
    return await quickly_summarize_text(req.texte)

@router.post("/ask_text")
async def ask_text_endpoint(req: TextAskRequest):
    return await ask_text(req.texte, req.user_request)