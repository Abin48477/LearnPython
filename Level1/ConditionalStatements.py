# Operator	Name	Description
# ==	    Equal	        Checks if two values are equal
# !=	    Not equal	    Checks if two values are not equal
# >	    Greater than	Checks if the value on the left is greater than the value on the right
# <	    Less than	    Checks if the value on the left is less than the value on the right
# >=	Greater than or equal	Checks if the value on the left is greater than or equal to the value on the right
# <=	Less than or equal	    Checks if the value on the left is less than or equal to the value on the right

print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

age = 12
if age>18:
    print('you are adult.')
elif age > 50:
    print('you r old.')
else:
    print("you are child")  
