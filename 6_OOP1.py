class Student:
    def __init__(self, name, age):
        self.student_name = name
        self.student_age = age

    def show_info(self):
        print(f"Name: {self.student_name}, Age: {self.student_age}")

s1 = Student("Saad Mansoori", 20)
print(s1.student_name)
print(s1.student_age)

s1.show_info()

s2 = Student("Tabish", 19)
s2.show_info()
#Student.show_info(s2)


studentsList_2306B1 = [ Student("Razan", 21), Student("Zaeema", 21), Student("Abdul Muheet", 19) ]

studentsList_2306B1[0].show_info()

for stdObj in studentsList_2306B1:
    stdObj.show_info()

