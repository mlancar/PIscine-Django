from elements import *
from elem import *
import pytest

def test_elem_basics():
    # Default behaviour :
    assert str(Html()) == '<html></html>'
    assert str(Head()) == '<head></head>'
    assert str(Body()) == '<body></body>'
    assert str(Meta()) == '<meta />'
    assert str(Title()) == '<title></title>'
    assert str(Img()) == '<img />'
    assert str(Table()) == '<table></table>'
    assert str(Td()) == '<td></td>'
    assert str(Tr()) == '<tr></tr>'
    assert str(Th()) == '<th></th>'
    assert str(Ul()) == '<ul></ul>'
    assert str(Ol()) == '<ol></ol>'
    assert str(Li()) == '<li></li>'
    assert str(H1()) == '<h1></h1>'
    assert str(H2()) == '<h2></h2>'
    assert str(P()) == '<p></p>'
    assert str(Div()) == '<div></div>'
    assert str(Span()) == '<span></span>'
    assert str(Hr()) == '<hr />'
    assert str(Br()) == '<br />'

def test_embedding():

    assert str(Html(Head())) == '<html>\n  <head></head>\n</html>'
    assert str(Body(Div())) == '<body>\n  <div></div>\n</body>'
    assert str(Head(Meta())) == '<head>\n  <meta />\n</head>'
    assert str(Div(Img())) == '<div>\n  <img />\n</div>'
    assert str(Table([Tr(Th()), Tr(Td())])) == '<table>\n  <tr>\n    <th></th>\n  </tr>\n  <tr>\n    <td></td>\n  </tr>\n</table>'
    assert str(Div([Ul(Li()), Ol(Li())])) == '<div>\n  <ul>\n    <li></li>\n  </ul>\n  <ol>\n    <li></li>\n  </ol>\n</div>'
    assert str(Div(H1())) == '<div>\n  <h1></h1>\n</div>'
    assert str(Div(Span(P()))) == '<div>\n  <span>\n    <p></p>\n  </span>\n</div>'
    assert str((Title(Text("Hello")))) == '<title>\n  Hello\n</title>'
    assert str(Img(attr={"src": "http://i.imgur.com/pfp3T.jpg"}))

def test_subject():
    
    assert str(Html([Head(Title(Text("Hello ground!"))), Body([H1(Text("Oh no, not again!")), Img(attr={"src": "http://i.imgur.com/pfp3T.jpg"})])])) ==\
        '<html>\n  <head>\n    <title>\n      Hello ground!\n    </title>\n  </head>\n  <body>\n    <h1>\n      Oh no, not again!\n    </h1>\n    <img src="http://i.imgur.com/pfp3T.jpg" />\n  </body>\n</html>'
