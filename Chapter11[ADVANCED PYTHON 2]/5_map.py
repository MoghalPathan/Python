#map() applies a function to EVERY item of a list and gives back the results.

nums = [1, 2, 3, 4, 5]

# Square every number
squares = list(map(lambda x: x * x, nums))
print(squares)              # [1, 4, 9, 16, 25]

#With a normal function:
def double(x):
    return x * 2

print(list(map(double, nums)))     # [2, 4, 6, 8, 10]

#With built-in functions:
print(list(map(str, nums)))        # ['1', '2', '3', '4', '5']
print(list(map(int, ["1", "2"])))  # [1, 2]

#Two lists at once:
a = [1, 2, 3]
b = [10, 20, 30]
print(list(map(lambda x, y: x + y, a, b)))   # [11, 22, 33]

#Same result with list comprehension:
[x * x for x in nums]