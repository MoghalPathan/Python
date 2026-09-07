s = {1,2,3,4,5,6,7,8}
s1 = {8,9,10,11,12,13,14}

#add and remove method
s.add(100)
print(s)

s.remove(1)
print(s)

s.pop()
print(s)

s.copy()
print(s)

s.discard(8)
print(s)

s.update([23,45,67])
print(s)

s.clear()
print(s)

#set operations
s = {1,3,4,5,6,7,8,9,12,34,56,678,34,567,6}  # new set

print(s.union(s1))
print(s.intersection(s1))
print(s.difference(s1))
print(s.symmetric_difference(s1))

#comparisons check if valuse exist or not
print(s.issubset({1,3,4,5,6}))
print(s.issuperset({2,4,6,7}))
print(s.isdisjoint({3,5,10}))
