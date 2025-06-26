import elem

class Html(elem.Elem):
    def __init__(self, content=None, attr=None, ):
        if attr is None:
            attr = {}
        super().__init__(tag="html", attr=attr, content=content, tag_type='double')

class Head(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="head", attr=attr, content=content, tag_type='double')

class Body(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="body", attr=attr, content=content, tag_type='double')

class Title(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="title", attr=attr, content=content, tag_type='double')

class Meta(elem.Elem):
    def __init__(self, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="meta", attr=attr, tag_type='simple')

class Img(elem.Elem):
    def __init__(self, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="img", attr=attr, tag_type='simple')

class Table(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="table", attr=attr, content=content, tag_type='double')

class Th(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="th", attr=attr, content=content, tag_type='double')

class Tr(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="tr", attr=attr, content=content, tag_type='double')

class Td(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="td", attr=attr, content=content, tag_type='double')

class Ul(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="ul", attr=attr, content=content, tag_type='double')

class Ol(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="ol", attr=attr, content=content, tag_type='double')

class Li(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="li", attr=attr, content=content, tag_type='double')

class H1(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="h1", attr=attr, content=content, tag_type='double')

class H2(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="h2", attr=attr, content=content, tag_type='double')

class P(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="p", attr=attr, content=content, tag_type='double')

class Div(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="div", attr=attr, content=content, tag_type='double')

class Span(elem.Elem):
    def __init__(self, content=None, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="span", attr=attr, content=content, tag_type='double')

class Hr(elem.Elem):
    def __init__(self, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="hr", attr=attr, tag_type='simple')

class Br(elem.Elem):
    def __init__(self, attr=None):
        if attr is None:
            attr = {}
        super().__init__(tag="br", attr=attr, tag_type='simple')