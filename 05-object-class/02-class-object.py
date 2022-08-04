class Employee:
   empId = ''
   name = ''
   designation = ''

   #create a method
   def setValue(self, empId, name, designation):
      self.empId = empId
      self.name = name
      self.designation = designation

   #create a function
   def show(self):
      print(f"ID : {self.empId}, Name : {self.name}, Designation : {self.designation}")


#creating an object
rahim = Employee()
print(isinstance(rahim, Employee))  # checking for instance created
rahim.setValue(54003, 'Jakir', 'Managing Director')
rahim.show()

karim = Employee()
karim.setValue(54004, 'Momin', 'Director')
karim.show()