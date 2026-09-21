#Encapsulation means keeping data protected inside a class 
# and controlling how it can be accessed or changed.


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance      #'balance' is a private attribute/variable coz of double underscore and by protecting and hadling it we use encapsulation here.


    def show_balance(self):
        print(f"Current Balance:{self.__balance}")    

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Money deposited")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Money withdrawn") 


    def show_balance(self):
            print(f"Current Balance:{self.__balance}")           


acc = BankAccount("Naved", 25000000)
acc.show_balance()               
print()
acc.deposit(10000000)
acc.show_balance()
print()
acc.withdraw(1000000)
acc.show_balance()
print()
acc.withdraw(10000)
acc.show_balance()
print()