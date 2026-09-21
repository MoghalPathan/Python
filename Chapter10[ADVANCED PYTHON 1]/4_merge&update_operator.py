#Dictionary merge and update operators (Python 3.9+)

d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}



#Merge operator | creates a NEW dictionary:
merged = d1 | d2
print(merged)   # {'a': 1, 'b': 20, 'c': 3}

#If the same key is in both, the right side wins (b became 20).




#Update operator |= changes the left dictionary in place:
d1 |= d2
print(d1)       # {'a': 1, 'b': 20, 'c': 3}

#This is the same as d1.update(d2).


#Old ways (for comparison):
merged = {**d1, **d2}    # unpacking
d1.update(d2)            # update method
