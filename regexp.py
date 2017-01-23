# -*- coding: utf-8 -*-

import re

text = """v tomto textu
budu mega moc hledat a hledat
a hledat, jestli nenajdu
taky se hodí vyhledávat nějakou
diakritiku ŽLUŤOUČKÉHO koně a jiná
zviřátka :)"""


def pokus1():
    match_obj = re.match(r'ŽLUŤOUČKÉHO', text)
    if match_obj:
        print '1) match, je tu'
    else:
        print '1) match, neni tu'


def pokus2():
    search_obj = re.search(r'ŽLUŤOUČKÉHO', text)
    if search_obj:
        print '2) search, je tu'
    else:
        print '2) search, neni tu'


def pokus3():
    pattern = re.compile('ŽLUŤOUČKÉHO')
    match_obj = re.match(pattern, text)
    if match_obj:
        print '3) match, je tu'
    else:
        print '3) match, neni tu'

pokus3()
