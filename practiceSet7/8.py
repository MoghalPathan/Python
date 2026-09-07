#write a program to print multipluication table of the given number

def table(n):
    for i in range(1,11):
        print(f"{i} * {n} = {i*n}")

n = int(input("Enter a number: "))
table(n)
    