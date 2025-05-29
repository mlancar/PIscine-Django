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

    def is_valid(self, element):

        list_elem = ["html", "head", "body", "title", "meta", "img", "table", "th", "tr", "td" , "ul", "ol", "li", "h1", "h2", "p", "div", "span", "hr", "br", "Text"]
        # print(self.root)
        previous_elem = []
        index = 0
        # html_rendered = str(self.root)
        # for line in html_rendered.splitlines():
        current_elem = element
        print(element.tag)
        # for elem in current_elem.content:
            
        #     print("elem is:",  elem.tag)
        #     current_elem = elem.content
        #     print("apres elem is:",  current_elem.)
        for i in range(len(current_elem.content)):
            # print("coucou")
            # print(len(current_elem.content))
            # print('1 mais pas la size!',current_elem.content[0])
            # print('2 mais pas la size!',current_elem.content[1])

            self.is_valid(current_elem.content[i])
            print("apres")
            # for children in current_elem:
            #     print(f"children: {children}")

            # for elem2 in current_elem:

            # print("ici:", len(current_elem))
            # if index == 0 and not isinstance(self.root, elements.Html):
            #     raise TypeError("Wrong type:", self.root.tag)
            # elif index == 0 and isinstance(self.root, elements.Html):
            #     print("isok")
            #     index += 1
            #     previous_elem.append(self.root.tag)
            # print("index:", index)
            # print("previous elem = ", previous_elem[-1])
            # print("tag = ", elem.tag)
            # if elem.tag == "head" and index == 1 and previous_elem[-1] == "html":
            #     print("isok2")

            # elif elem.tag == "title" and previous_elem[-1] == "head":
            #     print("isok3")
            # index += 1
            # previous_elem.append(elem.tag)
            # print("\n")

        return True

        
# if __name__ == '__main__':
# print(str(Elem(tag='body', attr={}, content=Elem(), tag_type='double')))

# print(str(Elem(content=(content=Elem(content=Elem())))))

page = Page(elements.Html([elements.Head([elements.Title([elements.Div()])]), elements.Body([elements.Div(), elements.Div()])]))
# print(page, "\n")
try:
    result = page.is_valid(page.root)
except Exception as e:
    print(e)

# print(result)
# printf(Page(Html))