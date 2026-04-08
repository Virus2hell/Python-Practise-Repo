# Classes
# A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. An object is an instance of a class, and it can
# have its own unique values for the attributes defined in the class. Classes are used to create reusable code and to model real-world entities in a program.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30)
person1.greet() # This will call the greet method of the person1 object and print "Hello, my name is Alice and I am 30 years old."