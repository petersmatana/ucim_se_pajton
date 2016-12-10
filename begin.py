# -*- coding: utf-8 -*-


def pprint():
    print """asd
        -h asd
            - asd"""


def pprint2():
    """string - retezec je immutable
    :return:
    """
    p = 'python'
    print p[-5:-1]

    print p[:]


def pprint3():
    py = 'python'
    for character in py[:]:
        print character


# pprint3()


def list():
    """list je mutable, takze je pomaly
    :return:
    """
    ll = list([1, 2, 3])
    ll.append(4)

    print ll
