# In python we can read and write files using the built-in functions. 
#thre are 2 types of files: 1. Text File(.txt, .c, etc) and 2. Binary Files(.jpg, .dat, etc) 

f = open("example.txt")
data = f.read()
print(data)
f.close()