from Page import Page
from elements import *
import traceback
from elem import Elem, Text
import pytest

def test_valid_html_node():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body()]))
    assert valid_page.is_valid(valid_page.root, current_path) == True

def test_root_invalid():
    valid_page = Page(Body())
    current_path = []
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_html_empty():
    valid_page = Page(Html())
    current_path = []
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_no_head():
    current_path = []
    valid_page = Page(Html([Body()]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_double_head():
    current_path = []
    valid_page = Page(Html([Head(Title()), Head()]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_invalid_head():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Head())]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_no_title():
    current_path = []
    valid_page = Page(Html([Head(Body())]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_double_title():
    current_path = []
    valid_page = Page(Html([Head([Title(), Title()]), Body()]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_invalid_title():
    current_path = []
    valid_page = Page(Html([Head([Title()]), Body(Title())]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_no_body():
    current_path = []
    valid_page = Page(Html([Head(Title()), Div()]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_double_body():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div()), Body()]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_invalid_body():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Body())]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_valid_div():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div())]))
    assert valid_page.is_valid(valid_page.root, current_path) == true

def test_invalid_li():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Li()))]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_valid_ul():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body([Ul(Li(Text("hello")))])]))
    assert valid_page.is_valid(valid_page.root, current_path) == True

def test_empty_ul():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body([Ul()])]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_invalid_ul():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body([Ul(Text("invalid"))])]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_valid_span():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Span(Text("hola"))))]))
    assert valid_page.is_valid(valid_page.root, current_path) == True

def test_invalid_span():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Span(Table())))]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_valid_span_p():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Span(P())))]))
    assert valid_page.is_valid(valid_page.root, current_path) == True

def test_valid_table():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Table()))]))
    assert valid_page.is_valid(valid_page.root, current_path) == True

def test_invalid_table():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Table(Span())))]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_empty_tr():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Table(Tr())))]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_invalid_tr():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Table(Tr(Tr()))))]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_valid_tr():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Table(Tr(Td()))))]))
    assert valid_page.is_valid(valid_page.root, current_path) == True

def test_valid_td():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Table(Tr(Td()))))]))
    assert valid_page.is_valid(valid_page.root, current_path) == True

def test_invalid_td():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Table(Tr(Td(Span)))))]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_valid_div():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(H2()))]))
    assert valid_page.is_valid(valid_page.root, current_path) == True

def test_invalid_div():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(P()))]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_invalid_h1():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(H1(H1()))]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

def test_valid_h1():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(H1(Text()))]))
    assert valid_page.is_valid(valid_page.root, current_path) == True

def test_valid_p():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body([P(Text("la"))])]))
    assert valid_page.is_valid(valid_page.root, current_path) == True

def test_invalid_p():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body([Span(P(Div()))])]))
    assert valid_page.is_valid(valid_page.root, current_path) == False

#TEST TEXT