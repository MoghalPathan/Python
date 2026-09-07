#write a python function to remove a given word from a list add strip it at the same time.

l = ["this", "is", "a", "list", "of", "words", "to", "remove"]

def remove_word(word):
    l.remove(word)
    return [w.strip() for w in l]

print(remove_word("this"))
