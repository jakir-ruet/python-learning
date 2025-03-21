class Employee:
    empId = ''
    name = ''
    designation = ''


# creating an object
rahim = Employee()
print('Checking for instance created', isinstance(rahim, Employee))
print('Checking the object', rahim)
rahim.empId = 54003
rahim.name = 'Rahim'
rahim.designation = 'Sr. Developer'
print(f"ID : {rahim.empId}, Name: {rahim.name}, Designation : {rahim.designation}")
