from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance):
        self._balance = balance
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @property
    def balance(self):
        return self._balance

class CheckingAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount

class SavingsAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount

class BusinessAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
def atm_program():
    # Create account instances
    checking_account = CheckingAccount(1000)
    savings_account = SavingsAccount(5000)
    business_account = BusinessAccount(20000)
    
    # ATM program loop
    while True:
        print("Welcome to the ATM program.")
        print("Select an account to access:")
        print("1. Checking Account")
        print("2. Savings Account")
        print("3. Business Account")
        print("4. Exit")
        
        account_choice = input("Enter your choice: ")
        
        if account_choice == "1":
            print("You have selected Checking Account.")
            print(f"Your balance is {checking_account.balance}.")
            transaction_type = input("Enter the transaction type (d for deposit, w for withdraw): ")
            
            if transaction_type == "d":
                amount = float(input("Enter the amount to deposit: "))
                checking_account.deposit(amount)
                print(f"Deposit successful. Your new balance is {checking_account.balance}.")
            elif transaction_type == "w":
                amount = float(input("Enter the amount to withdraw: "))
                checking_account.withdraw(amount)
                print(f"Withdrawal successful. Your new balance is {checking_account.balance}.")
            else:
                print("Invalid transaction type.")
        
        elif account_choice == "2":
            print("You have selected Savings Account.")
            print(f"Your balance is {savings_account.balance}.")
            transaction_type = input("Enter the transaction type (d for deposit, w for withdraw): ")
            
            if transaction_type == "d":
                amount = float(input("Enter the amount to deposit: "))
                savings_account.deposit(amount)
                print(f"Deposit successful. Your new balance is {savings_account.balance}.")
            elif transaction_type == "w":
                amount = float(input("Enter the amount to withdraw: "))
                savings_account.withdraw(amount)
                print(f"Withdrawal successful. Your new balance is {savings_account.balance}.")
            else:
                print("Invalid transaction type.")
        
        elif account_choice == "3":
            print("You have selected Business Account.")
            print(f"Your balance is {business_account.balance}.")
            transaction_type = input("Enter the transaction type (d for deposit, w for withdraw): ")
            
            if transaction_type == "d":
                amount = float(input("Enter the amount to deposit: "))
                business_account.deposit(amount)
                print(f"Deposit successful. Your new balance is {business_account.balance}.")
            elif transaction_type == "w":
                amount = float(input("Enter the amount to withdraw: "))
                business_account.withdraw(amount)
                print(f"Withdrawal successful. Your new balance is {business_account.balance}.")
            else:
                print("Invalid transaction type.")
        
        elif account_choice == "4":
            print("Thank you for using the ATM program.")
            break
        
        else:
            print("Invalid account choice.")


obj=atm_program()
