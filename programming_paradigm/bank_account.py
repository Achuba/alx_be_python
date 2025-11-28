class BankAccount:
    def __init__(self, account_balance):
        self.__account_balance = account_balance
    
    
    def deposit(self, amount):
        self.__account_balance += amount
        return self.__account_balance
        
    def withdraw(self, amount):
        if amount > self.__account_balance:
            raise ValueError("Insurficient Funds")
        self.__account_balance -= amount
        return self.__account_balance
            
    def display_balance(self) :
        print(f"Current Balance: ${self.__account_balance}")
