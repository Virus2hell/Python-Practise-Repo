# String Functions
# 1. len() - returns the length of the string
name = "Atharva"
length = len(name)
print(length)

# 2. upper() - converts the string to uppercase
name = "Atharva"
upper_name = name.upper()
print(upper_name)

# 3. lower() - converts the string to lowercase
name = "Atharva"
lower_name = name.lower()
print(lower_name)

# 4. strip() - removes leading and trailing whitespace from the string
name = "   Atharva   "
stripped_name = name.strip()
print(stripped_name)

# 5. replace() - replaces a specified substring with another substring
name = "Atharva"
new_name = name.replace("A", "E")
print(new_name)

# 6. split() - splits the string into a list of substrings based on a specified delimiter
sentence = "Hello World"
words = sentence.split(" ")  # splitting the sentence into words based on space
print(words)

# 7. join() - joins a list of strings into a single string with a specified delimiter
words = ["Hello", "World"]
sentence = " ".join(words)  # joining the words into a sentence with space as a delimiter
print(sentence)

# 8. find() - returns the index of the first occurrence of a specified substring, or -1 if the substring is not found
name = "Atharva"
index = name.find("h")  # finding the index of the first occurrence of "h"
print(index)

# 9. count() - returns the number of occurrences of a specified substring in the string
name = "Atharva"
count = name.count("a")  # counting the number of occurrences of "a"
print(count)

# 10. isalpha() - returns True if all characters in the string are alphabetic, and False otherwise
name = "Atharva"
is_alpha = name.isalpha()  # checking if all characters in the string are alphabetic
print(is_alpha)

# 11. isdigit() - returns True if all characters in the string are digits, and False otherwise
number = "12345"
is_digit = number.isdigit()  # checking if all characters in the string are digits
print(is_digit)

# 12. isspace() - returns True if all characters in the string are whitespace, and False otherwise
whitespace = "   "
is_space = whitespace.isspace()  # checking if all characters in the string are whitespace
print(is_space)

# 13. startswith() - returns True if the string starts with a specified substring, and False otherwise
name = "Atharva"
starts_with_a = name.startswith("Ath")  # checking if the string starts with "Ath"
print(starts_with_a)

# 14. endswith() - returns True if the string ends with a specified substring, and False otherwise
name = "Atharva"
ends_with_va = name.endswith("va")  # checking if the string ends with "va"
print(ends_with_va)


