# tuple methods
# 1. count() - returns the number of occurrences of a specified item in the tuple
items = ("apple", "banana", "cherry", "banana")
count = items.count("banana")  # counts the number of occurrences of "banana"
print(count)

# 2. index() - returns the index of the first occurrence of a specified item in the tuple
items = ("apple", "banana", "cherry")
index = items.index("banana")  # returns the index of the first occurrence of "banana
print(index)

# 3. len() - returns the number of items in the tuple
items = ("apple", "banana", "cherry")
length = len(items)  # returns the number of items in the tuple
print(length)

# 4. unpacking - allows you to assign the items in a tuple to individual variables
items = ("apple", "banana", "cherry")
fruit1, fruit2, fruit3 = items  # unpacking the items in the tuple into individual variables
print(fruit1, fruit2, fruit3)