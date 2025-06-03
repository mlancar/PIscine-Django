from elements import *
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

        current_elem = element

        # for elem in current_path:
        #     print(f"current path = {elem}")
        
        match current_elem:
            case Html():
                print("html")
            
            case Head():
                if "head" in current_path:
                    return False
            
            case Title():
                if ((current_path[-1] == "head") and (Title in current_path)):
                    return False
                elif "head" not in current_path or "title" in current_path:
                    return False
            
            case Body():
                if ("head" not in current_path) or ("title" not in current_path):
                    return False
                elif "body" in current_path:
                    return False
            
            case Div():
                if "body" not in current_path:
                    return False
            
            case P():
                print("P")
            
            case Text():
                if (current_path[-1] == "p") and (not isinstance(current_elem, Text)):
                    return False
                if ((current_path[-1] == "title") or (current_path[-1] == "h1") or (current_path[-1] == "h2") or (current_path[-1] == "li") or (current_path[-1] == "th") or (current_path[-1] == "td")):
                    if "text" in current_path:
                        return False
            case Li():
                if current_path[-1] != ("ul" or "ol"):
                    return False

        if current_path:
            match current_path[-1]:
                case "ul" | "ol":
                    if not isinstance(current_elem, Li):
                        return False
                case "table":
                    if not isinstance(current_elem, Tr):
                        return False
                case "tr":
                    if not isinstance(current_elem, Th and not isinstance(current_elem, Td)):
                        return False
                case

        else:
            if not isinstance(current_elem, Html):
                return False

        print(f"DEBUG: current_elem = {current_elem}, type = {type(current_elem)}")

        current_path.append(current_elem.tag)

        for i, elem in enumerate(current_elem.content):
            if not self.is_valid(elem, current_path):
                return False
        return True

# page = Page(Html([Head(Title()), Body(Text())]))

# print(page, "\n")
# try:
#     index = 0
#     current_path = []
#     result = page.is_valid(page.root, current_path)
#     print(f"result: {result}")
# except Exception as e:
#     traceback.print_exc()
#     print(e)

# print(result)
# printf(Page(Html))
