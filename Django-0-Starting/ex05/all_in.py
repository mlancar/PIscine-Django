import sys

def find_city(state, states_dic, cities_dic):

    for key, value in states_dic.items():
        if key.lower() == state.lower():
            to_find = value
            for key, value in cities_dic.items():
                if key == to_find:
                    to_find = value
                    print(to_find,"is the capital of", state)
                    return 1
    return 0

def find_state(city, states_dic, cities_dic):

    for key, value in cities_dic.items():
        if value.lower() == city.lower():
            to_find = key
            for key, value in states_dic.items():
                if value == to_find:
                    to_find = key
                    print(city,"is the capital of", to_find)
                    return 1
    else:
        return 0

def where_is_it(arg):
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

    arg_list = [item.strip() for item in arg.split(",") if item.strip()]

    for to_find in arg_list:
        if find_city(to_find, states, capital_cities) == 0:
            if find_state(to_find, states, capital_cities) == 0:
                print(to_find, " is neither a capital city nor a state")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        where_is_it(arg)
