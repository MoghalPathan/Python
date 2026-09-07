#write a program to print multiplication table of n usinf loops in reversed order.


n = int(input("Enter a number : "))

for i in range(10, 0, -1):
    print(n, "x", i, "=", n*i)