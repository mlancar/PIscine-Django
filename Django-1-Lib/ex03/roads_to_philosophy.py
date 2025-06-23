import sys
import requests
from bs4 import BeautifulSoup

def find_first_p(content_div):
    #check pas help dans le lien/IPA
    #test avec urine
    for p in content_div.find_all('p'):
        parent = p.parent
        if parent.name == "div" and parent.get("class") == ['mw-content-ltr', 'mw-parser-output'] and p.get_text(strip=True):
            return p

def get_link(title):
    
    url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}" #wikipedia met des espaces mais le liens c'est avec des underscores
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    content_div = soup.find('div', {'class': 'mw-content-ltr mw-parser-output'}) #toutes les div de wiki contenant le premier paraggraphe s'appelle comme ca


    first_paragraphe = find_first_p(content_div)
    
    # print(first_paragraphe)
    #FAIRE UNE FONCTION PEUTETRE POUR TROUVER LE LIEN
    link = first_paragraphe.find('a',  href=lambda href: href and '/wiki/' in href and '/wiki/Help' not in href and "/wiki/File:" not in href)
    # print("link = ", link)
    if link == None:
        return None
    new_title = link["title"].split(":")[-1]

    return new_title

def find_philosophy(title, road_to_philosophy):

    # for title in road_to_philosophy:
    #     print("title = ", title)

    print(title)
    road_to_philosophy.append(title)
    title = get_link(title)
    if title == None:
        print("It leads to a dead end !", file=sys.stderr)
        sys.exit(1)

    if title in road_to_philosophy:
        print("It leads to an infinite loop !", file=sys.stderr)
        sys.exit(1)

    if title != "Philosophy":
        find_philosophy(title, road_to_philosophy)
    

    print(f"{len(road_to_philosophy)} roads from {road_to_philosophy[0]} to philosophy !")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: one argument required", file=sys.stderr)
        sys.exit(1)
    road_to_philosophy = []
    find_philosophy(sys.argv[1], road_to_philosophy)
