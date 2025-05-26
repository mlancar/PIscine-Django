#!/usr/bin/python3
from abc import ABC

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        text = super().__str__()
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('"', '&quot;')
        text = text.replace('\n', '\n<br />\n')
        return text

# class Elem(ABC):

class Elem():
    """
    Elem will permit us to represent our HTML elements.
    """

    class ValidationError(Exception):
        def __init__(self):
            super().__init__("Error")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        #[...]
        #attr = dictionnaire
        #content = list
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type

        if content is None: 
            self.content = [] #si on fait pas ca ca fait que content = [none] donc on fait une list vide []
        elif self.check_type(content): #check si content est un contenu valide, instance html ou text ou list d'elenetb Elem ou Text
            if isinstance(content, list): #check si c'est une list
                self.content = content
            else: #sinon on cree une list
                self.content = [content]
        else:
            raise Elem.ValidationError

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = ''
        if self.tag_type == 'double':
            #[...]
            result += '<' + self.tag + self.__make_attr() + '>' + self.__make_content() + '</' + self.tag + '>'
        elif self.tag_type == 'simple':
            #[...]
            result += '<' + self.tag + self.__make_attr() + '/>'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        print(result)
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if len(self.content) == 0:
            return ''
        result = ""
        for i, elem in enumerate(self.content):
            
            text = "  " + str(elem).replace('\n', '\n  ')
            if text.strip() == "":
                continue
            # print(str(elem))
            if i == len(self.content) - 1:
                text += '\n'
            result += "\n" + text
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    [...]
