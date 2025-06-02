import elem


class Html(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="html", attr={}, content=content, tag_type='double')

class Head(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="head", attr={}, content=content, tag_type='double')

class Body(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="body", attr={}, content=content, tag_type='double')

class Title(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="title", attr={}, content=content, tag_type='double')

class Meta(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="meta", attr={}, content=content, tag_type='simple')

class Img(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="img", attr={}, content=content, tag_type='simple')

class Table(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="table", attr={}, content=content, tag_type='double')

class Th(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="th", attr={}, content=content, tag_type='double')

class Tr(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="tr", attr={}, content=content, tag_type='double')

class Td(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="td", attr={}, content=content, tag_type='double')

class Ul(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="ul", attr={}, content=content, tag_type='double')

class Ol(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="ol", attr={}, content=content, tag_type='double')

class Li(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="li", attr={}, content=content, tag_type='double')

class H1(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="h1", attr={}, content=content, tag_type='simple')

class H2(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="h2", attr={}, content=content, tag_type='double')

class P(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="p", attr={}, content=content, tag_type='double')

class Div(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="div", attr={}, content=content, tag_type='double')

class Span(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="span", attr={}, content=content, tag_type='double')

class Hr(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="hr", attr={}, content=content, tag_type='simple')

class Br(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="br", attr={}, content=content, tag_type='simple')

class Text(elem.Elem):
    def __init__(self, content=None):
        super().__init__(tag="text", attr={}, content=content, tag_type='double')

# print( Html( [Head(), Body()] ) )