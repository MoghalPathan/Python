#write a program to find greatest of threee numbers.

def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

    
a = 1
b = 3
c = 4

print(greatest(a,b,c))