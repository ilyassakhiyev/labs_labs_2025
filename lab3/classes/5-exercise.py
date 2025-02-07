class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawing: {amount}. New balance: {self.balance}")


account = BankAccount("Ilyas", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)