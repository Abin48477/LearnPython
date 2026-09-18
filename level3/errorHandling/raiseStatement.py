def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
try:
    check_age(-5)
except ValueError as e:
    print(f"Error:{e}")
    # Error:Age cannot be negative

def test():
    try:
        int("hello")
    except ValueError:
        print("I saw the error!")
        raise
print(test())

#     raise   → 🚨 "There is a problem!"
# except  → 🧑‍🚒 "Don't worry, I'll handle it."

# check_age(-5)
    #   ↓
# age < 0 ?
#       ↓
#     YES
#       ↓
# raise ValueError
#       ↓
# except catches it
#       ↓
# print the error

def login(username):
    if username == "":
        raise ValueError("Username cannot be empty")

    print("Login successful")

print(login("abin"))
# raise by itself = throw the current error again.