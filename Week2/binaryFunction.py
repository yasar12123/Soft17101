#This function takes the input and converts it into binary
def binary(numberN:int):
    numberNStore = numberN
    binaryList = []
    if numberN < 0:
        raise ValueError("The give number %d is negative" %numberN)
    elif numberN == 0:
        binaryList.insert(0,0)
    else:
        while numberNStore != 0:
            if numberNStore != 0:
                binaryList.insert(0, (numberNStore % 2))
                numberNStore = numberNStore // 2
    print("The binary for ", numberN, " is ", binaryList)

binary(50)