numberN = int(input("input number: "))
numberCounterStart = numberN - 1
numberCounterLoop = numberCounterStart
modulo = numberN % numberCounterLoop
isPrime = False

for i in range(2, numberCounterStart):
    while isPrime is False:
        if modulo != 0:
            numberCounterLoop -= 1
            isPrime = True
    else:
        isPrime = False

print(modulo)


