class BankAccount:
    def __init__(self):
        self.__balance = 0  

    def deposit(self, amount):
        self.__balance += amount 

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount 
        else:
            print("Money on your balance is not enough!")  

    def get_balance(self):
        return self.__balance 


# Тестування
account = BankAccount()
account.deposit(100)
print(account.get_balance())  
account.withdraw(50)
print(account.get_balance())
account.withdraw(100)