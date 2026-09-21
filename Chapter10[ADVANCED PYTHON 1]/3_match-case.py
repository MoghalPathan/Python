#Match-case (Python 3.10+) is a cleaner replacement for long if / elif / elif chains.
# It is like switch in C or Java, but more powerful.

#Basic version
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:     # | means OR
            return "Server Error"
        case _:                   # _ means anything else (default)
            return "Unknown"

print(http_status(404))   # Not Found
print(http_status(502))   # Server Error
print(http_status(1))     # Unknown


"""
Only the first matching case runs. There is no break.
_ is the default case and should be last.
Matching patterns (this is where it becomes powerful)

"""

#Tuples, and capturing values:
def check_point(p):
    match p:
        case (0, 0):
            return "Origin"
        case (x, 0):                 # x captures whatever the first value is
            return f"On X axis at {x}"
        case (0, y):
            return f"On Y axis at {y}"
        case (x, y):
            return f"Point at {x}, {y}"

print(check_point((5, 0)))   # On X axis at 5
print(check_point((2, 3)))   # Point at 2, 3



#Dictionaries:
def command(cmd):
    match cmd:
        case {"action": "play", "song": song}:
            return f"Playing {song}"
        case {"action": "stop"}:
            return "Stopped"
        case _:
            return "Invalid command"

print(command({"action": "play", "song": "Believer"}))  # Playing Believer

#This is very useful for voice assistant commands, which is close to what you're building.





#Guard (extra condition with if):
def number_type(n):
    match n:
        case int() if n < 0:
            return "Negative integer"
        case int():
            return "Positive integer or zero"
        case str():
            return "It's a string"

#int() here checks the type of the value.

