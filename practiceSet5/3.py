'''
a spam message is defined as text containing followinf keywords "by now", "click this",
"subscribe this","make a lot of money". Write a program to detect this spams. 
USING 'if' KEYWORD.
'''

p1 = "buy now"
p2 = "click this"
p3 = "subscribe this"
p4 = "make a lot of money"

msg = input("Enter your message: ")

if (p1 in msg or p2 in msg or p3 in msg or p4 in msg):
    print("this is a spam message.")

else:
    print("this is not spam message.")    