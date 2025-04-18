import sys

def find_state(city):

    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CD": "Denver"
    }

    for key, value in capital_cities.items():
        if value == city:
            to_find = key
            for key, value in states.items():
                if value == to_find:
                    to_find = key
                    print(to_find)
                    return
    else:
        print("Unknown city")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        city = sys.argv[1]
        find_state(city)
