class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
Student1 = Student("Ram",10)
x = "name"
print(getattr(Student1, x))
# Look inside student1, take the attribute whose name is stored in x.