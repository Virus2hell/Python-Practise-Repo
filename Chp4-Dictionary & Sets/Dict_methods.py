# Dictionary Methods
dictionary = {
    "key": "value",
    "name": "Atharva",
    "age": 21,
    "city": "Pune"
}

print(dictionary["name"])  # This will print the value associated with the key "name" in the dictionary, which is "Atharva"

# 1. get() method
print(dictionary.get("name"))  # This will also print the value associated with the key "name" in the dictionary, which is "Atharva"
print(dictionary.get("country", "Not Found"))  # This will print "Not Found" because the key "country" is not present in the dictionary.

# 2. keys() method
print(dictionary.keys())  # This will print a view object that displays a list of all the keys in the dictionary.

# 3. values() method
print(dictionary.values())  # This will print a view object that displays a list of all the values in the dictionary.

# 4. items() method
print(dictionary.items())  # This will print a view object that displays a list of all the key-value pairs in the dictionary as tuples.

# 5. pop() method
popped_value = dictionary.pop("age")  # This will remove the key "age" and its associated value from the dictionary and return the value, which is 21
print(popped_value)  # This will print the popped value, which is 21
print(dictionary)  # This will print the updated dictionary after popping the key "age".
