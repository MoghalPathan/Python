"""

"Dunder" means double underscore.


__init__
__str__
__len__
__eq__
__add_


"""





#__str__
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}\nMarks: {self.marks}"


student = Student("Rahul", 85)

print(student)
print()




#__eq__
class Student1:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.name == other.name and self.marks == other.marks


s1 = Student1("Rahul", 85)
s2 = Student1("Rahul", 85)

print(s1 == s2)