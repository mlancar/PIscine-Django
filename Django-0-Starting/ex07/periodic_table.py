import itertools                    

def get_first_key_value(d):
    return int(d["number"])

def get_type(element):

    number = element.get('number')
    number = int(number)

    if number in {1, 6, 7, 8, 15, 16, 34}:
        return "non-metal"
    elif number in {2, 10, 18, 36, 54, 86}:
        return "noble-gas"
    elif number in {3, 11, 19, 37, 55, 87}:
        return "alkaline-metal"
    elif number in {4, 12, 20, 38, 56, 88}:
        return "alkali-earth-metal"
    elif number in {5, 14, 32, 33, 51, 52, 85}:
        return "metalloid"
    elif number in {9, 17, 35, 53, 85}:
        return "halogen"
    elif number in {13, 30, 31, 48, 49, 50, 80, 81, 82, 83, 84}:
        return "post-transition-metal"
    #pas faire avec itertools
    elif number in itertools.chain(range(21, 30), range(39, 48), range(71, 80), range(103, 109)) or number == 112:
        return "transition-metal"
    else:
        return "non-classified"


def parse_data():

    with open("periodic_table.txt", "r") as file:
        list_file = file.read()

    list_element = []
    for line in list_file.strip().split("\n"):
        dictionary = {}
        element = line.split("=")
        dictionary["name"] = element[0]
        pairs = element[1].split(",")
        for pair in pairs:
            key, value = pair.strip().split(":")
            dictionary[key.strip()] = value.strip()
        list_element.append(dictionary)
    
    sorted_data = sorted(list_element, key=get_first_key_value)
    return sorted_data

def create_html_content(sorted_data):

    # Génération HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Tableau Périodique</title>
       
    </head>
    <body>
        <link rel="stylesheet" href="periodic_table.css">
        <div id="page-content">
            <h1 id="title">Tableau Périodique des Éléments</h1>
            <table>
    """
    rows = 7
    columns = 18
    index = 0

    for row in range(rows):
        html_content += "  <tr>\n"
        for col in range(columns):
            if index < len(sorted_data):
                element = sorted_data[index]
                name = element.get('name')
                number = element.get('number')
                small = element.get('small')
                molar = element.get('molar')
                electron = element.get('electron')

                if (row == 0 and col == 2) or ((row == 1 or row == 2) and col == 8) or (row == 5 and col == 17):
                    break
                if row == 0 and col == 1:
                    html_content += f"""    <td class="no-border" colspan="16"></td>\n"""
                elif (row == 1 or row == 2) and col == 2:
                    html_content += f"""    <td class="no-border" colspan="10"></td>\n"""
                elif (row == 5 or row == 6) and col == 2:
                    html_content += f"""    <td class="no-border"></td>\n"""
                index += 1
                element_type = get_type(element)
                html_content += f"""    <td class="{element_type}">
                                                <h4 class="name">{name}</h4>
                                                <ul>
                                                    <li class="number">{number}</li>
                                                    <li class="small">{small}</li>
                                                    <li class="molar">{molar}</li>
                                                </ul>
                                    </td>\n"""
        html_content += "  </tr>\n"
    html_content += "</table>\n</div>\n</body>\n</html>"
    return html_content
    

if __name__ == "__main__":
    sorted_data = parse_data()
    html_content = create_html_content(sorted_data)
    with open("periodic_table.html", "w") as file:
        file.write(html_content)