                    
def get_first_key_value(d):
    return int(d["position"])

def create_html_file():

    with open("periodic_table.txt", "r") as file:
        list_file = file.read()
    # line = list_file.split()

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
    
    # print(list_element)
    sorted_data = sorted(list_element, key=get_first_key_value)
                
    # print(sorted_data)


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
        <h1 style="text-align:center;">Tableau Périodique des Éléments</h1>
        <table>
        
    """
    # data = [f"Case {i}" for i in range(126)]
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
                
                if (row == 0 and col == 2) or ((row == 1 or row == 2) and col == 8):
                    break
                if row == 0 and col == 1:
                    print(row, col)
                    html_content += f"""    <td colspan="16"</td>\n"""
                elif (row == 1 or row == 2) and col == 2:
                    print("ici", row, col)
                    html_content += f"""    <td colspan="10"></td>\n"""
                else:
                    index += 1

                html_content += f"""    <td>
                                            
                                                <h4 id="name">{name}</h4>
                                                <ul>
                                                    <li id="number">{number}</li>
                                                    <li id="small">{small}</li>
                                                    <li id="molar">{molar}</li>
                                                </ul>
                                            
                                    </td>\n"""

        html_content += "  </tr>\n"

    html_content += "</table>\n</body>\n</html>"




    with open("periodic_table.html", "w") as file:
        file.write(html_content)

if __name__ == "__main__":
    create_html_file()
   