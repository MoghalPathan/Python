"""
4. format() method
What it does: puts values inside a string at {} placeholders.

"""


name = "Naved"
age = 22

# Empty placeholders: filled in order
print("My name is {} and I am {}".format(name, age))

# With index numbers
print("{1} is {0} years old".format(age, name))

# With names (easiest to read)
print("{n} is {a} years old".format(n=name, a=age))





"""
o. Formatting numbers:

python
pi = 3.14159265

print("{:.2f}".format(pi))        # 3.14   (2 decimal places)
print("{:10}".format("Hi"))       # "Hi        " (width 10, left aligned)
print("{:>10}".format("Hi"))      # "        Hi" (right aligned)
print("{:^10}".format("Hi"))      # "    Hi    " (centered)
print("{:,}".format(1000000))     # 1,000,000
print("{:b}".format(10))          # 1010 (binary)
"""



"""
o. Modern alternative: f-strings (recommended). They do the same job with less typing:

python
print(f"My name is {name} and I am {age}")
print(f"{pi:.2f}")            # 3.14
print(f"{1000000:,}")         # 1,000,000
print(f"{age + 1}")           # 23 (you can even calculate inside)
"""