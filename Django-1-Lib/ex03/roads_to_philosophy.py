import sys
import requests
from bs4 import BeautifulSoup

# def get_title(api_url, title_search):

#     content_params = {
#         "action": "query",
#         "list": "search", #liste des resulats
#         "format": "json",
#         "srsearch": title_search, #terme cherche
#     }

#     response = requests.get(api_url, params=content_params)
#     response.raise_for_status()
#     data = response.json()
#     results = data["query"]["search"]
    
#     if not results:
#         print("Aucun résultat trouvé.")
#         sys.exit(1)
#     title = results[0]["title"] #prend le titre du premier resultat

#     return title

# def find_first_paragraphe(div):
#     for element in div.children:
#         element.find('p')
#             print(f"element = {element}")
#             return element
#         # elif "homonymie" not in texte:
#         #     return element

def get_link(title):
    
    url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}" #wikipedia met des espaces mais le liens c'est avec des underscores
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    content_div = soup.find('div', {'id': 'mw-content-text'}) #toutes les div de wiki contenant le premier paraggraphe s'appelle comme ca

    # first_paragraphe = find_first_paragraphe(content_div)
    
    # print("first_paragaphre: ", first_paragraphe)

    link = content_div.find_all('a',  href=lambda href: href and href.startswith('https') and '/wiki/' in href)
    
    #check que le parent de <a> est l'id de la premiere div

    print(link[0]["href"])
    new_title = link[0]["title"].split(":")[-1]
    if new_title == title:
        print("test")
    return new_title

def get_title(link):
    print(link)

def find_philosophy(title, road_to_philosophy):

    
    
    if title in road_to_philosophy:
        print("It leads to an infinite loop !", file=sys.stderr)
        sys.exit(1)
    # elif:
    #     print("It leads to a dead end !", file=sys.stderr)
        #sys.exit(1)

    if title != "https://en.wikipedia.org/wiki/Philosophy":
        title = get_link(title)
        print("new title = ", title)
        #que faire si link existe pas
        print(title)
        road_to_philosophy.append(title)
        find_philosophy(title, road_to_philosophy)

    print(f"{len(road_to_philosophy)} roads from {road_to_philosophy[0]} to philosophy !")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: one argument required", file=sys.stderr)
        sys.exit(1)
    road_to_philosophy = []
    find_philosophy(sys.argv[1], road_to_philosophy)
