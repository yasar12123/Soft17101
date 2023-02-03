class Account:
    """
    A class to store bank accounts.
    """
    def __init__(self, accNumber, accHolderName, openingBalance, accType):
        self.accNumber = accNumber
        self.accHolderName = accHolderName
        self.openingBalance = openingBalance
        self.accType = accType

    def __str__(self):
        return ('\n' "Account Number: " + str(self.accNumber) +
                '\n' "Account Holder Name: " + self.accHolderName +
                '\n' "Opening Balance: " + str(self.openingBalance) +
                '\n' "Account Type: " + self.accType)

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

    #get_balance()

acc1 = Account(123, "jon doe", 100, "standard variable")

acc1.withdraw(50)
print(acc1)