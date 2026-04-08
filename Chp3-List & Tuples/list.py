items = ["apple", "banana", "cherry", 67, True, 69.69]

for i in items:
    print(i)

items[0] = "grape" # This will change the first item in the list from "apple" to "grape"
print(items[0])  # List are mutable, so we can change the value of an item in the list by assigning a new value to it using its index.