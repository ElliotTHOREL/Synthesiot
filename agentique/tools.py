import re
import json5
from typing import Optional, Dict

def extract_json_list_from_response(response: str) -> list[dict]:
    """
    Extrait une liste de dictionnaires JSON d'une réponse textuelle.
    Utilise json5 pour plus de tolérance.
    """
    # Cherche un bloc qui commence par [ et finit par ]
    pattern = r'\[[\s\S]*?\]'
    matches = re.findall(pattern, response)

    for json_candidate in matches:
        try:
            parsed = json5.loads(json_candidate)
            if isinstance(parsed, list) and all(isinstance(x, dict) for x in parsed):
                return parsed
        except Exception as e:
            continue  # essaie avec le match suivant

    return None

def extract_think_do_block(text: str) -> Optional[Dict[str, str]]:
   # Remplacer les crochets [] entourant du texte par des guillemets doubles, en gérant les retours à la ligne
    # Capture le contenu entre crochets, strip, puis ajoute guillemets autour
    def replacer(match):
        inner = match.group(2).strip().replace('\n', ' ').replace('"', '\\"')
        return f'{match.group(1)}"{inner}"'

    cleaned = re.sub(r'("?(?:think|content)"?\s*:\s*)\[(.*?)\]', replacer, text, flags=re.DOTALL)

    # Ajouter la virgule manquante entre "think" et "do" s’il n’y en a pas
    cleaned = re.sub(r'("think"\s*:\s*".*?")(\s*"do"\s*:)', r'\1,\2', cleaned, flags=re.DOTALL)

    try:
        data = json5.loads(cleaned)
    except Exception as e:
        # Pour debug, tu peux imprimer e et cleaned ici
        return None

    think = data.get("think", "").strip()
    do = data.get("do", {})
    do_type = do.get("type", "").strip().upper()
    result = {
        "think": think,
        "do": do_type
    }
    if do_type == "QUESTION":
        question = do.get("content", "").strip()
        if question:
            result["question"] = question

    return result

if __name__ == "__main__":
    texte_test = """{
  "think": [Les idées principales de la section Résultats ont été fournies. Je vais maintenant extraire les idées principales de la section suivante.]
  "do": {
    "type": "QUESTION",
    "content":  [Quelles sont les idées principales de la section Discussion ?]
  }
}"""
    print(extract_think_do_block(texte_test))
    #OK