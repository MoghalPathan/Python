#write a progtram to reame a file to "renamed_by python.txt".


with open("old.txt") as f:
    content = f.read()

with open("renambed_by_python.txt") as f:
    f.write(content)    