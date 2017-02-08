# -*- coding: utf-8 -*-

'''

    fajnova prerekvizita:
    - http://nvie.com/posts/iterators-vs-generators/
    - https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/

'''

def poprve():
    """Kdyz mam list, v nem elementy a nad
    nima jedu forem, rika se tomu iterace
    """
    mylist = [1, 2, 3]
    for element in mylist:
        print element

def podruhe():
    """Druha moznost je si seznam vygenerovat
    pomoci list comprihension. mylist je
    iterable.
    """
    mylist = [x for x in range(3)]
    for element in mylist:
        print element

def generator():
    """Docela zajimavosti je ze skrz generator
    muzu iterovat jen jednou.
    """
    mygenerator = (x for x in range(3))
    for element in mygenerator:
        print 'poprve = ', element

    for element in mygenerator:
        print 'podruhe = ', element

# generator()

def vytvorit_generator():
    """Yield je klicove slovo, ktere se pouziva jako
    return az na to, ze to vraci generator
    """
    mylist = range(3)
    print 'mylist = ', mylist
    for element in mylist:
        yield element

def pouzit_generator():
    mygenerator = vytvorit_generator()
    for element in mygenerator:
        print element

pouzit_generator()
