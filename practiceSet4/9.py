'''
what will be the lenght of the following set
s = set()
s.add(10)
s.add(10.0)
s.add('10')
'''

''' its 2 bcoz python counts floatpoint and interger values atre same '''

s = set()
s.add(10)
s.add(10.0)
s.add('10')

print(s)