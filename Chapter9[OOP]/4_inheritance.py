"""

class Vehical:
    def start(self):
        print("Vehical is starting.")

class Car(Vehical):
    def drive(self):
        print("Car is driving.")        


c = Car()

c.start()
c.drive()

"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Engineer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)    #here we used super() to call name and salary variables.
        self.language= language

    def display(self):
            print("Name:" + self.name)
            print("Salary:", self.salary)     #You canot concate string with int 
            print("Language:" + self.language)


e = Engineer("Naved", 5000000, " Manderian")

e.display()
           
