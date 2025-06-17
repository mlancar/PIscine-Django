import sys
import requests


def get_title(request_name):
    # print(f"request: {request_name}")
    API_URL = "https://fr.wikipedia.org/w/api.php"
    title = request_name


    content_params = {
        "action": "query",
        "list": "search",
        "format": "json",
         "srsearch": title,
    }

    response = requests.get(API_URL, params=content_params)
    response.raise_for_status()
    data = response.json()

    results = data["query"]["search"]
    if not results:
        print("Aucun résultat trouvé.")
        exit()
    title = results[0]["title"]

def get_article(title):

    extract_params = {
    "action": "query",
    "prop": "extracts",
    "titles": title,
    "format": "json",
    "explaintext": 1,
    "redirects": 1
    }

    res2 = requests.get(API_URL, params=extract_params)
    res2.raise_for_status()
    data2 = res2.json()

    page = next(iter(data2["query"]["pages"].values()))
    extract = page.get("extract", "[Aucun contenu trouvé]")

    print(extract)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Too many arguments")
    title = get_title(sys.argv[1])
