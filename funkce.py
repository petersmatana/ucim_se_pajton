# -*- coding: utf-8 -*-

a = 13
o = object


def funkce(argument):
    """https://docs.python.org/2.7/tutorial/controlflow.html#defining-functions
    dokundamentace rika, ze argument se vklada hodnotou,
    jenze ta hodnota je reference na objekt

    pokud je uvedeno return tak funkce neco vraci...
    pokud return neni uvedeno, tak fce vraci None
    :param argument:
    :return:
    """
    print 'co je na vstupu = ', argument


def funkce2():
    """
    :return: tuple (pokud se nemylim tak tuple je
    immutable)
    """
    return 1, 2, 3


def volani_funkce2():
    a, b, c = funkce2()
    print 'funkce2 = ', a, b, c
    print 'co vraci fce2 za typ = ', type(funkce2())


def volani2_funkce2():
    for x in funkce2():
        print 'ted iteruju = ', x


# volani_funkce2()
# volani2_funkce2()
#
# print o
# funkce(o)
# print funkce


#       a   r   g   u   m   e   n   t   y


def f1(a, b='nic', c=13):
    print 'f1'
    print 'a = {0}, b = {1}, c = {2}'.format(a, b, c)

# f1(None)
# f1(10, None, 'ahoj')


def f2(yeeee, *lol, **omgdict):
    print 'yeeee = ', yeeee
    print '*lol = ', lol.append('asd')
    print '**omg = ', omgdict


f2(13, *[[1], [2], [3]], **{'a': 1, 'b': 2})

"""
    defakto rozdil mezi args a kwargs je ten ze
    args nejsou pojmenovane argumenty zato
    kwargs jsou pojmenovane
"""

def f3(*args):
    for x in args:
        print x


def f4(**kwargs):
    for x, y in kwargs.iteritems():
        print 'x = {0}, y = {1}'.format(x, y)


# f3(*[1,2,3])
# f3(123,123,123,12,312,312,3,123)
# f4(takto=1, se=2, vola=3, kwargs=4)




#              l   a   m   b   d   a
#                   (jako fce)


# nekde v mergadu mame toto: x = lambda x: x > 0
# takto se to nedela

def vetsi_jak(n):
    return lambda x: x > n


def mensi_jak(n):
    return lambda x: x < n


vetsi = vetsi_jak(10)
#print vetsi(13)

mensi = mensi_jak(0)
#print mensi(-13)
