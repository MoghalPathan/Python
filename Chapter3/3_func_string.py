s = " Naved Moghal Pathan "

print(len(s)) #len() function is used to find the length of the string.

print(s.upper()) #upper() function is used to convert the string into uppercase.
print(s.lower()) #lower() function is used to convert the string into lowercase.

print(s.strip()) #strip() function is used to remove the leading and trailing spaces from the string.

print(s.replace("Moghal Pathan", "Korabu")) #replace() function is used to replace a substring with another substring.

print(s.split(" ")) #split() function is used to split the string into a list of substrings based on the specified delimiter.

print(s.find("Moghal")) #find() function is used to find the index of the first occurrence of a substring in the string.

print(s.index("Nav")) #index() function is used to find the index of the first occurrence of a substring in the string. It raises a ValueError if the substring is not found.

print(s.count("a")) #count() function is used to count the number of occurrences of a substring in the string.

print(s.startswith(" Naved")) #startswith() function is used to check if the string starts with the specified substring. It returns True or False.

print(s.endswith("Pathan ")) #endswith() function is used to check if the string ends with the specified substring. It returns True or False.

print(s.isalpha()) #isalpha() function is used to check if all the characters in the string are alphabetic. It returns True or False.

print(s.isdigit()) #isdigit() function is used to check if all the characters in the string are digits. It returns True or False.

print(s.isalnum()) #isalnum() function is used to check if all the characters in the string are alphanumeric (letters and numbers). It returns True or False.