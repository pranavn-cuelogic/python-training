class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

a = BankAccount()
b = BankAccount()

print "A deposit 100:", a.deposit(100)
print "B deposit 50:", b.deposit(50)

print "A withdraw 12:", a.withdraw(12)
print "B withdraw 15:", b.withdraw(15)

# A simple exercise to show how we can use the class & its
# object to do the simple operation of deposit & withdraw amount
# in two different accounts.
