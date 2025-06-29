from Page import Page
from elements import *
import traceback
from elem import Elem, Text
import pytest

def test_valid_html_node():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body()]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == True

def test_root_invalid():
    is_page_valid = Page(Body())
    current_path = []
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_html_empty():
    is_page_valid = Page(Html())
    current_path = []
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_no_head():
    current_path = []
    is_page_valid = Page(Html([Body()]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_double_head():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Head()]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_invalid_head():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Head())]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_no_title():
    current_path = []
    is_page_valid = Page(Html([Head(Body())]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_double_title():
    current_path = []
    is_page_valid = Page(Html([Head([Title(), Title()]), Body()]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_invalid_title():
    current_path = []
    is_page_valid = Page(Html([Head([Title()]), Body(Title())]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_no_body():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Div()]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_double_body():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div()), Body()]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_invalid_body():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Body())]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_valid_div():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div())]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == true

def test_invalid_li():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(Li()))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_valid_ul():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body([Ul(Li(Text("hello")))])]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == True

def test_empty_ul():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body([Ul()])]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_invalid_ul():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body([Ul(Text("invalid"))])]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_valid_span():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(Span(Text("hola"))))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == True

def test_invalid_span():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(Span(Table())))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_valid_span_p():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(Span(P(Text("Text")))))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == True

def test_valid_table():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(Table()))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == True

def test_invalid_table():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(Table(Span())))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_empty_tr():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(Table(Tr())))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_invalid_tr():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(Table(Tr(Tr()))))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_valid_tr():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(Table(Tr(Td()))))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == True

def test_valid_td():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(Table(Tr(Td()))))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == True

def test_invalid_td():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(Table(Tr(Td(Span())))))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_valid_div():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(H2()))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == True

def test_invalid_div():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(Div(P()))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_invalid_h1():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(H1(H1()))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_valid_h1():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body(H1(Text()))]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == True

def test_invalid_p():
    current_path = []
    is_page_valid = Page(Html([Head(Title()), Body([Span(P(Div()))])]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == False

def test_valid_assert():
    current_path = []
    is_page_valid = Page(Html(attr={"id": "page-content"}, content=[Head(Title(Text('"Hello ground!"'))), Body([Div(attr={"id": "main-content"}, content=[H1(Text('"Oh no, not again!"')), Img({"src": "image/open_me.jpg", "id": "image"})])])]))
    # print(is_page_valid)
    assert is_page_valid.is_valid(is_page_valid.root, current_path) == True
