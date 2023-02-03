
#this function adds the inputs
def addition(x, y):
    calc = float(x) + float(y)
    print(x, " + ", y, " = ", calc)


#this function subtracts the inputs
def subtraction(x, y):
    calc = float(x) - float(y)
    print(x, " - ", y, " = ", calc)


#this function multiplys the inputs
def multiplication(x, y):
    calc = float(x) * float(y)
    print(x, " * ", y, " = ", calc)


#this function divides the inputs
def division(x, y):
    calc = float(x) / float(y)
    print(x, " / ", y, " = ", calc)


#this function takes x to the power of y
def exponent(x, y):
    calc = float(x) ** float(y)
    print(x, " ^ ", y, " = ", calc)


stopCalc = False


while stopCalc is False:
    functionSelect = input('\n' "Select an operation: " +
                           '\n' "(1) Add" +
                           '\n' "(2) Subtract" +
                           '\n' "(3) Multiply" +
                           '\n' "(4) Divide" +
                           '\n' "(5) Exponent" '\n')

    if functionSelect not in ["1", "2", "3", "4", "5"]:
        print("Error!, that is not an operation in the list")

    else:
        #error handling number input 1
        while True:
            numberX = input("Enter first number: ")
            try:
                check = int(numberX) or float(numberX)
                break;
            except ValueError:
                print("That is not a valid number, try again")
        # error handling number input 2
        while True:
            numberY = input("Enter second number: ")
            try:
                check = int(numberY) or float(numberY)
                break;
            except ValueError:
                print("That is not a valid number, try again")

    if functionSelect == "1":
        addition(numberX, numberY)
    elif functionSelect == "2":
        subtraction(numberX, numberY)
    elif functionSelect == "3":
        multiplication(numberX, numberY)
    elif functionSelect == "4":
        division(numberX, numberY)
    elif functionSelect == "5":
        exponent(numberX, numberY)

    nextOperation = input('\n' "Would you like to perform another operation : "
                          '\n' "Yes or No" '\n')
    if nextOperation.upper() == "YES":
        stopCalc = False
    else:
        stopCalc = True

