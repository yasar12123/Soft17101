numberN = int(input("input number 1: "))
numberM = int(input("input number 2: "))
totalNumber = 0

for i in range(numberM):
    totalNumber += numberN

print(numberN, " * ", numberM, " = ", totalNumber)
