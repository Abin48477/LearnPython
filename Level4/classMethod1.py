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
#__str__() method:
# it controls what is returned when the object is printed.

class Person2:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1= Person2("abin", 54)
print(p1.name)
print(p1)

# without__str__method
class Person3:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    # def __str__(self):
    #     return f"{self.name} ({self.age})"

p3= Person3("abinram", 540)
print(p3)#<__main__.Person3 object at 0x000002AF8C8469D0>
