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
