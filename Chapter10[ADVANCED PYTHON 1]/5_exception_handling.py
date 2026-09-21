#Exception handling is a way to handle errors so your program doesn't crash.


def divide(a, b):
    try:
        result = a / b                    # risky code goes here
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError as e:                # 'as e' stores the error message
        print("Wrong type:", e)
    except (ValueError, KeyError):        # catch multiple errors in one line
        print("Value or key problem")
    else:
        print("Success:", result)         # runs ONLY if there was NO error
        return result
    finally:
        print("Finally block executed")   # ALWAYS runs

divide(10, 2)     # Success: 5.0  then  Finally block executed
divide(10, 0)     # Cannot divide by zero  then  Finally block executed
divide(10, "a")   # Wrong type: ...  then  Finally block executed

"""
Easy way to remember:

Block	When it runs
try	always first, this is the risky code
except	only if an error happens
else	only if NO error happens
finally	always, error or not (good for closing files)
Raising your own errors

"""

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-1)
except ValueError as e:
    print("Caught:", e)     # Caught: Age cannot be negative

#Custom exception
class InsufficientBalance(Exception):
    pass

try:
    raise InsufficientBalance("Balance too low")
except InsufficientBalance as e:
    print(e)

#Newer feature: exception groups (Python 3.11+): When several errors happen together, except* handles each type separately:
try:
    raise ExceptionGroup("multiple", [ValueError("bad value"), TypeError("bad type")])
except* ValueError as eg:
    print("Value errors:", eg.exceptions)
except* TypeError as eg:
    print("Type errors:", eg.exceptions)

# note: This is a newer, rarely used feature. Focus on try / except / else / finally first.

