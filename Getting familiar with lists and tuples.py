
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


list1 = ["1", "2", "3", "2", "2", "6", "7"]
list2 = ["1", "2", "3", "2", "2", "4", "5", "6", "7"]


commonElements(list1, list2)

