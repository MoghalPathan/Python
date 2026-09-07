'''
l = [23, 1, 67, 89, 9, 45, 67, 3, 4, 5, 2, 11, 23, 11]

l.append(56)
print(l)          # [23, 1, 67, 89, 9, 45, 67, 3, 4, 5, 2, 11, 23, 11, 56]

l.sort()
print(l)          # [1, 2, 3, 4, 5, 9, 11, 11, 23, 23, 45, 56, 67, 67, 89]

l.reverse()
print(l)          # [89, 67, 67, 56, 45, 23, 23, 11, 11, 9, 5, 4, 3, 2, 1]

l.sort()
print(l)          # back to ascending order

l.insert(0, 100)       # insert 100 at index 0
print(l)

l.extend([200, 300])   # add multiple items
print(l)

l.remove(11)           # removes first occurrence of 11
print(l)

idx = l.index(56)     # capture the returned index
print(idx)             # 11

cnt = l.count(11)      # count() on element that exists (5 was removed earlier example, use 11)
print(cnt)             # 2

l2 = l.copy()          # capture the returned copy
print(l2)              # a new list, same contents as l

l.remove(11)           # removes first occurrence of 11
print(l)

popped = l.pop()       # removes and returns last item
print(popped, l)

l.clear()               # empties the list
print(l)                # []
'''

l = [1,5,8,4,2,7,9,90,90,78,56,99,23,1.3,1.5]

l.append(10)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

l.insert(1,100)
print(l)

l.extend([101])   
print(l)

l.remove(101)
print(l)

ind = l.index(100)
print(ind)

ct = l.count(90)
print(ct)

cpy = l.copy()
print(cpy)

popp = l.pop()
print(popp, l)

clr = l.clear()
print(clr)