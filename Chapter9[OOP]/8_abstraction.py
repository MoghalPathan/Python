from abc import ABC, abstractmethod


class Payment:
    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):
    def pay(self):
        print("pay using UPI.")

class Credit_card(Payment):
    def pay(self):
        print("Pay using Credit Card")


u = UPI()
c = Credit_card() 

u.pay()
c.pay()
            