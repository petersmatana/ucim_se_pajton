def poprve():
    import datetime

    datum = datetime.datetime(year=2017, month=10, day=13,
                              hour=0, minute=0, second=0)

    print 'datum co jsem si nasteloval = ', datum
    print 'den = ', datum.day

    # tohle je blby, den 53 se jaksi v kalendari neobjevuje
    print 'aritmetika = ', datum.day + 40

# poprve()


def rozdil_casu():
    import datetime
    from datetime import timedelta
    dnes = datetime.datetime.now()

    # docela uzitecne, takto muzu aritmeticky pracovat
    # s casem
    minulost = timedelta(days=123)
    print 'minulost = ', dnes - minulost

    print 'dnes     = ', dnes

# rozdil_casu()


def porovnavani_casu():
    import datetime
    from datetime import timedelta
    dnes = datetime.datetime.now()
    minulost = timedelta(days=123)

    # toto nemuzu udelat, nemuzu porovnavat cas typu
    # datetime a timedelta
    # if dnes > minulost:
    #     ...

    print type(dnes), dnes
    print type(minulost), minulost
    x = datetime.datetime.now()-minulost
    print type(x), x

    if dnes > x:
        print 'ano'
    else:
        print 'ne'

porovnavani_casu()
