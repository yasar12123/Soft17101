import math
def sqrtCalc(n : int):
    if n < 0:
        raise ValueError("Error! The give number %d is negative" %n)
    return math.sqrt(n)

try:
    print("Let's calculate the square root of a number!")
    n = int(input("Enter a number you that you want the square root of: "))
    sq = sqrtCalc(n)
    print("The square root is: %d" %sq)
except ValueError as err:
    print('Invalid input: %s' % err)