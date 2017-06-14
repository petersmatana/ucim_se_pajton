# -*- coding: utf-8 -*-

class Rodic(object):

    def __call__(self):
        print 'call Rodic'


class Potomek(Rodic):

    '''
    def __call__(self):
        print 'call Potomek'
        super(Potomek, self).__call__()
    '''


p = Potomek()
p()
