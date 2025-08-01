import re
import json5

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