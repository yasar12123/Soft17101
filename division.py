numberN = int(input("input number 1: "))
numberM = int(input("input number 2: "))
numberNStart = numberN
counter = 0

while numberNStart > 0:
    if numberNStart > 0 and (numberN % numberM) == 0:
        numberNStart = numberNStart - numberM
        counter += 1

    elif (numberN % numberM) > 0:
        print("cant divide ",numberN, " by ",numberM  )
        break

print(numberN, " divided by ",numberM, " = ", counter)


