
def primeRange(numberN):
    if numberN < 2:
        raise ValueError("There is no prime number under 2")
    else:
        for iLoop in range(2, numberN+1):
            for i in range(2, iLoop):
                if (iLoop % i) == 0:
                    break
            else:
                print(iLoop)

primeRange(111)