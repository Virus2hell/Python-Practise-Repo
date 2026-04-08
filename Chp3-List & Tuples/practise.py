name = list(input("Enter a list of items separated by commas: ").split(","))
sortedList = sorted(name) # This will sort the list in alphabetical order
print("Sorted list:", sortedList)


n = list(int(x) for x in input("Enter a list of numbers separated by commas: ").split(","))
n.sort() # This will sort the list in ascending order
print("Sorted list:", n)


zero = (1,0,1,0,0,0,0,1,0)

print(zero.count(0)) # This will count the number of occurrences of 0 in the tuple