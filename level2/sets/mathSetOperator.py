my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 5}

print(your_set.issubset(my_set)) # True your_set is subset is my_set
print(my_set.issuperset(your_set)) # True

# isdisjoint()-->The isdisjoint() method checks if two sets are disjoint, if they don't have elements in common.
print(my_set.isdisjoint(your_set))# false because they have the common 

print(my_set | your_set)#union operator
# The union operator | returns a new set with all the elements from both sets.
print(my_set & your_set)# intersecttion operator
# The intersection operator & returns a new set with only the elements that the sets have in common.
print(my_set - your_set)# difference operator
# The difference operator - returns a new set with the elements of the first set that are not in the other sets.
print(my_set^ your_set)#symmetric operator
# The symmetric difference operator ^ returns a new set with the elements that are either in the first or the second set, but not both.



