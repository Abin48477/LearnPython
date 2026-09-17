# pop() removes a key from the dictionary and returns its value
person = {
    "name": "John",
    "age": 33
}

age = person.pop("age")

print(age)
print(person)#here the age is not displayed
# 33 return the value 
# {'name': 'John'} removes a key from the dictionary 
# popitem()--> removes the last inserted item 
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250
}
remove = pizza.popitem()
print(remove)
print(pizza)
# # pizza.pop('price')       # ✅
# pizza.popitem()          # ✅
# pizza.popitem('price')   # ❌
# \note:
# pop('key')       → remove a specific key
# popitem()        → remove the last key-value pair