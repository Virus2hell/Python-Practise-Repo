# list methods
# 1. append() - adds an item to the end of the list
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)

# 2. insert() - adds an item at a specified index in the list
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "date")
print(fruits)

# 3. remove() - removes the first occurrence of a specified item from the list
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)

# 4. pop() - removes and returns the item at a specified index in the list (or the last item if no index is specified)
fruits = ["apple", "banana", "cherry"]
popped_item = fruits.pop(1)  # removes and returns the item at index 1 (which is "banana")
print(popped_item)

# 5. clear() - removes all items from the list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

# 6. index() - returns the index of the first occurrence of a specified item in the list
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")  # returns the index of the first occurrence of "banana
print(index)

# 7. count() - returns the number of occurrences of a specified item in the list
fruits = ["apple", "banana", "cherry", "banana"]
count = fruits.count("banana")  # counts the number of occurrences of "banana"
print(count)

# 8. sort() - sorts the items in the list in ascending order
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # sorts the numbers in ascending order
print(numbers)

# 9. reverse() - reverses the order of the items in the list
fruits = ["apple", "banana", "cherry"]
fruits.reverse()  # reverses the order of the items in the list
print(fruits)

# 10. copy() - returns a shallow copy of the list
fruits = ["apple", "banana", "cherry"]
fruits_copy = fruits.copy()  # creates a shallow copy of the list
print(fruits_copy)

