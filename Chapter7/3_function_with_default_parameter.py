#Now we will see how to define a function with default parameter in python.


def greet1(name="Guest"):                   #here the name is the parameter which has default vaule 'guest'.
    print(f"Hello, {name}. Good Morning!")

greet1()           #if there is no user name defined then it automatically gets 'Guest' and reusult is "Hello, Guest. Good Morning"
greet1("Alice")    #while in this case it says "Hello, Alice. Good Morning"
greet1("Bob")      #while in this case it says "Hello, Bob. Good Morning"
greet1("Charlie")  #while in this case it says "Hello, Charlie. Good Morning"
print()            #it adds single blank line after result 
print("\n")        #2 black lines after result        



#pr2
def dialaoge(name, ending= "Some Work"):
    print(f"How u doing? {name}.")
    print(ending)

dialaoge("Thomas", "Nothing")   #here we use parameterised parameter 'Nothing'
print()                         #blank line
dialaoge("Quill")               #so here we use default parameter 'some work' "