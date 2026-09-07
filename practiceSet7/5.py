#write a program to print n lines of the following pattern.  for n = 3

"""

***
**
*

"""

def pattern(n):
    if(n == 0):
        return
    print("*"* n)
    pattern(n-1)

pattern(3)