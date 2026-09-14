def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

# print("calculator file is running") in main.py its calculator.py is running so put it inside the if statement
if __name__ == "__main__":
    print("calculator file is running.")
    print(add(10,3))
    print(subtract(10,4))
# if __name__ == "__main__": if we dont do this then all the output also imported to main.py that is not good only the function should be executed.

# print("calculator file is running.")
# print(add(10,3))
# print(subtract(10,4))
