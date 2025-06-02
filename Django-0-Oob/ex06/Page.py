import elements
import traceback
from elem import Elem, Text

class Page():

    def __init__(self, root_elem):
        if not isinstance(root_elem, Elem):
            raise TypeError("blabla error")
        self.root = root_elem
    
    def __str__(self):
        return str(self.root)

    def is_valid(self, element, current_path):

        list_elem = ["html", "head", "body", "title", "meta", "img", "table", "th", "tr", "td" , "ul", "ol", "li", "h1", "h2", "p", "div", "span", "hr", "br", "Text"]


        current_elem = element
        # print(element.tag)
        # print(f"index = {index}")

        # print(f"current elem = {current_elem.tag}")
        # print(f"last elem = {last_elem.tag}")
        
        for elem in current_path:
            print(f"current path = {elem}")

        if current_elem.tag not in list_elem:
            return False
        #HTML
        if not current_path:
            if not isinstance(current_elem, elements.Html):
                return False    
        # HEAD
        elif isinstance(current_elem, elements.Head):
            if "head" in current_path:
                return False
        # TITLE
        elif isinstance(current_elem, elements.Title):
            if ((current_path[-1] == "head") and (elements.Title in current_path)):
                return False
            elif "head" not in current_path or "title" in current_path:
                return False
        #BODY
        elif isinstance(current_elem, elements.Body):
            if ("head" not in current_path) or ("title" not in current_path):
                return False
            elif "body" in current_path:
                return False
        #DIV
        elif isinstance(current_elem, elements.Div):
            if "body" not in current_path:
                return False
        #TEXT
        elif isinstance(current_elem, elements.Text):
            if ((current_path[-1] == "title") or (current_path[-1] == "h1") or (current_path[-1] == "h2") or (current_path[-1] == "li") (current_path[-1] == "th") or (current_path[-1] == "td")):
                if "text" in current_path:
                    return False
            # elif (current_path[-1] == "span")
            #     return False
        
        #Ul/Ol/Li
        elif (current_path[-1] == ("ul" or "ol")) and not isinstance(current_elem, elements.Li):
            return False
        #TABLE
        elif current_path[-1] == "table" and not isinstance(current_elem, elements.Tr):
            return False
        #TR
        elif current_path[-1] == "tr" and (not isinstance(current_elem, elements.Th) and not isinstance(current_elem, elements.Td)):
                return False
        
        # elif 
        #ADD ELEMENT
        current_path.append(current_elem.tag)
        # print("\n")
        #RECURSSIOM
        for i, elem in enumerate(current_elem.content):
            if not self.is_valid(elem, current_path):
                return False
        return True

page = Page(elements.Html([elements.Head([elements.Title()]), elements.Body(elements.Div([elements.P([elements.Text()])]))]))

print(page, "\n")
try:
    index = 0
    current_path = []
    result = page.is_valid(page.root, current_path)
    print(f"result: {result}")
except Exception as e:
    print(e)

# print(result)
# printf(Page(Html))
