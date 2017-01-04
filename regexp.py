# -*- coding: utf-8 -*-

import re

text = """v tomto textu
budu mega moc hledat a hledat
a hledat, jestli nenajdu
taky se hodí vyhledávat nějakou
diakritiku ŽLUŤOUČKÉHO koně a jiná
zviřátka :)"""


match_obj = re.match(r'ŽLUŤOUČKÉHO', text)
if match_obj:
    print 'match, je tu'
else:
    print 'match, neni tu'


search_obj = re.search(r'ŽLUŤOUČKÉHO', text)
if search_obj:
    print 'search, je tu'
else:
    print 'search, neni tu'
