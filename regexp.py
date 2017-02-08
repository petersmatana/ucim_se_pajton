# -*- coding: utf-8 -*-

import re

text = """v tomto textu
budu mega moc hledat a hledat
a hledat, jestli nenajdu
taky se hodí vyhledávat nějakou
diakritiku ŽLUŤOUČKÉHO koně a jiná
zviřátka :)"""

text2 = u'v tomto teřxtu budu mega moc hleřdat a hledat a hledat, jeřstli nenajdu taky se hořdí vyhledávat nějařkou diakritiku ŽLUŤOUřČKÉHO koně a jiřná zviřátka :)'


def pokus1():
    match_obj = re.match(r'ŽLUŤOUČKÉHO', text)
    if match_obj:
        print '1) match, je tu'
    else:
        print '1) match, neni tu'


def pokus2():
    search_obj = re.search(r'ŽLUŤoUČKÉHO', text)

    """
    jinymi slovy pokud search_obj klapne tak vraci objekt
    Match. pokud nenajde, vraci None
    """
    # print 'typ search_obj = ', type(search_obj)

    if search_obj:
        print '2) search, je tu'
    else:
        print '2) search, neni tu'

# pokus2()


def pokus3():
    pattern = re.compile('ŽLUŤOUČKÉHO')
    match_obj = re.match(pattern, text)
    if match_obj:
        print '3) match, je tu'
    else:
        print '3) match, neni tu'


def get_char():
    return u'ř'


def unicode_pokus1():
    reg_exp = re.search(get_char(), text2, re.U)
    if reg_exp:
        print 'jo'
    else:
        print 'ne'

unicode_pokus1()
