from datetime import date


class Employee:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    @classmethod
    def age_calculator(cls, name, dob):
        return cls(name, date.today().year - dob)

    def show(self):
        print(self.Name + "'s age is " + str(self.Age))


jakir = Employee('Jakir', 35)
jakir.show()

jasim = Employee.age_calculator('Jasim', 1986)
jasim.show()
