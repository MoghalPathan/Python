# a file contains word "donkey" multiple times. 
# you need to write a program which replace this word with ##### by updating same file.

word = "donkey"

with open("file.txt","r") as f:
    content = f.read()


contentNew = content.replace("donkey", "######")

with open("file.txt", "w") as f:
    f.write(contentNew)