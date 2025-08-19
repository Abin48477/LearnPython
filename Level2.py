#Exception Handling
a = int(input("Enter numerator value:"))
b = int (input("Enter denominator value:"))
try:
    r=a/b
    print("Result is :",r)
except:
    print("division by zoro is not possible")
finally:
    print("This is the final code that should be run at any cost")