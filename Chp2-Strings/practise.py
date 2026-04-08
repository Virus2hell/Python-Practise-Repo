n = input("Enter your name: ")
print(n + " Good Afternoon!")


name = input("Enter your name: ")
position = input("Enter the position you are applying for: ")
letter = '''
Dear {name},
You are selected for the position of {position} in our company.
Please let us know if you are interested in this opportunity.'''.format(name=name, position=position)

print(letter)