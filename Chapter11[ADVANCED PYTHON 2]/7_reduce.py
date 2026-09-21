#it combines all items of a list into ONE single value by applying a function step by step.

#this must be imported first:  'from functools import reduce'

#Syntax:  'reduce(function, iterable)'




from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# Square the even numbers, then add them all
even = filter(lambda x: x % 2 == 0, nums)        # 2, 4, 6
squared = map(lambda x: x * x, even)             # 4, 16, 36
total = reduce(lambda a, b: a + b, squared)      # 56
print(total)                                     # 56