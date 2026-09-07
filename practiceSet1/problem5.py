# label problem4

import os    #fetch resources from os module

for item in os.listdir():    #gives you a list of everything (files + folders) inside a directory.  
    print(item)              #print the directory of the current working directory

for item in os.listdir("C:\\Users\\fragr\\OneDrive\\Desktop"):   #print specified path 
    print(item)    