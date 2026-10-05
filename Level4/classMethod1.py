# class Method
class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("abin")
p1.greet()

# # Methods With Parameters

class Calculator:
    def add(self, a,b):
        return a+b
    def multiply(self,a , b):
        return a*b
calc = Calculator()
print(calc.add(5,60))
print(calc.multiply(4,50))

# Method Accessing Properties
# method can access and modify object properties using self

# method modifying properties
class Student:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"happy birthday! you are now {self.age}")

s1 = Student("pradip", 25)
s1.celebrate_birthday()
s1.celebrate_birthday()
#
        

    