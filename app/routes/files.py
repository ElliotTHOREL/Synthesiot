from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import Optional

from app.database.update import add_file_in_bdd
from app.services.files import get_files

router = APIRouter()

@router.get("/get_files/")
async def get_files_endpoint():
    return await get_files()


@router.post("/import_file/")
async def import_file_endpoint(file: UploadFile = File(...), name: Optional[str] = None):
    # Récupérer le contenu du fichier en mémoire
    try:
        contenu = await file.read()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors de la lecture du fichier: {e}")

    # Nom du fichier, si pas donné on prend celui de l'upload
    filename = name or file.filename.split(".")[0]

    # Convertir bytes en texte, ici on suppose utf-8
    try:
        texte = contenu.decode("utf-8")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur de décodage utf-8: {e}")

    # Ici tu appelles ta fonction métier qui enregistre le texte
    await add_file_in_bdd(filename, texte)

    return {"status": "success", "filename": filename}


