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

    def is_valid(self):

        for elem in self.root.content:
            print("elem is:",  elem)
            if isinstance(elem, elements.Html):
                print("oui")
            else:
                print("non")
        return True

        
# if __name__ == '__main__':
# print(str(Elem(tag='body', attr={}, content=Elem(), tag_type='double')))

# print(str(Elem(content=(content=Elem(content=Elem())))))

page = Page(elements.Html([elements.Head(), elements.Body()]))
print(page)
result = page.is_valid()
print(result)
# printf(Page(Html))