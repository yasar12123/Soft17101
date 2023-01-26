

def numberRange(x, y):
    rangeCounter = x
    numberRangeList = []
    for i in range(x, y+1):
        numberRangeList.append(rangeCounter)
        rangeCounter += 1
    numberRangeList.reverse()
    print(numberRangeList)

numberRange(4,10)