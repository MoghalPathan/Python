#repeat program 4 for list of such words to be censored# a file contains word "donkey" multiple times. 
# you need to write a program which replace this word with ##### by updating same file.

words = "donkey"

with open("file.txt","r") as f:
    content = f.read()


contentNew = content.replace("donkey", "######")

with open("file.txt", "w") as f:
    f.write(contentNew)