class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def bal(self):
        return self.balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print "Sorry, please maintain minimum balance."
        else:
            wa = BankAccount.withdraw(self, amount)
            return wa

b = MinimumBalanceAccount(10)
x = b.deposit(100)
print "Deposited Balance:", b.bal()
b.withdraw(5)
print "Withdrawn Balance:", b.bal()

# In this exercise we've inherit the property of parent class
# into a child class & create an object of child class
# to access the parent class functions.
