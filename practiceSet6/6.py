#write a program to find factorial  of a given number   5!=1X2X3X4X5

n = int(input("Enter a number :"))
product = 1
for i in range(1,n+1):
    product = product * i

print(f"the factorian of {n} is {product}")    

