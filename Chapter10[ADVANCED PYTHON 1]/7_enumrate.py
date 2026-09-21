#enumerate() gives the index and the value together while looping.

#Without enumerate (ugly):
fruits = ["apple", "banana", "mango"]
i = 0
for fruit in fruits:
    print(i, fruit)
    i += 1



#With enumerate (clean):
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 mango



# Start counting from 1:
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. mango
