
def poprve():
    promenna = None
    print promenna


def podruhe():
    """vypise se false
    """
    promenna = None
    if promenna:
        print 'true'
    else:
        print 'false'

    if promenna is not None:
        print 'true 2'
    else:
        print 'false 2'


def potreti():
    """vypise se prekvapive true
    """
    promenna = None
    if not promenna:
        print 'true'
    else:
        print 'false'


def poctvrte():
    """py je ohebny
    """
    promenna = None
    print promenna
    if not promenna:
        promenna = 10
    print promenna

# poprve()
podruhe()
# potreti()
# poctvrte()