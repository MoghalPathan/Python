#write a program to create a dictionary of turkish words with values as therir english translation. 
# Provide user with an option to look it up!

dictionary = {
    "yewet" : "yes",
    "neya"  : "what do u want",
    "nasilson" : "what"
}

word = input("Enter a word whose translation u required: ")

print("translation: ",dictionary[word])