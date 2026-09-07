#write a program to convert celcius into fernihight

"""c/5 = f-32/9    i.e.  c = 5*(f-32)/9   ....... formula to convert"""


def convert(n):
    return 5*(n-32)/9 


n = int(input("enter a number: "))    
print(convert(n))