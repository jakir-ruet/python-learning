class Employee:
    @staticmethod
    def detail(x):
        print('This is an Employee', x)


# call static method
Employee.detail(10)


class Student:
    uni_name = 'RUET'

    def __init__(self, stu_id, name):
        self.__Student_Id = stu_id
        self.Name = name

    def details(self):
        print(self.__Student_Id, self.Name, Student.uni_name)

    @classmethod
    def change_uname(cls, u_name):
        cls.uni_name = u_name

    @staticmethod
    def check_department(dept_id):
        if dept_id[1:3] == '50':
            print('CSE')
        elif dept_id[1:3] == '40':
            print('ETE')


stu1 = Student('Jakir', 54003)
stu1.details()
Student.check_department('54003')
stu2 = Student('Jasim', 55003)
stu2.details()
Student.check_department('55003')
