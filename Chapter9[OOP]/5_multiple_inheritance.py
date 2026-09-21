class Father:

    def drive(self):
        print("Father is driving.")


class Mother:

    def cook(self):
        print("Mother is cooking.") 

class Child(Father, Mother):

    def cry(self):
        print("Child is crying")


c = Child()
c.drive()
c.cook()
c.cry()        