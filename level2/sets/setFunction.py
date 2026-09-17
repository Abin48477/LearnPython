# Sets: Sets are built-in data structures in Python that do not allow duplicate values. Sets are mutable and unordered, which means that their elements are not stored in any specific order, so you cannot use indices or keys to access them. Also, sets can only contain values of immutable data types, like numbers, strings, and tuples.

# Defining a Set: To define a set, you need to write its elements within curly brackets and separate them with commas.
my_set = {1,2,3,4,5,5,5,5,5,3,2}


# common methods in set?
# my_set.remove(7) gives the keyerror 
my_set.discard(7)# doesnot give keyerror
my_set.add(6)
print(my_set)
my_set.clear()
print(my_set)