# inheritance + polymorphisum = methopd overriding

class Animal:
    def sound(self):
        print("Animal makes sound.")

class Dog(Animal):
    def sound(self):
        print("Dog says woof.")

class Cat(Animal):
    def sound(self):
        print("Cat says meow.")  

d = Dog()
c = Cat()

d.sound()
c.sound()