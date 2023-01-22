numberN = int(input("input number 1: "))
numberM = int(input("input number 2: "))
numberList = [numberN, numberM]
numberList.sort()
counter = 1
lcmFound = False

if 1 in numberList:
    print(numberList[-1])
elif 0 in numberList:
    print("LCM of zero does not exist")
else:
    while lcmFound is False:
        if counter % numberN == 0 and counter % numberM == 0:
            lcmFound = True
        else:
            counter += 1

    print("Then LCM of ", numberN, " and ", numberM, " is ", counter)