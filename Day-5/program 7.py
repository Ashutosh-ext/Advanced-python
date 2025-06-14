class BankAccount:
    def __init__(self, account_number,balance):
        self.account_number = account_number
        self.balance = balance

    def calculate_interest(self):
        return self.balance * 0.01
    def display(self):
        print(f"Account Number: {self.account_number},Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.04

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.02

a = SavingsAccount("123456789",100)
b = CurrentAccount("123456789",1000)
a.display()
b.display()
print(f"Savings account interest:{a.calculate_interest()}")
print(f"Current account interest:{b.calculate_interest()}")
