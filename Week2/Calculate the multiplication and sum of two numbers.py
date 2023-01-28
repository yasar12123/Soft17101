# Given two integer numbers return their product only if the product is equal to or lower than 1000,
# else return their sum.

number1 = float(input("Please input first number: "))
number2 = float(input("Please input second number: "))
multiply = number1 * number2
addition = number1 + number2

if multiply <= 1000:
    print(str(number1) + " * " + str(number2) + " = " + str(multiply))
elif multiply > 1000:
    print(str(number1) + " + " + str(number2) + " = " + str(addition))