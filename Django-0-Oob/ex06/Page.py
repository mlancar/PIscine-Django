from elements import *
import traceback
from elem import Elem, Text

class Page():

    def __init__(self, root_elem):
        if not isinstance(root_elem, Elem):
            raise TypeError("blabla error")
        self.root = root_elem
    
    def __str__(self):
        if isinstance(self.root, Html):
            return "<!DOCTYPE html>\n" + str(self.root) + "\n"
        else:
            return str(self.root)

    def write_to_file(self):
        with open("page.html", "w") as file:
            file.write(self.__str__())

    def is_valid(self, element, current_path):

        current_elem = element

        match current_elem:
            case Html():
                if len(current_elem.content) != 2:
                    return False
            
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
                elif current_path[-1] not in ("body", "div"):
                    return False

            case Ul():
                if current_path[-1] not in ("body", "div"):
                    return False
                elif not current_elem.content:
                    return False
            
            case Ol():
                if current_path[-1] not in ("body", "div"):
                    return False
                elif not current_elem.content:
                    return False
            case Li():
                if current_path[-1] not in ("ul", "ol"):
                    return False
            
            case Table():
                if current_path[-1] not in ("body", "div"):
                    return False
            
            case H1():
                if current_path[-1] not in ("body", "div"):
                    return False
            
            case H2():
                if current_path[-1] not in ("body", "div"):
                    return False

            case Tr():
                if not current_elem.content:
                    return False
            
            case Td():
                if current_path[-1] != "tr":
                    return False
        
            case P():
                if current_path[-1] != "span":
                    return False
            case Span():
                if current_path[-1] not in ("body", "div"):
                    return False
            
            case Text():
                if (current_path[-1] != "p") and (current_path[-1] != "body") and (current_path[-1] != "title") and (current_path[-1] != "h1") and (current_path[-1] != "h2") and (current_path[-1] != "li") and (current_path[-1] != "th") and (current_path[-1] != "td") and (current_path[-1] != "span") and (current_path[-1] != "div"):
                    return False
                elif ():
                    if "text" in current_path:
                        return False
                    else:
                        current_path.append("text")
                        return True
                else:
                    current_path.append("text")
                    return True

        if current_path:
            match current_path[-1]:
                case "span":
                    if not isinstance(current_elem, Text) and not isinstance(current_elem, P):
                        return False    
                
                case "ul":
                    if not isinstance(current_elem, Li):
                        return False
                
                case "table":
                    if not isinstance(current_elem, Tr):
                        return False
                
                case "tr":
                    if not isinstance(current_elem, Th) and not isinstance(current_elem, Td):
                        return False
                
                case "p":
                    if not isinstance(current_elem, Text):
                        return False
        else:
            if not isinstance(current_elem, Html):
                return False

        if isinstance(current_elem, Text):
            current_path.append("text")
            return True
        else:
            current_path.append(current_elem.tag)

        for i, elem in enumerate(current_elem.content):
            if not self.is_valid(elem, current_path):
                return False
        
        self.write_to_file()
        return True

if __name__ == '__main__':

    page = Page(Html([Head(Title()), Body(Img())]))

    try:
        current_path = []
        is_page_valid = page.is_valid(page.root, current_path)
        print(is_page_valid)

    except Exception as e:
        traceback.print_exc()
        print(e)
