class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds or invalid withdraw amount.")

useraccount = BankAccount("123456789", "Delvin Gonzalez")


useraccount.withdraw(700)  # This one fails due to being an insufficent amount 
useraccount.deposit(1000)  
useraccount.withdraw(500) 

print(f"Final balance {useraccount.balance}")