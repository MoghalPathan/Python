#repeat program 4 for list of such words to be censored# a file contains word "donkey" multiple times. 
# you need to write a program which replace this word with ##### by updating same file.

words = ["donkey", "bad", "ganda"]

with open("file.txt","r") as f:
    content = f.read()


for word in words:
    content = content.replace(word, "#" * len(word))

with open("file.txt", "w") as f:
    f.write(content)