person = {"name":"abin", "age":24}

new_person = {
    **person,
    "city":"kathmandu"
}
print(new_person)
# Think of **person as:
# "Take everything inside this dictionary and put it here."
# combining dictionaries
a = {"name": "John"}
b = {"age": 33}

person = {
    **a,
    **b
}

print(person)
# 3.** in function arguments
def person_info(name, age):
    print(name, age)

person = {
    "name": "John",
    "age": 33
}

person_info(**person)
# person_info(name="John", age=33)
# note:::
#  *   → unpack list/tuple
# **  → unpack dictionary
numbers = [1, 2, 3]
print(*numbers)

# person = {"name": "John", "age": 33}
# print(**person)  # ❌ not valid for print like this

# ** is mainly used when building dictionaries or passing keyword arguments to functions.