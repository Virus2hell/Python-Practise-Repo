# Sets methods
# 1. add() - adds an item to the set
s = {1, 2, 3}
s.add(4)
print(s)

# 2. remove() - removes a specified item from the set. If the item is not found, it raises a KeyError.
s = {1, 2, 3}
s.remove(2)
print(s)

# 3. discard() - removes a specified item from the set. If the item is not found, it does nothing (no error is raised).
s = {1, 2, 3}
s.discard(2)
print(s)

# 4. pop() - removes and returns an arbitrary item from the set. If the set is empty, it raises a KeyError.
s = {1, 2, 3}
popped_item = s.pop()
print(popped_item)
print(s)

# 5. clear() - removes all items from the set
s = {1, 2, 3}
s.clear()
print(s)

# 6. union() - returns a new set that is the union of two sets (i.e., it contains all the unique items from both sets)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

# 7. intersection() - returns a new set that is the intersection of two sets (i.e., it contains only the items that are present in both sets)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.intersection(s2)
print(s3)

# 8. difference() - returns a new set that is the difference of two sets (i.e., it contains only the items that are present in the first set but not in the second set)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.difference(s2)
print(s3)

# 9. symmetric_difference() - returns a new set that is the symmetric difference of two sets (i.e., it contains only the items that are present in either set but not in both sets)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.symmetric_difference(s2)
print(s3)

# 10. issubset() - returns True if the set is a subset of another set (i.e., all items in the set are also present in the other set), otherwise it returns False
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1.issubset(s2))  # True because all items in s1 are also present in s2
print(s2.issubset(s1))  # False because not all items in s2 are present in s1

# 11. issuperset() - returns True if the set is a superset of another set (i.e., all items in the other set are also present in the set), otherwise it returns False
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1.issuperset(s2))  # True because all items in s2 are also present in s1
print(s2.issuperset(s1))  # False because not all items in s1 are present in s2

