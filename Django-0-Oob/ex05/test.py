from elements import *
from elem import *
import pytest

def test_html():
    Html()

def test_head():
    Head()

def test_body():
    Body()

def test_title():
    Title()

def test_meta():
    Meta()

def test_img():
    Img()

def test_table():
    Table()

def test_th():
    Th()

def test_td():
    Td()

def test_tr():
    Tr()

def test_ul():
    Ul()

def test_ol():
    Ol()

def test_li():
    Li()

def test_h1():
    H1()

def test_h2():
    H2()

def test_p():
    P()

def test_div():
    Div()

def test_span():
    Span()

def test_hr():
    Hr()

def test_br():
    Br()

def test_valid_html_node():
    valid_page = Html([Head(Title()), Body()])
