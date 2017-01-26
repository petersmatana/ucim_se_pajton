
# def what_1():
#     if 13 > 10:
#         print 'podminka prosla'
#
#     print 'what?'
#
#     else:
#         print 'podminka neprosla'


def what_2():
    x = [1,2,3]
    # x = [1]

    for asd in x:
        print asd

        if asd == 2:
            break
    else:
        print 'ou je'


def what_3():
    cislo = 0

    while cislo < 10:
        cislo += 1
        print 'jedu while = ', cislo

        if cislo == 3:
            # break
            pass
    else:
        print 'co?co?co?'


what_2()
# what_3()
