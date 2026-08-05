from multipledispatch import dispatch

@dispatch(int, int)
def product(a, b):
    print("Result:", a * b)

@dispatch(int, int, int)
def product(a, b, c):
    print("Result:", a * b * c)

@dispatch(float, float, float, float)
def product(a, b, c, d):
    print("Result:", a * b * c * d)

product(3, 4)
product(1, 2, 3)
product(1.0, 2.0, 3.0, 4.0)
