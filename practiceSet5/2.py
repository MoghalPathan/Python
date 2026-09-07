'''
write a program to check whether student passed or failed in the exam, 
if it requires total of 42% and aleast 33% in each subject to pass, 
assume 3 subjects. take values from the user
'''
s1 = int(input("Enter markes of subject 1 : "))
s2 = int(input("Enter markes of subject 2 : "))
s3 = int(input("Enter markes of subject 3 : "))

sum = s1+s2+s3

if (sum%100>=42):
    print("PASS") 

else:
    print("FAIL")     

if (s1%100>=33):
    print("pass in sub 1.")

else:
    print("failed in sub 1")     

if (s2%100>=33):
    print("pass in sub 2.")

else:
    print("failed in sub 2")     

if (s3%100>=33):
    print("pass in sub 3.")

else:
    print("failed in sub 3")   

 
