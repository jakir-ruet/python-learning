class Employee:
    def __init__(self, emp_id, name, age):
        self.Emp_Id = emp_id        # instance variable
        self.Name = name        # instance variable
        self.Age = age        # instance variable

    def show(self):         # instance method
        print('ID: ', self.Emp_Id, 'Name: ', self.Name, 'Age: ', self.Age)

    # update the method
    def update(self, name, age):
        self.Name = name
        self.Age = age


obj = Employee(101, 'Jakir', 35)
# call instance method
obj.show()
obj.update('Rahim', 40)
obj.show()
