class PublicMember:
    def __init__(self, emp_id, name, age):
        self.Emp_Id = emp_id
        self.Name = name
        self.Age = age

    def emp_age(self):
        # Accessing the public data member
        print('Age = ', self.Age)


obj = PublicMember(101, "Jakir", 35)
# Accessing the public data member
print('Id = ', obj.Emp_Id)
print('Name = ', obj.Name)
# calling public member function of class
obj.emp_age()
