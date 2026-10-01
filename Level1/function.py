class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        if self.marks >=80:
            return "A"
        elif self.marks >=60:
            return "B"
        elif self.marks >=40:
            return "C"
        else:
            return "F"
s1 = Student("Abin","3",46)

grade = s1.display()

print(f'Congratulation! you got {grade} Grade. Hare krishna!')


        
        