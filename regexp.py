# -*- coding: utf-8 -*-

import re

text = """v tomto textu
budu mega moc hledat a hledat
a hledat, jestli nenajdu
taky se hodí vyhledávat nějakou
diakritiku ŽLUŤOUČKÉHO koně a jiná
zviřátka :)"""

# print type(text)

text2 = u'v tomto teřxtu budu mega moc hleřdat a hledat a hledat, jeřstli nenajdu taky se hořdí vyhledávat nějařkou diakritiku ŽLUŤOUřČKÉHO koně a jiřná zviřátka :)'

# print type(text2)

text3 = """

                                asd    fuuuu
                ererer

                    ŽLUŤOUČKÉHO


"""

unicode_text3 = u'asd    fuuuu  ererer ŽLUŤOUČKÉHO'


def pokus1():
    match_obj = re.match(r'ŽLUŤOUČKÉHO', text)
    if match_obj:
        print '1) match, je tu'
    else:
        print '1) match, neni tu'  # vrati se


# pokus1()


def unicode_pokus1():
    match_obj = re.match(u'ŽLUŤOUČKÉHO', text3)
    if match_obj:
        print '1) match, je tu'
    else:
        print '1) match, neni tu'  # vrati se, ani kdyz pouziju re.U


# unicode_pokus1()


def unicode_pokus2():
    match_obj = re.search(u'UŤOUČK', unicode_text3, re.U)
    if match_obj:
        print '1) search, je tu'  # vrati se
    else:
        print '1) search, neni tu'


# unicode_pokus2()


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
        print '2) search, neni tu'  # vrati se, dava smysl


pokus2()


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

# unicode_pokus1()
