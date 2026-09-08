# write a program to read the text from given file "poem.txt" 
# and find out whether it contains twinklw word init.

f = open("poem.txt")

data = f.read()
print(data)

if ("twinkle" in data):
    print("Yes, 'twinkle' is present in the file.") 

f.close()