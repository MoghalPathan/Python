'''
write a program to calculate biggest number amonf 4,
take value from the user.
'''

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))

if(n1>n2 and n1>n3 and n1>n4):
    print("n1 is the greater number.", n1)

elif(n2>n1 and n2>n3 and n2>n4):
    print("n2 is the greater number.", n2)

elif(n3>n1 and n3>n2 and n3>n4):
    print("n3 is the greater number.", n3)

else:
    print("n4 is the greater number.", n4)

    