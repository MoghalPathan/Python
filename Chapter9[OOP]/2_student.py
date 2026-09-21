class Student:     #class created

    def __init__(self, name, age, marks):    #__init__() is a constructor & automatically created when we call an object
        self.name = name       #here 'self' refer to the current object in that method
        self.age = age 
        self.marks =  marks

    def display(self):                #display() method created
        print("name:", self.name)   
        print("age:", self.age) 
        print("marks:", self.marks)   

s = Student("Naved", 21, 88)       #object 
s1 = Student("Sayali", 21, 90)     #object
s2 = Student("Manasi", 21, 85)     #object
s3 = Student("Shriram", 23, 71)    #object

s.display()              #display() method called
print()                  # add space(single line) between two line
s1.display()
print()
s2.display()
print()
s3.display()
        
