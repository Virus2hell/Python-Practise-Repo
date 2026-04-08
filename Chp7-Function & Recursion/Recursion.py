# Recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.
# Example of a recursive function to calculate the factorial of a number

def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

n = int(input("Enter a number to calculate its factorial: "))
result = factorial(n)
print(f"The factorial of {n} is {result}")