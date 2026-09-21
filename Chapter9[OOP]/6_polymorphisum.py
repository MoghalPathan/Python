class Dog:                
    def sound(self):     #here both classes has same method
        print("Dog says woof.")

class Cat:
    def sound(self):     #here both classes has same method
        print("Cat says meow.")


d = Dog()
c = Cat()

d.sound()
c.sound()