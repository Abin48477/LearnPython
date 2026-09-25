class Dog:
    species = "French Bulldog" #class attribute

    def __init__(self, name):
        self.name = name #Instance attribute

    def bark(self):
        return f"{self.name} says woof woof!"
print(Dog.species) #French Bulldog

jack = Dog("Jack")
jill = Dog("Jill")

print(jack.bark())#jack says woof woof!
print(jill.bark())#jill says woof woof!

# Note that you can access class attributes directly 
# from the class itself, but you need to create an 
# object and pass it data first before you can access 
# instance attributes.

# Class attribute → shared by all objects.
# Instance attribute → different for each object.