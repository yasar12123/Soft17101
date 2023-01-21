numberN = int(input("input number 1: "))
numberM = int(input("input number 2: "))

numberList = [numberN, numberM]
numberList.sort()
lowestNumber = int(numberList[0]+1)
lcmFound = False
while lcmFound is False:
    for i in range(2, lowestNumber):
        if numberN % i == 0 and numberM % i == 0 and lcmFound is False:
            lcmFound = True
            print(i)
        else:
            print("none")




