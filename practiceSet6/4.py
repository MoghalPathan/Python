#write a program to find given number is prime or not

n = int(input("enter a number: "))

for i in range(2,n):
    if(n%i)==0:
        print("its not a prime number")
        break

else:
    print("its a prime number")


