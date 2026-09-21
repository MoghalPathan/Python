
def greet(name):
    print("Hello, " + name + ". Good Morning!")

greet("Alice")
greet("Bob")
greet("Charlie")
print("\n")


#Now we will see how to define a function with return statement in python.
def get_greeting(name):
    return "Hello, " + name + ". Good Morning!"

g = get_greeting("Alice")
print(g)
print("\n")



#now we will see how to define a function with positional argument in python.
def greet4(name, age, /):      # the / forces name, age to be positional-only
    print(f"Hello, {name}. You are {age} years old.")

greet4("Alice", 25)
greet4("Bob", 30)
greet4("Charlie", 35)
print("\n")



#Now we will see how to define a function with variable number of argument in python.
def greet2(*names):
    for name in names:
        print(f"Hello, {name}. Good Morning!")

greet2("Alice", "Bob", "Charlie")
print("\n")




#Now we will see how to define a function with keyword argument in python.
def greet3(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet3(name="Alice", age=25, city="New York")
print("\n")

 


#Now we will see how to define a  function with keyword-only argument in python.
def greet5(*, name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet5(name="Alice", age=2)
greet5(name="Bob", age=3)
greet5(name="Charlie", age=3.5)
print("\n")