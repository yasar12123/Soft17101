
#this function adds the inputs
def addition(x, y):
    calc = int(x) + int(y)
    print(calc)

#this function adds subtracts the inputs
def subtraction(x, y):
    calc = int(x) - int(y)
    print(calc)

#this function multiply's the inputs
def multiplication(x, y):
    calc = int(x) * int(y)
    print(calc)

#this function divides the inputs
def division(x, y):
    calc = int(x) / int(y)
    print(calc)


functionSelectInput = False

while functionSelectInput is False:
    functionSelect = input("Select an operation: " +
                            '\n' "(1) Add" +
                            '\n' "(2) Subtract" +
                            '\n' "(3) Multiply" +
                            '\n' "(4) Divide)")
    if functionSelect not in ["1","2", "3", "4"]:
        print("Error!, that is not a function")