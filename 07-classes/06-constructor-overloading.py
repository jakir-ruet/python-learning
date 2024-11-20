# class Employee:
#     # def __init__(self, emp_id, name):
#     #     self.Id = emp_id
#     #     self.Name = name
#     #     print(self.Id, self.Name)
#
#     # def __init__(self, emp_id, name, salary):
#     #     self.Id = emp_id
#     #     self.Name = name
#     #     self.Salary = salary
#     #     print(self.Id, self.Name, self.Salary)
#
#
# # e1 = Employee(54003, 'Jakir')   # it's working good
# # e2 = Employee(54004, 'Momin', 5000)     # it does not work

# problem will be solved using constructor overloading METHOD #1
class Employee:
    def __init__(self, *emp_info):
        if len(emp_info) == 3:
            self.Id = emp_info[0]
            self.Name = emp_info[1]
            self.Salary = emp_info[2]
            print(self.Id, self.Name, self.Salary)
        elif len(emp_info) == 2:
            self.Id = emp_info[0]
            self.Name = emp_info[1]
            print(self.Id, self.Name)
        else:
            self.Id = emp_info[0]
            print(self.Id)

    print('Constructor working good here > checking purpose method #1')


e1 = Employee(54003, 'Jakir', 5000)
e2 = Employee(54003, 'Jakir')
e3 = Employee(54003)


# problem will be solved using constructor overloading METHOD #2
class Employee:
    def __init__(self, **emp_info):
        if len(emp_info) == 3:
            self.Id = emp_info['Id']
            self.Name = emp_info['Name']
            self.Salary = emp_info['Salary']
            print(self.Id, self.Name, self.Salary)
        elif len(emp_info) == 2:
            self.Id = emp_info['Id']
            self.Name = emp_info['Name']
            print(self.Id, self.Name)
        else:
            self.Id = emp_info['Id']
            print(self.Id)

    print('Constructor working good here > checking purpose method #2')


e11 = Employee(Id=54003, Name='Jakir', Salary=5000)
e22 = Employee(Id=54003, Name='Jakir')
e33 = Employee(Id=54003)
