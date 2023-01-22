
#this function adds the inputs
def addition(x, y):
    calc = float(x) + float(y)
    print(calc)

#this function adds subtracts the inputs
def subtraction(x, y):
    calc = float(x) - float(y)
    print(calc)

#this function multiply's the inputs
def multiplication(x, y):
    calc = float(x) * float(y)
    print(calc)

#this function divides the inputs
def division(x, y):
    calc = float(x) / float(y)
    print(calc)


functionSelect = input("Select an operation: " +
                        '\n' "(1) Add" +
                         '\n' "(2) Subtract" +
                         '\n' "(3) Multiply" +
                         '\n' "(4) Divide)")

if functionSelect not in ["1", "2", "3", "4"]:
    print("Error!, that is not a function")

else:
    numberX = input("Enter a first number: ")
    if isinstance(float(numberX), float) == False:
        print("That is not a number: ")

    else:
        numberY = input("Enter a second number: ")
        if isinstance(float(numberY), float) == False:
            print("That is not a number: ")
        else:
            if functionSelect == "1":
                addition(numberX, numberY)
            elif functionSelect == "2":
                subtraction(numberX, numberY)
            elif functionSelect == "3":
                multiplication(numberX, numberY)
            elif functionSelect == "4":
                division(numberX, numberY)
