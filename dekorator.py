# -*- coding: utf-8 -*-

# https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

# expresni uvod do dekoratoru...

def muj_dekorator(func):
    def cokoli(name):
        return "<i>{0}</i>".format(func(name))

    return cokoli


@muj_dekorator
def get_text(text):
    return "nejaky text: {0}".format(text)

# print get_text('ahoj')

################################################################################


def i_tag(func):
    def inner_func(text):
        return "<i>{0}</i>".format(func(text))
    return inner_func


def b_tag(func):
    def inner_func(text):
        return "<b>{0}</b>".format(func(text))
    return inner_func


@i_tag
@b_tag
def jedu(text):
    return text

@b_tag
@i_tag
def jedu2(text):
    return text

print jedu2("asd")
