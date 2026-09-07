# write program to print directory of os module

import os

for item in os.listdir():
    print(item)

for item in os.listdir("C:\\Users\\fragr\\OneDrive\\Desktop"):   #print specified path 
    print(item)    