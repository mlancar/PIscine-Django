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

    def is_valid(self, element, last_elem, index):

        list_elem = ["html", "head", "body", "title", "meta", "img", "table", "th", "tr", "td" , "ul", "ol", "li", "h1", "h2", "p", "div", "span", "hr", "br", "Text"]


        current_elem = element
        print(element.tag)
        print(f"index = {index}")

        print(f"current elem = {current_elem.tag}")
        print(f"last elem = {last_elem.tag}")
        

        if current_elem.tag not in list_elem:
            return False
        if index == 0 and not isinstance(current_elem, elements.Html):
            print("par la")
            return False
        elif index == 1 and (isinstance(last_elem, elements.Html)) and (not isinstance(current_elem, elements.Head)):
            print("la")
            return False
        elif (isinstance(last_elem, elements.Head)) and (not isinstance(current_elem, elements.Title)):
            print("ici")
            return False
        elif index == 2 and (isinstance(current_elem, elements.Body) and (not isinstance(last_elem, elements.Html))):
            print("cc")
            return False
        
        if current_elem.tag in list_elem:
            if isinstance(current_elem, elements.Html):
                list_elem.remove("html")
            elif isinstance(current_elem, elements.Head):
                list_elem.remove("head")
            elif isinstance(current_elem, elements.Body):
                list_elem.remove("body")
            elif isinstance(current_elem, elements.Title):
                list_elem.remove("title")

        print("\n")

        for i, elem in enumerate(current_elem.content):
            if not self.is_valid(elem, current_elem, index + 1):
                return False
 
        return True


page = Page(elements.Html([elements.Head([elements.Title()]), elements.Body([elements.Div(), elements.Div()])]))
print(page, "\n")
try:
    index = 0
    result = page.is_valid(page.root, page.root, index)
except Exception as e:
    print(e)

# print(result)
# printf(Page(Html))
