import sys
import requests
import dewiki

def get_title(api_url, title_search):

    content_params = {
        "action": "query",
        "list": "search", #liste des resulats
        "format": "json",
        "srsearch": title_search, #terme cherche
    }

    response = requests.get(api_url, params=content_params)
    response.raise_for_status()
    data = response.json()
    results = data["query"]["search"]
    
    if not results:
        print("Aucun résultat trouvé.")
        exit()
    title = results[0]["title"] #prend le titre du premier resultat

    return title

def get_article(api_url, title):

    params = {
        "action": "query", #type de requete
        "prop": "revisions", #dermiere version de l'article
        "rvprop": "content", #donne juste le contenu, pas date ou auteur
        "rvslots": "main", #recuperer le contenu principale de la page
        "titles": title, #titre recherche
        "format": "json", # retourne format json
        "formatversion": 2 #version2 format json
    }
   
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    data = response.json()

    if "query" not in data:
        print("Aucune page trouvée ou erreur dans la requête.")
        print("Réponse API :", data)
        exit()
    
    page = data["query"]["pages"][0]
    raw_wikitext = page["revisions"][0]["slots"]["main"]["content"]
    clean_text = dewiki.from_string(raw_wikitext)

    return clean_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Too many arguments")
        
    api_url = "https://fr.wikipedia.org/w/api.php"
    
    title = get_title(api_url, sys.argv[1])

    data = get_article(api_url, title)
    formated_title = title.replace(" ", "_")
    file_name = title + ".wiki"
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(data)
    except Exception as e:
        print(e)