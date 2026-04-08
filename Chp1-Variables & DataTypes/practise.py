a = input("Enter a number: ")
b = input("Enter another number: ")
a = int(a)
b = int(b)
print("The sum of the two numbers is", a + b)  # This will concatenate the two strings instead of adding them


dividend = input("Enter a dividend: ")
divisor = input("Enter a divisor: ")
dividend = int(dividend)
divisor = int(divisor)
print("The remainder of the division is", dividend % divisor)  # This will raise a TypeError because we cannot divide strings


typeOfNum = input("enter the value to get its type: ")
print(type(typeOfNum))


c = 34
d = 80
if(c > d):
    print(True)
else:
    print(False)


e = int(input("Enter a number: "))
f = int(input("Enter another number: "))
average = (e + f) / 2
print("The average of the two numbers is", average)


