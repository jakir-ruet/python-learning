class Employee:
    designation = 'Manager'     # static/class variable

    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    # class method
    @classmethod
    def change_designation(cls, name):      # cls refer to class
        print(Employee.designation)         # access class variable
        Employee.designation = name         # modify class variable


obj = Employee('Jakir', 25)
Employee.change_designation('Managing Director')
