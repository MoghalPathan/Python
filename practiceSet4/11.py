'''
create a empty dictionary. alllow 4 freiends to enter their favouritre language and
their name as key value along side with it. 
Assume that names are unique
'''

d = {}

name = input("Enter name: ")
lang = input("Enter favourite language: ")
d.update({name: lang})

name = input("Enter name: ")
lang = input("Enter favourite language: ")
d.update({name: lang})

name = input("Enter name: ")
lang = input("Enter favourite language: ")
d.update({name: lang})

name = input("Enter name: ")
lang = input("Enter favourite language: ")
d.update({name: lang})

print(d)