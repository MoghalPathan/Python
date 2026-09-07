'''
write a program to calculate grade of student from the following scheme:
90 - 100 _ O
80 - 90  _ A
70 - 80  _ B
60 - 70  _ C
50 - 60  _ D
< 50     _ F
'''

grade = int(input("Enter your Grade: "))

if (grade in range(90, 100)):
    print("O")

elif(grade in range(80, 90)):
    print("A")

elif(grade in range(70, 80)):
    print("B")

elif(grade in range(60, 70)):
    print("C")    

elif(grade in range(50, 60)):
    print("D")

else:
    print("FAIL")