"""
2. Lambda functions

What it is: a small, nameless, one-line function.
"""

"""

# Normal
def square(x):
    return x * x

# Lambda (same thing)
square = lambda x: x * x

print(square(5))


"""


add = lambda a, b: a + b
print(add(3, 4))                      # 7

is_even = lambda n: n % 2 == 0
print(is_even(10))                    # True

greet = lambda name: f"Hello {name}"
print(greet("Naved"))                 # Hello Naved

# Call immediately without saving
print((lambda x: x * 2)(6))           # 12