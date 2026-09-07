#write a program, to acceptmark
# of 6 students and display in asecending order
mark = []

f1 =int(input("Enter 1st student mark: "))
mark.append(f1)

f2 =int(input("Enter 2nd student mark: "))
mark.append(f2)

f3 =int(input("Enter 3rd student mark: "))
mark.append(f3)

f4 =int(input("Enter 4th student mark: "))
mark.append(f4)

f5 =int(input("Enter 5th student mark: "))
mark.append(f5)

f6 =int(input("Enter 6th student mark: "))
mark.append(f6)


print("Accepted markes: ", mark)

mark.sort()
print("Markes of students in Ascending order: ", mark)
