
class Trida(object):

    def __init__(self):
        print('init')

    def __new__(cls, *args, **kwargs):
        return super(Trida, cls)

t = Trida()
print(t)

