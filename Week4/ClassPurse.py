class Purse:
    """
    A class to store bank accounts.
    """
    def __init__(self, purseNumber, purseHolderName, openingBalance):
        self.purseNumber = purseNumber
        self.purseHolderName = purseHolderName
        self.openingBalance = openingBalance

    def __str__(self):
        return ('\n' "Purse Number: " + str(self.purseNumber) +
                '\n' "Purse Holder Name: " + self.purseHolderName +
                '\n' "Opening Balance: " + str(self.openingBalance))

    def deposit(self, amount:int):
        if amount <= 0:
            raise ValueError("The deposit amount should be greater than 0")
        self.openingBalance += amount
        return self.openingBalance

    def withdraw(self, amount:int):
        if amount <= 0:
            raise ValueError("The withdrawal amount should be greater than 0")
        if (self.openingBalance - amount) < 0:
            raise ValueError("The withdrawal of %d will take the account into a negative balance" % amount)
        self.openingBalance -= amount
        return self.openingBalance


    def transferFunds(self, purseTo, amount:int):
        if amount <= 0:
            raise ValueError("The transfer amount should be greater than 0")
        if (self.openingBalance - amount) < 0:
            raise ValueError("The transfer of %d will take the account into a negative balance" % amount)
        purseTo.openingBalance += amount
        self.openingBalance -= amount
        return self.openingBalance, purseTo.openingBalance


p1 = Purse(12, "jon doe", 100)
p2 = Purse(34, "mike one", 0)
p3 = Purse(56, "mike two", 0)
p4 = Purse(78, "harry three", 0)

people = [p1,p2,p3,p4]

p1.transferFunds(p2,100)

print(p1,p2)
