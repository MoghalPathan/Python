'''
python has various operators that are used to perform operations on variables and values. 
Python divides the operators in the following groups: 1.arthmatic operators 2.assignment operators 3.comparison operators 4.logical operators 5.identity operators 6.membership operators 7.bitwise operators

# 1. Arithmetic operators
a = 10
b = 3
print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division (float result)
print(a // b)  # floor division
print(a % b)   # modulus (remainder)
print(a ** b)  # exponent (power)


# 2. Assignment operators
x = 5
x += 2   # x = x + 2
x -= 2   # x = x - 2
x *= 2   # x = x * 2
x /= 2   # x = x / 2
x //= 2  # x = x // 2
x %= 2   # x = x % 2
x **= 2  # x = x ** 2


# 3. Comparison operators
print(a == b)  # equal to
print(a != b)  # not equal to
print(a > b)   # greater than
print(a < b)   # less than
print(a >= b)  # greater than or equal to
print(a <= b)  # less than or equal to


# 4. Logical operators
print(a > 5 and b > 5)   # True if both are true
print(a > 5 or b > 5)    # True if at least one is true
print(not(a > 5))        # reverses the result


# 5. Identity operators
p = [1, 2, 3]
q = [1, 2, 3]
r = p
print(p is r)       # True, same object
print(p is q)       # False, different objects (same content)
print(p is not q)   # True, not same object


# 6. Membership operators
lst = [1, 2, 3, 4]
print(3 in lst)      # True, value found
print(10 not in lst) # True, value not found


# 7. Bitwise operators
m = 6   # 110 in binary
n = 3   # 011 in binary
print(m & n)   # AND
print(m | n)   # OR
print(m ^ n)   # XOR
print(~m)      # NOT (bit invert)
print(m << 1)  # left shift
print(m >> 1)  # right shift
'''


#Arithmatic operators
print("Arithmatic operators")
a = 10
b = 3
c = a + b
print("Addition:", c)

a = 10
b = 3
c = a - b
print("Subtraction:", c)

a = 10
b = 3
c = a * b
print("Multiplication:", c)

a = 10
b = 3
c = a / b
print("Division:", c)

a = 10
b = 3
c = a // b
print("Floor Division:", c)

a = 10
b = 3
c = a % b
print("Modulus:", c)

a = 10
b = 3
c = a ** b
print("Exponent:", c)
print()



#Assignment operators are used to assign values to variables. The most common assignment operator is the equal sign (=), which assigns the value on the right to the variable on the left. There are also compound assignment operators that combine an arithmetic operation with assignment, such as +=, -=, *=, /=, etc.
print("Assignment operators")
a = 5
print("Initial value of a:", a)
a += 2
print("Value of a after addition:", a)
a -= 2
print("Value of a after subtraction:", a)
a *= 2
print("Value of a after multiplication:", a)
a /= 2
print("Value of a after division:", a)
print()



#Comparison operators are used to compare two values.
# They return a boolean value (True or False) based on the comparison.
# The common comparison operators are == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), and <= (less than or equal to).
print("Comparison operators")
a = 2
b = 2
a == b
print( "a is equal to b:", a == b)

a = 2
b = 3
a != b
print("a is not equal to b:", a != b)

a = 5
b = 3
a > b
print("a is greater than b:", a > b)

a = 2
b = 3
a < b
print("a is less than b:", a < b)

a = 5
b = 5
a >= b
print("a is greater than or equal to b:", a >= b)

a = 2
b = 3
a <= b
print("a is less than or equal to b:", a <= b)
print()


#logical operators are used to combine conditional statements.
print("Logical operators")
a = 5
b = 5
print("a and b are both true:", a > 0 and b > 0)
print("a or b is true:", a > 0 or b > 0)
print("not(a > 0):", not(a > 0))
print()

#Identity operators are used to compare the memory locations of two objects.
# The identity operators are is and is not.
print("Identity operators")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a and c are the same object:", a is c)
print("a and b are not the same object:", a is not b)

a = 5
b = 5
print("a and b are the same object:", a is b)
print("a and b are not the same object:", a is not b)
print()



#Membership operators are used to test whether a value is present in a sequence (such as a list, tuple, or string).
print("Membership operators")
a = [1, 2, 3]
print("1 is in a:", 1 in a)
print("4 is not in a:", 4 not in a)
print("2 is in a:", 2 in a)
print("5 is not in a:", 5 not in a)
print()



#Bitwise operators are used to perform bit-level operations on binary numbers. 
print("Bitwise operators")
a = 5   # Binary: 101
b = 3   # Binary: 011
c = a & b   # Binary: 001
print("a & b:", c)   
c = a | b  # Binary: 111
print("a | b:", c)
c = a ^ b  # Binary: 110
print("a ^ b:", c)
c = ~a     #Binary: 010
print("~a:", c)
c = a << 1   #Binary: 1010
print("a << 1:", c)
c = a >> 1   #Binary: 010
print("a >> 1:", c)
print()