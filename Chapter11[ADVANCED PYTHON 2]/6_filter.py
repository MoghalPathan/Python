#it keeps only the items for which the function returns True.

#Syntax:   filter(function, iterable)

nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)                # [2, 4, 6, 8]

# Keep numbers greater than 5
print(list(filter(lambda x: x > 5, nums)))   # [6, 7, 8]

# Keep long words
words = ["hi", "python", "code", "programming"]
print(list(filter(lambda w: len(w) > 4, words)))   # ['python', 'programming']


"""
Difference between map and filter:
    ______________________________________________________________________
	|          | Function's job                    |    Result size       |         
    |__________|___________________________________|______________________|             
    |    map   |     changes each item             | same number of items |                  
    |__________|___________________________________|______________________|
    |  filter  | decides keep or drop (True/False) |   same or fewer items|                
    |_________ |___________________________________|______________________|
"""
