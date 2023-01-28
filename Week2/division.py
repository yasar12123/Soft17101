numberN = int(input("input number 1: "))
numberM = int(input("input number 2: "))

numberNSubtract = numberN
numberOfSubtractions = 0
remainder = numberN % numberM

while numberNSubtract > 0:
    numberNSubtract = numberNSubtract - numberM
    numberOfSubtractions += 1

if numberNSubtract < 0:
    print((numberOfSubtractions - 1), "remainder ", remainder)
else:
    print(numberOfSubtractions)