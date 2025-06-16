class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance # personal note: double underscore represents private in terms of variables.

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount < 0:
            print("Please enter a positive amount.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    



# Test
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance()) #outputs 1200
# print(acc.__balance) # raises attribute error when program is run