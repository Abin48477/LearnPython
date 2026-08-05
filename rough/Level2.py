# Exception Handling
a = int(input("Enter numerator value: "))
b = int(input("Enter denominator value: "))

try:
    r = a / b
    print("Result is:", r)
except ZeroDivisionError:
    print("Division by zero is not possible")
finally:
    print("This is the final code that should be run at any cost")

# Switch case (match-case in Python 3.10+)
day = int(input("Enter a number between 1 and 7: "))

match day:  # [web:1][web:2]
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid day number")

# Tuple
t = (1, 'c', "lumbini", 9 + 7)
print(t)
print(type(t))

l = list(t)  # convert tuple to list [web:9][web:12]
print(l)
print(type(l))

# Pyramid
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()  # move to next line [web:13][web:19]

# Table from 1 to 20
for i in range(1, 21):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")  # formatted string literal
    print()  # blank line between tables

# Triangle
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Dictionary
d = {
    "Faculty": "bca",
    "sem": 4,
    "Location": "gaidakot",
    "Duration": "4 years"
}
print(d)
print(type(d))
