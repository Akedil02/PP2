class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")
        else:
            print("Insufficient funds. Withdrawal not allowed.")

account = BankAccount("Akedil", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(800)  
