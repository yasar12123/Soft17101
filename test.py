numberN = int(input("input number: "))
numberLoop = numberN - 1
modulo = 1
isPrime = False

while isPrime is False and modulo != 0:
    modulo = numberN % numberLoop
    numberLoop -= 1

print(modulo)