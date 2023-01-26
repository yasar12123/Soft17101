
#This function checks if the input is in a list
def crossReference (input, list):
    if input in list:
        print(True)
    else:
        print(False)


#This function removes
def removeFromList(input, list):
    while (input in list):
        list.remove(input)


#This function removes duplicates from a list
def removeDuplicates(list):
    distinctList = []
    [distinctList.append(x) for x in list if x not in distinctList]
    print(distinctList)


#This function returns common elements between two lists
def commonElements(list1, list2):
    commonElementsList = []
    counterElementInList = 0
    for i in list1:
        if list1[counterElementInList] in list2:
            commonElementsList.append(list1[counterElementInList])
            counterElementInList += 1
    distinctList = []
    [distinctList.append(x) for x in commonElementsList if x not in distinctList]
    print(distinctList)


#This function takes a list of integers and returns if they are even or odd numbers
def OddEvenCheck(userInput):
    userInputList = userInput
    evenOddList = []
    uilCounter = 0
    for i in userInputList:
        if int(userInputList[uilCounter]) % 2 == 0:
            evenOddList.append('({}, even)'.format(userInputList[uilCounter]))
        if int(userInputList[uilCounter]) % 2 != 0:
            evenOddList.append('({}, odd)'.format(userInputList[uilCounter]))
        uilCounter += 1
    print(evenOddList)


#Write in python function descending (n, m) which returns a list of integers from integer n to m (both inclusive) in descending order.
# Example: descending (2, 4) should return [4, 3, 2]
def numberRange(x, y):
    rangeCounter = x
    numberRangeList = []
    for i in range(x, y+1):
        numberRangeList.append(rangeCounter)
        rangeCounter += 1
    numberRangeList.reverse()
    print(numberRangeList)



list1 = ["1", "2", "3", "2", "2", "6", "7"]
list2 = ["1", "2", "3", "2", "2", "4", "5", "6", "7"]


commonElements(list1, list2)

