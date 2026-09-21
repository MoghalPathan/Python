"""
3. join() method
What it does: joins a list (or any iterable) of strings into one string, 
with a separator you choose.

"""




words = ["Python", "is", "fun"]

print(" ".join(words))      # Python is fun
print("-".join(words))      # Python-is-fun
print(", ".join(words))     # Python, is, fun
print("".join(words))       # Pythonisfun



"""
Important: join works only on strings. Numbers cause an error:

python
nums = [1, 2, 3]
# ", ".join(nums)                          # TypeError

print(", ".join(str(n) for n in nums))     # 1, 2, 3  (convert first)
print(", ".join(map(str, nums)))           # same result, using map

"""


"""
Why it's better than a loop with +:

python
# Slow and ugly
result = ""
for w in words:
    result += w + " "

# Clean and fast
result = " ".join(words)
"""