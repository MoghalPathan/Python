#List comprehension is a short way to build a list using a loop in one line.

#Formula:  [expression  for item in iterable  if condition]


# Normal
squares = []
for i in range(1, 6):
    squares.append(i * i)

# Comprehension
squares = [i * i for i in range(1, 6)]
print(squares)      # [1, 4, 9, 16, 25]



#With a condition (filter):
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)        # [2, 4, 6, 8, 10]



#Changing each item:
fruits = ["apple", "banana", "mango"]
print([f.upper() for f in fruits])   # ['APPLE', 'BANANA', 'MANGO']



#If-else inside (goes BEFORE the for):
labels = ["even" if i % 2 == 0 else "odd" for i in range(5)]
print(labels)       # ['even', 'odd', 'even', 'odd', 'even']

# Note: Common mistake: a plain if (filter) goes at the END, but if-else goes at the START.

