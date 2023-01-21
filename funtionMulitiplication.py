
def multiplication(numberN,numberM):
    totalNumber = 0
    for i in range(numberM):
        totalNumber += numberN

    print(numberN, " * ", numberM, " = ", totalNumber)

multiplication(int(input("input number 1: ")), int(input("input number 2: ")))
