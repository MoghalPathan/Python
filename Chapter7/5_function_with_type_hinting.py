#Now we will see how to define a function with type hinting in python.
def greet6(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."

greeting_msg = greet6("Alice", 25)
print(greeting_msg)
print()
print()