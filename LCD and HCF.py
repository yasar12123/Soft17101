numberN = int(input("input number 1: "))
numberM = int(input("input number 2: "))

numberList = [numberN, numberM]
numberList.sort()
lowestNumber = int(numberList[0]+1)
multipleList = []

for i in range(2, lowestNumber):
    if numberN % i == 0 and numberM % i == 0:
        multipleList.insert(0, i)

if len(multipleList) == 0:
    print("There is no LCD of ", numberN, " and ", numberM)
    print("The HCF of ", numberN, " and ", numberM, " is 1")
else:
    print("The LCD of ", numberN, " and ", numberM, " is ", multipleList[-1])
    print("The HCF of ", numberN, " and ", numberM, " is ", multipleList[0])




