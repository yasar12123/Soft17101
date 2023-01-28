
calculation = str(input("what calculation would you like to process: "))
calculationList = [i for i in calculation]
operators = ["+", "-", "/", "*", " "]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


if any(item not in (numbers+operators) for item in calculationList):
    print("error")
else:
    print(eval(calculation))