"""
Walrus operator stores a value in a variable and lets you use that value in the same line.
The name comes from how := looks, like a walrus face with eyes and tusks.
Problem without it: you often calculate something, save it, and then check it in another line.

"""


text = "Hello Naved"

# Normal way: 2 lines
n = len(text)
if n > 5:
    print("Long text, length is", n)

# Walrus way: 1 line
if (n := len(text)) > 5:
    print("Long text, length is", n)

#Here n := len(text) calculates the length, saves it in n, and gives the value back to the if to compare with 5.




#Where it helps most is while loops:
# Keep asking until the user types "quit"
while (word := input("Enter word: ")) != "quit":
    print("You typed:", word)

#Without walrus you would need input() twice, once before the loop and once inside it.

"""
Rules to remember:
Put it in brackets: if (n := 10) > 5.
Don't use it just to look smart. Use it only when it saves a repeated calculation.

"""
