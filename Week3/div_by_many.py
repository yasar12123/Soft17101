def div_by_many (p, qs):
    qsCounter = 0
    divList = []
    try:
        for i in qs:
            divList.append(p/qs[qsCounter])
            qsCounter +=1
    except ZeroDivisionError:
        divList = []
    return divList


print(div_by_many(10,[3,4,6,7,8]))