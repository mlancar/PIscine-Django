import sys
import requests
from bs4 import BeautifulSoup

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

def find_first_p(content_div):

    for p in content_div.find_all('p'):
        parent = p.parent
        if p.find_parent(class_=["mw-content-ltr", "mw-parser-output"]):
            if p.find('a', href=lambda href: href and '/wiki/' in href):
                # print(p)
                return p

def get_link(title):
    
    url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}" #wikipedia met des espaces mais le liens c'est avec des underscores
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')

    content_div = soup.find('div', {'class': 'mw-content-ltr mw-parser-output'}) #toutes les div de wiki contenant le premier paraggraphe s'appelle comme ca
    if content_div == None:
        return None

    first_paragraphe = find_first_p(content_div)

    if first_paragraphe == None:
        return None
    link = first_paragraphe.find('a',  href=lambda href: href and '/wiki/' in href and '/wiki/Help' not in href and "/wiki/File:" not in href)

    if link == None:
        return None

    new_title = link["title"].split(":")[-1]

    return new_title

def find_philosophy(title, road_to_philosophy):

    print(BLUE + title + RESET)

    road_to_philosophy.append(title)
    title = get_link(title)

    if title == None:
        print(RED + "It leads to a dead end !" + RESET, file=sys.stderr)
        sys.exit(1)

    if title in road_to_philosophy:
        print(RED + "It leads to an infinite loop !" + RESET, file=sys.stderr)
        sys.exit(1)

    if title != "Philosophy":
        find_philosophy(title, road_to_philosophy)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: one argument required", file=sys.stderr)
        sys.exit(1)
    road_to_philosophy = []
    i = 0
    find_philosophy(sys.argv[1], road_to_philosophy)

    print(f"{GREEN}{len(road_to_philosophy)} roads from {GREEN}{road_to_philosophy[0]} to philosophy !" + RESET)
