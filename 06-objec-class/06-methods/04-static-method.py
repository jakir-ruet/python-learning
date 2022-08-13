class Employee:
    edu_ins_name = 'RUET'

    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def details(self):
        print(self.Name, self.Age)

    @classmethod
    def add_edu_ins(cls, ins_name):
        cls.add_edu_ins = ins_name

    @classmethod
    def input_from_string(cls, string_name):
        name, age = string_name.split('-')
        obj = cls(name, age)
        return obj


emp1 = Employee('Jakir', 35)
emp1.details()
emp2 = Employee.input_from_string('Jasim-45')
emp2.details()
