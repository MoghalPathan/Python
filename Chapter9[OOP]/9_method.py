"""

There are mainly 3 types of Methods in Python:

                o. Instance Method
                o. Class Method (@classmethod)
                o. Static Method (@staticmethod)
                
                
"""



#instance method

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name: " + self.name)

s = Student("Naved")
s.display() 
print()           



#class method

class Student1:

    school = "Abc"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school



print(Student1.school)

Student1.change_school("xyz")
print(Student1.school)
print()

#stastic method
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.add(10, 20))
print(Calculator.multiply(5, 4))