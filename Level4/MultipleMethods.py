class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)
        print(f"{song} is Added")

    def remove_song(self, song):
        self.songs.remove(song)
        print(f"{song} is removed.")

    def show_song(self):
        print(f"Playlist '{self.name}")
        for song in self.songs:
            print(f"- {song}")

p1 = Playlist("my_fevbrate")
p1.add_song("hare krishna song")
p1.add_song("kritan mela")
del Playlist.remove_song
p1.show_song()
# p1.remove_song("kritan mela")

# delete methods
# using the del keyword
# __str__() method must retrun the string 
# class Person:
    # def __init__(self,age):
        # self.age = age
    # def __str__(self):
    #     return self.age

# p1 = Person(45)
# print(p1)
#MultipleMethods.py", line 36, in <module>
# print(p1)
# TypeError: __str__ returned non-string (type int)



# the __repr__() method 
# use this method to describe the object 
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name!r},{self.age})"
p1 = Person("ramRam",455)
print(p1)
# define both method and comparision
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

  def __repr__(self):
    return f"Person(name={self.name!r}, age={self.age})"

p1 = Person("Emil", 36)

print(p1)
print(repr(p1))

# One simple memory trick 🧠
# str = "Tell me nicely what this object is."
# repr = "Show me exactly what this object is for debugging."

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self,other):
       return self.name == other.name and self.age == other.age

p1 = Person1("Linus", 30)
p2 = Person1("Linus", 30)

print(p1 == p2)
# true
# witout eq method object will not be equal even the valuei is equal
# Add a __eq__() method that defines that two objects are equal if the values are equal:

# 🧠 Remember:
# Without __eq__() → "Are you the same object?"
# With __eq__() → "Do you have the same data?"
class Person12:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def __add__(self,other):
      return self.age + other.age

p1 = Person12("Emil", 22)
p2 = Person12("abin",45)

print(p1 + p2)
# Note: Without __add__(), writing p1 + p2 would raise a TypeError, since Python would not know how to add two Person objects.

# The__len__() Method
# The __len__() method controls what the built-in len() function returns for your object.
class Company1:
    def __init__(self,employees):
        self.employee = employees
    def __len__(self):
        return len(self.employee)
c1 = Company1(["abin","ram","sita","python"])
print(len(c1))

# Note: Without __len__(), calling len(c1) would raise a TypeError, since Python would not know what "length" means for a Company.

# __lt__()method
# The __lt__() method ("less than") controls what the < operator does for your own objects.

class Family:
    def __init__(self,name,age):
      self.name = name
      self.age = age
# Remove __lt__(), and the comparison fails:

    def __lt__(self,other):
      return self.age < other.age

f1 = Family("kishor",23)
f2 = Family("ishor",20)
print(f1 < f2)
# TypeError:

# Sorting with __lt__()
class Subject:
    def __init__(self, name, age):
       self.name = name
       self.age = age
# without __lt__method  x = sorted([s1,s2,s3])
        # ^^^^^^^^^^^^^^^^^^
# TypeError: '<' not supported between instances of 'Subject' and 'Subject'
    def __lt__(self,other):
       return self.age < other.age
    
s1 = Subject("o",64)
s2 = Subject("hlo",14)
s3 = Subject("hello",4)

x = sorted([s1,s2,s3])
for xi in x:
    print(xi.name, xi.age)

# the __contains__() method

# the __contains__() method controls what the in operator checks for your own objects. 
#  check if  an employee is in a  abcCpmpany
class AbcCompany:
    def __init__(self,employees):
       self.employees = employees

    def __contains__(self, name):
        return name in self.employees

c1 = AbcCompany(["ram","hare","hari","krishna"])
print("krishna" in c1)#true 
print("gopal" in c1)#false

# python __call__() mehod

# the __call__() method lets an object be called like a function, using object() syntax.


class Dog:
    def __init__(name, age):
        self.name = name
        self.age = age

dog = Dog("Pinky", 3)
print(dog.name)