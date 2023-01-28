#even odd number
number = float(input("Input a number: "))
result = number % 2

if result == 0:
    print(str(number) + "is a even number")
else:
    print(str(number) + "is a odd number")



#number 1 multiple of number 2
number1 = float(input("Input number 1: "))
number2 = float(input("Input number 2: "))

result = (number2/number1) % 1

if result == 0:
    print(str(number1) + " is a multiple of " + str(number2) )
else:
    print(str(number1) + " is not a multiple of " + str(number2) )