#This function takes the input and converts it into binary
def binary(numberN):
    numberNStore = numberN
    binaryList = []
    while numberNStore != 0:
        if numberNStore != 0:
            binaryList.insert(0, (numberNStore % 2))
            numberNStore = numberNStore // 2
    print("The binary for ", numberN, " is ", binaryList)

binary(45)