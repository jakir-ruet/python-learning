class Employee:
    empId = ''
    name = ''
    designation = ''

    # create a method
    def set_value(self, emp_id, name, designation):
        self.empId = emp_id
        self.name = name
        self.designation = designation

    # create a function
    def show(self):
        print(f"ID : {self.empId}, Name : {self.name}, Designation : {self.designation}")


# creating an object
rahim = Employee()
print(isinstance(rahim, Employee))  # checking for instance created
rahim.set_value(54003, 'Jakir', 'Managing Director')
rahim.show()

karim = Employee()
karim.set_value(54004, 'Momin', 'Director')
karim.show()
