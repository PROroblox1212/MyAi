import requests

def search_web(query: str) -> str:
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    resp = requests.get(url).json()
    if "AbstractText" in resp and resp["AbstractText"]:
        return resp["AbstractText"]
    elif "RelatedTopics" in resp and len(resp["RelatedTopics"]) > 0:
        return resp["RelatedTopics"][0].get("Text", "Pas trouvé")
    return "Aucune information trouvée"
