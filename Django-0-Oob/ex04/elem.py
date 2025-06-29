#!/usr/bin/python3

class Text(str):

    def __str__(self):

        text = super().__str__()
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('"', '&quot;')
        text = text.replace('\n', '\n<br />\n')
        return text

class Elem:

    class ValidationError(Exception):
        def __init__(self):
            super().__init__("Error")

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):

        self.tag = tag
        self.tag_type = tag_type

        if attr is not None:
            if not isinstance(attr, dict):
                raise TypeError(f"attr doit être un dictionnaire, pas {type(attr).__name__}")
            self.attr = attr
        else:
            self.attr = {}
        if content is None: 
            self.content = []
        elif self.check_type(content):
            if isinstance(content, list):
                self.content = content
            else: #sinon on cree une list
                self.content = [content]
        else:
            raise Elem.ValidationError

    def __str__(self):

        result = ''
        if self.tag_type == 'double':
            #[...]
            result += '<' + self.tag + self.__make_attr() + '>' + self.__make_content() + '</' + self.tag + '>'
        elif self.tag_type == 'simple':
            #[...]
            result += '<' + self.tag + self.__make_attr() + ' />'
        return result

    def __make_attr(self):

        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):

        if len(self.content) == 0:
            return ''
        result = ""
        for i, elem in enumerate(self.content):
            text = "  " + str(elem).replace('\n', '\n  ')
            if text.strip() == "":
                continue
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

        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

