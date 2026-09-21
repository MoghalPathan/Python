#now we will see how to define a function with nested function in python.
def outer_function(x):
    def inner_function(y):
        return y * y
    return inner_function(x) + 1

print(outer_function(5))
print("\n")