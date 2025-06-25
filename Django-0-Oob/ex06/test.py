from Page import Page
from elements import *
import traceback
from elem import Elem, Text
import pytest

# def test_root_valid():
#     current_path = []
#     valid_page = Page(Html())
#     valid_page.is_valid(valid_page.root, current_path)

def test_valid_html_node():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body()]))
    valid_page.is_valid(valid_page.root, current_path)

def test_root_invalid():

    invalid_page = Page(Body())
    current_path = []
    invalid_page.is_valid(invalid_page.root, current_path)

def test_html_empty():
    invalid_page = Page(Html())
    current_path = []
    invalid_page.is_valid(invalid_page.root, current_path)   

def test_no_head():
    current_path = []
    valid_page = Page(Html([Body()]))
    valid_page.is_valid(valid_page.root, current_path)

def test_double_head():
    current_path = []
    valid_page = Page(Html([Head(Title()), Head()]))
    valid_page.is_valid(valid_page.root, current_path)

def test_invalid_head():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Head())]))
    valid_page.is_valid(valid_page.root, current_path)

def test_no_title():
    current_path = []
    valid_page = Page(Html([Head(Body())]))
    valid_page.is_valid(valid_page.root, current_path)

def test_double_title():
    current_path = []
    valid_page = Page(Html([Head([Title(), Title()]), Body()]))
    valid_page.is_valid(valid_page.root, current_path)

def test_invalid_title():
    current_path = []
    valid_page = Page(Html([Head([Title()]), Body(Title())]))
    valid_page.is_valid(valid_page.root, current_path)

def test_no_body():
    current_path = []
    valid_page = Page(Html([Head(Title()), Div()]))
    valid_page.is_valid(valid_page.root, current_path)

def test_double_body():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div()), Body()]))
    valid_page.is_valid(valid_page.root, current_path)

def test_invalid_body():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Body())]))
    valid_page.is_valid(valid_page.root, current_path)

def test_valid_div():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div())]))
    valid_page.is_valid(valid_page.root, current_path)

def test_invalid_li():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Li()))]))
    valid_page.is_valid(valid_page.root, current_path)

def test_valid_ul():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body([Ul(Li(Text("hello")))])]))
    valid_page.is_valid(valid_page.root, current_path)

def test_empty_ul():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body([Ul()])]))
    valid_page.is_valid(valid_page.root, current_path)

def test_invalid_ul():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body([Ul(Text("invalid"))])]))
    valid_page.is_valid(valid_page.root, current_path)

def test_valid_span():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Span(Text("hola"))))]))
    valid_page.is_valid(valid_page.root, current_path)

def test_invalid_span():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Span(Table())))]))
    valid_page.is_valid(valid_page.root, current_path)

def test_valid_table():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Table()))]))
    valid_page.is_valid(valid_page.root, current_path)

def test_invalid_table():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Table(Span())))]))
    valid_page.is_valid(valid_page.root, current_path)

def test_empty_tr():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Table(Tr())))]))
    valid_page.is_valid(valid_page.root, current_path)

def test_valid_tr():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(Div(Table(Tr(Td()))))]))
    valid_page.is_valid(valid_page.root, current_path)

def test_valid_div():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(H2())]))
    print(Page)
    valid_page.is_valid(valid_page.root, current_path)

def test_invalid_h1():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(H1(H1()))]))
    print(Page)
    valid_page.is_valid(valid_page.root, current_path)

def test_valid_p():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body([P(Text("la"))])]))
    valid_page.is_valid(valid_page.root, current_path)

def test_invalid_p():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body([P(Div())])]))
    valid_page.is_valid(valid_page.root, current_path)

def test_invalid_test():
    current_path = []
    valid_page = Page(Html([Head(Title()), Body(H1(Div()))]))
    valid_page.is_valid(valid_page.root, current_path)
