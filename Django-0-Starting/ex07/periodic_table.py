                    
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
    
    name = ""
    position = ""
    number = ""
    small = ""
    molar = ""
    electron = ""

    html_content = """
        <html lang="en">
            <head>
                <title>Periodic Table</title>
                <meta charset="UTF-8">
            </head>
            <body>
                <link rel="stylesheet" href="periodic_table.css">
                <div id="page-content">
                    <h1>Periodic Table</h1>
                    <div id="table-content">
                        <table>
                                <tr>
                                    {items}
                                </tr>
                        </table>
                    </div>
                </div>
            </body>
        </html>
    """
    items_html = ""
    row_html = ""
    row = []
    last_position = 0

    for element in sorted_data:
        name = element.get("name", "")
        small = element.get("small", "")
        molar = element.get("molar", "")
        electron = element.get("electron", "")

        position = element.get("position", "")

        if (position > last_position)
            row.append([])

        cell += """           <th>
                                        <ul>
                                            <li><strong>name</strong></li>
                                            <li>small</li>
                                            <li>molar</li>
                                            <li>electron</li>
                                        </ul>
                                    </th>
                        """
        last_position = position
        current_row.append(cell)


    final_html = html_content.format(rows=rows_html)

    with open("periodic_table.html", "w") as file:
        file.write(final_html)

if __name__ == "__main__":
    create_html_file()
   