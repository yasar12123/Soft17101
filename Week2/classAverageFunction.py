
#this function takes a list of numbers and returns the average
def classAverage(x):
    totalSum = sum([float(x) for x in x])
    average = totalSum / len(x)
    print("The total scores is: ", totalSum)
    print("The Average is: ", average)



list = [1,2,3,4,5,6,7,8,8,10,15,11,12]

classAverage(list)