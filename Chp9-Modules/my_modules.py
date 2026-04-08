skill_list = ["Python", "JavaScript", "Java", "C++"]

def displaySkills(skills):
    print(f"this is your favorite skill: {skills}")

def calculateSalary():
    baseSalary = int(input("Enter base salary: "))
    bonus = float(input("Enter bonus percentage (as a decimal): "))
    totalSalary = baseSalary * (1 + bonus)
    print("The total salary is: ", totalSalary)