class Student:
    def __init__(self, stu_id, name, age):
        self.Stu_Id = stu_id
        self.Name = name
        self.Age = age

    def details(self):
        print('Student Info: ', self.Stu_Id, self.Name, self.Age)


class CseStudent(Student):
    def __init__(self, stu_id, name, age, labs):
        super().__init__(stu_id, name, age)
        self.Lab_yes = labs

    def cse_student_details(self):
        print(self.Lab_yes, 'lab tag')


# child class
class CseFresherStudent(CseStudent):
    def enroll_cse(self):
        print(self.Name, 'enrolled in CSE')


stu1 = CseStudent(102, 'Jakir', 35, 'yes')
stu1.details()
stu1.cse_student_details()
stu2 = CseFresherStudent(103, 'Jasim', 30, 'no')
stu2.details()
stu2.cse_student_details()
stu2.enroll_cse()
