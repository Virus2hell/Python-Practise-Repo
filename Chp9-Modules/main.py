import my_modules
from my_modules import calculateSalary

print(my_modules.skill_list) # This will print the skill_list defined in my_modules.py

my_modules.displaySkills("Python") # This will call the displaySkills function defined in my_modules.py and pass the argument "Python" to it. The function will print "this is your favorite skill: Python"

calculateSalary() # This will call the calculateSalary function defined in my_modules.py