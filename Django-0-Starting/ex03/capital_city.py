import sys

def find_city(state):

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

    if state in states:
        to_find = states[state]
        if to_find in capital_cities:
            print(capital_cities[to_find])
    else:
        print("Unknown state")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        state = sys.argv[1]
        find_city(state)
