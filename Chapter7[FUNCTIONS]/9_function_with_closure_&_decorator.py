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