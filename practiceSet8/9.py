#write a programto find out whether a file is identicala and matches the content of another file.

with open("file1.txt") as f:
    content1 = f.read()

with open("file2.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("conents are same, both are identical.")  
else:
    print("nno...")      