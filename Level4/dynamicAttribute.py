# Dynamic object attributes = working with an object's attributes when their names are decided while the program is running.

# And the important functions are:

# getattr() → get
# setattr() → set/change
# hasattr() → check if it exists
# delattr() → delete

class Product:
    def __init__(self):
        self.name = "Laptop"
        self.price = 800
        self.brand = "Dell"
product = Product()

# Change an attribute with setattr().
setattr(product, "price", 1000)

#to know the object attribute we use dir() function
for attr in dir(product):
    if not attr.startswith('__') and not callable(getattr(product, attr)):
        value = getattr(product, attr)
        print(f'{attr}:{value}')

# print(product.price)#You already know the attribute.
attribute = input("What do you want to know? ")
if hasattr(product, attribute):
    print(getattr(product, attribute))
else:
    print(f"I didn't find the attribute named '{attribute}'")

# getattr(object, attribute_name, default_value) 
attribute = input("Which attribute do you want to delete? ")
if hasattr(product, attribute):
    delattr(product, attribute)
    print(f"Deleted '{attribute}'")
else:
    print(f"I didn't find the attribute named '{attribute}'")