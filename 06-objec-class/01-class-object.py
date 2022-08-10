class Employee:
    empId = ''
    name = ''
    designation = ''


# creating an object
rahim = Employee()
print(isinstance(rahim, Employee))  # checking for instance created
print(rahim) # checking the object
rahim.empId = 54003
rahim.name = 'Rahim'
rahim.designation = 'Sr. Developer'
print(f"ID : {rahim.empId}, Name: {rahim.name}, Designation : {rahim.designation}")
