class Employee(object):
    def __init__(self, name, salary, project):
        self.Name = name
        self.Salary = salary
        self.Project = project

    @staticmethod
    def details(project):
        if project == 'Console Project':
            requirement = ['C', 'Compiler', 'MinGW']
        else:
            requirement = ['C']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.details(self.Project)
        for req in requirement:
            print('Completed', req)


emp = Employee('Jakir', 3500, 'Console Project')
emp.work()


# Call Static Method from Another Method
class Test:
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2():
        Test.static_method_1()

    @classmethod
    def class_method_1(cls):
        cls.static_method_2()


# call class method
Test.class_method_1()
