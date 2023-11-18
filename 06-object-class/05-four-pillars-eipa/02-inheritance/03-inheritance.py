class Student:
    def __init__(self, stu_id, name, age):
        self.Stu_Id = stu_id
        self.Name = name
        self.Age = age

    def details(self):
        print('Student Info:', self.Stu_Id, self.Name, self.Age)


class StudentCse(Student):
    def __init__(self, stu_id, name, age, lab_yes):
        super().__init__(stu_id, name, age)
        self.Lab_yes = lab_yes

    def student_cse_lab_details(self):
        print('CSE Student: ', self.Lab_yes, 'labs')


class StudentNonCse(Student):
    def __init__(self, stu_id, name, age, lab_no):
        super().__init__(stu_id, name, age)
        self.Stu_Id = stu_id
        self.Name = name
        self.Age = age
        self.Lab_no = lab_no

    def student_non_cse_lab_details(self):
        print('Non CSE Student: ', self.Lab_no, 'Labs')


stu1 = StudentCse(102, 'Jakir', 20, 'lab yes')
stu1.details()
stu1.student_cse_lab_details()

stu2 = StudentNonCse(104, 'Jasim', 20, 'lab no')
stu2.details()
stu2.student_non_cse_lab_details()
