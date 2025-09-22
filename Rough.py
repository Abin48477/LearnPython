# #Simple Student Marks program
# students = {}
# for i in range(5):
#         name = input("Enter student name:")
#         marks = int(input(f"Enter marks for {name}"))
#         students[name] = marks

# #Display 
# print ("\n-------Student Marks-------")
# for name,marks in students.items():
#         print(f"{name}:{marks}")

#boolean
result = (5>3)
print(result)

#List Comprehension
words =["hello","world","python","is","awesome"]
cap =[word.upper()for word in words]
low = [word.lower()for word in words]
print(cap)
print(low)

# Unpacking
t1 = (1,2,3,4,5)
a,*b,c= t1
print(a)
print(b)

