# function in python are defined using the def keyword.
# A function is a block of code thatv only runs when it is called. You can pass data, known as parameters, into a function. 
# A function can return data as a result. Now we will see how to define a function in python.
# A functin can be craeted using 'def' keyword.
#function can be called using function_name()
#In python there are 2 types of functions : 1. Built-in function[len(), print(), range()]   2. User Defined Function

#pr1
def avg():
    a = int(input("Enter 1st no. : "))
    b = int(input("Enter 2nd no. : "))
    c = int(input("Enter 3rd no. : "))

    avg = (a+b+c)/3
    print(avg)
    
avg()
avg()  # function perfoem similar tasks repitadely
















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


    