# Function is a block of code that performs a specific task. It is a reusable piece of code that can be called multiple times in a program. Functions are defined using the def keyword, followed by the function name and parentheses. The code inside the function is indented.

# Function definition
def avg():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    average = (a + b + c) / 3
    print("The average of the three numbers is: ", average)

avg() # This will call the avg function and execute the code inside it. We can call the function multiple times to calculate the average of different sets of numbers.

def goodDay(name):
    print("Have a good day! " + name)
    # return "ok"

goodDay("Atharva") # This will call the goodDay function and pass the argument "Atharva" to it. The function will print "Have a good day! Atharva"
a = goodDay("Vedant") # This will call the goodDay function and pass the argument "Vedant" to it. The function will print "Have a good day! Vedant" and return "ok". The returned value will be stored in the variable a.
print(a) # This will print the value of a, which is "ok"

# Default parameter value
def greet(name="Guest"):
    print("Hello, " + name + "!")

greet() # This will call the greet function without passing any argument, so it will use the default parameter value "Guest" and print "Hello, Guest!"
greet("Atharva") # This will call the greet function and pass the argument "Atharva" to it, so it will print "Hello, Atharva!"

def calculateSalary(base_salary, bonus):
    total_salary = base_salary * (1 + bonus)
    return total_salary

base_salary = int(input("Enter base salary: "))
bonus = float(input("Enter bonus percentage (as a decimal): "))
total_salary = calculateSalary(base_salary, bonus)
print("The total salary is: ", total_salary)