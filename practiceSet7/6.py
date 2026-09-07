#write a program to convert inches into cms.

""" 1inch = 2.54cm """

def convert(inch):
    return inch*2.54


inch = int(input("enter a number: "))    
print(convert(inch))