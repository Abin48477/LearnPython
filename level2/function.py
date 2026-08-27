def hello():
    return "hey hello abin"

print(hello())
print(hello())

def add(a,b):
    if not isinstance(a,(int,float)) or not isinstance(b, (int, float)):
        return "enter the number"
    else:
        return a+b
print(add(20,"40"))

# isinstance() method checks the datatype
# type() method find/check the exact data type