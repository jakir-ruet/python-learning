
class Employee:
    designation = 'Sr. Manager'

    def __init__(self, emp_id, name, age):
        self.Emp_Id = emp_id
        self.Name = name
        self.Age = age

    @classmethod
    def change_designation(cls, designation):
        # class_name.class_variable
        cls.designation = designation

    # instance method
    def show(self):
        print('Emp Id:', self.Emp_Id, 'Name:', self.Name, 'Age:', self.Age, 'Designation:', self.designation)


jakir = Employee(101, 'Jakir', 35)
jakir.show()
# change the designation
Employee.change_designation('Managing Director')
jakir.show()
