
#function is called to find the lowest common divisor of two numbers
def findLcd(numberN, numberM):
    numberList = [numberN, numberM]
    numberList.sort()
    lowestNumber = int(numberList[0]+1)
    multipleList = []
    lcdFound = False
    while lcdFound is False:
        for i in range(2, lowestNumber):
            if lcdFound is False and numberN % i == 0 and numberM % i == 0:
                multipleList.insert(0, i)
                lcdFound = True
        if len(multipleList) == 0:
            print("there is no LCD")
            lcdFound = True
        else:
            print("The LCD of ", numberN, " and ", numberM, " is ", multipleList)

findLcd(5000,4050)




