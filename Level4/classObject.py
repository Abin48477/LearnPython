class Student:
    def __init__(self,name ,age):
        self.name = name
        self.age = age

student1 = Student("Abin", 20)
student2 = Student("Ram", 24)

print(student1.name)
print(student1.age)

print(student2.name)
print (student2.age)

# Class → blueprint

# Object → actual thing made from blueprint

# Attribute → data belonging to an object

# Method → function belonging to a class/object

# self → the current object

# __init__() → runs when you create an object and usually sets its initial data.