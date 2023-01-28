
#This function gets the LCM for the given numbers
def findLCM(numberN:int, numberM:int):
    numberList = [numberN, numberM]
    numberList.sort()
    counter = 1
    lcmFound = False

    try:
        while lcmFound is False:
            if counter % numberN == 0 and counter % numberM == 0:
                lcmFound = True
            else:
                counter += 1
        print("Then LCM of ", numberN, " and ", numberM, " is ", counter)

    except ZeroDivisionError:
        print("LCM of zero does not exist")




findLCM(45, 34)



