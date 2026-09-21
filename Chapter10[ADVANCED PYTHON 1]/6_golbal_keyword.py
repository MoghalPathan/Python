#global keyword is a variable made outside a function can be read inside it, 
# but if you try to change it, Python creates a new local variable instead.


counter = 0

def without_global():
    counter = 100            # creates a NEW local variable
    print("Inside:", counter)

without_global()             # Inside: 100
print(counter)               # 0  (outer variable unchanged)

#Fix with global:
counter = 0

def increase():
    global counter           # "use the outer variable"
    counter += 1

increase()
increase()
print(counter)               # 2

#Tip: use global rarely. Too many globals make code hard to debug. 
#Passing values as parameters and returning results is usually better.

