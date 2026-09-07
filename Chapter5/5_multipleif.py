''' in a single program there can be multiple if blocks, 
bcoz everyone has different identation and there ending alongside start.'''


n = int(input("Enter a number: "))

if n%2==0:
    print("it's an even number")

if n>=18:
    print("u r eligible")
    print("Good 4 u")

elif n<0:
    print("invalid number, age can't be negative u dumb ass")
    
elif n==0:
    print("invalid number, age can't be zero")

else:
    print("u are not eligible, u'r not an adult")



    