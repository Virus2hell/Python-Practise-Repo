d = {} # This will create an empty dictionary and assign it to the variable d
print(d) # This will print the empty dictionary, which is {}

dictionary = {
    "key": "value",
    "name": "Atharva",
    "age": 21,
    "city": "Pune"
}

print(dictionary["name"])  # This will print the value associated with the key "name" in the dictionary, which is "Atharva"
dictionary["name"] = "Mihir"  # This will change the value associated with the key "name" in the dictionary from "Atharva" to "Mihir"
print(dictionary["name"])  # This will print the updated value associated with the key "name" in the dictionary, which is now "Mihir"

# Dictionary property is mutable, so we can change the value of a key in the dictionary by assigning a new value to it using its key.