# function in python are defined using the def keyword.
# A function is a block of code thatv only runs when it is called. You can pass data, known as parameters, into a function. 
# A function can return data as a result. Now we will see how to define a function in python.

def greet(name):
    print("Hello, " + name + ". Good Morning!")

greet("Alice")
greet("Bob")
greet("Charlie")
print("\n")


#Now we will see how to define a function with return statement in python.
def get_greeting(name):
    return "Hello, " + name + ". Good Morning!"

greeting_message = get_greeting("Alice")
print(greeting_message)
print("\n")


#Now we will see how to define a function with default parameter in python.
def greet1(name="Guest"):
    print(f"Hello, {name}. Good Morning!")

greet1()
greet1("Alice")
greet1("Bob")
greet1("Charlie")
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


#now we will see how to define a function with positional argument in python.
def greet4(name, age, /):      # the / forces name, age to be positional-only
    print(f"Hello, {name}. You are {age} years old.")

greet4("Alice", 25)
greet4("Bob", 30)
greet4("Charlie", 35)
print("\n")


#Now we will see how to define a  function with keyword-only argument in python.
def greet5(*, name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet5(name="Alice", age=2)
greet5(name="Bob", age=3)
greet5(name="Charlie", age=3.5)
print("\n")


#Now we will see how to define a function with type hinting in python.
def greet6(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."

greeting_msg = greet6("Alice", 25)
print(greeting_msg)
print()
print()


#Now we  will see how to define a function with docstring in python.
def greet7(name: str, age: int) -> str:
    """
    This function greets a person with their name and age.
    
    Parameters:
    name (str): The name of the person.
    age (int): The age of the person.
    
    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}. You are {age} years old."

greeting_msg = greet7("Alice", 25)
print(greeting_msg)
print()
print()


#Now we will see how to define a lambda function in python.
square = lambda x: x * x
print(square(5))
print("\n")


#Now we will see how to define a recursive function in python.
n = int(input("Enter a number to find its factorial: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"the factorial of {n} is {factorial(n)}")
print("\n")


#now we will see how to define a function with nested function in python.
def outer_function(x):
    def inner_function(y):
        return y * y
    return inner_function(x) + 1

print(outer_function(5))
print("\n")


#now we will see how to define a function with closure in python.
def outer_function(msg):
    def inner_function():
        print(f"Message from closure: {msg}")
    return inner_function

my_closure = outer_function("Hello, World!")
my_closure()
print("\n")


#now we will see how to define a function with decorator in python.
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something before the function runs.")
        result = func(*args, **kwargs)
        print("Something after the function runs.")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


    