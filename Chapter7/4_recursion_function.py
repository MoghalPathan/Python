#Now we will see how to define a recursive function in python.

"""
factorial(1) = 1
factorial(2) = 1x2
factorial(3) = 1x2x3
factorial(4) = 1x2x3x4
factorial(5) = 1x2x3x4x5

factorial(n) = n * factorial(n-1)    .........formula
"""


n = int(input("Enter a number to find its factorial: "))

def factorial(n):
    if(n == 0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(f"the factorial of {n} is {factorial(n)}")
print("\n") 