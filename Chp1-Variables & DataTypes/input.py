# input function is used to take input from the user
# it always returns a string
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Your name is", name)
print("Your age is", age)

# if we want to take input as a number, we need to convert the string to an integer or float
age = input("Enter your age: ")
age = int(age)  # converting string to integer
ageWithMonth = input("Enter your age with month: ")
ageWithMonth = float(ageWithMonth)  # converting string to float
print("Your age is", age)
print("Your age with month is", ageWithMonth)