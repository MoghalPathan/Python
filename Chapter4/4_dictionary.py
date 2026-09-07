d = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six"}

print(d.get(1))  #prints one element at a time
print(d.get(6,"six"))

d.update({6: "six"})  #adds element
print(d)

d.setdefault(7, "seven")   #adds elemets
print(d)

po = d.pop(3)  #removes specific item
print(po, d)

poe = d.popitem()  #delete last item
print(poe, d)

for k, v in d.items():   # prints all elemts in vertical format
    print(k, v)

