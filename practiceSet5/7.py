'''
write a program to find out given post is talking about "Naved" or not.
'''

post = input("Enter the post: ")

if ("Naved".lower() in post.lower()):
    print("Naved is in the post.")

else:
    print("Naved is not in post.")    