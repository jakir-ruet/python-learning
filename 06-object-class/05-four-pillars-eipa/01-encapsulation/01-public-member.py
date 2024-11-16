class ParentClass:
    privateVariable = 0  # private variable

    def __init__(self):
        self.a = 'Jakir non private'
        self.b = 'Jakir private'
        # not working
        self.privateVariable = "I am talking from"


class ChildClass(ParentClass):
    def __init__(self):
        # call the parent class
        ParentClass.__init__(self)
        print('call the non private member', self.a)
        print('call the private member', self.b)
        # working good
        print('hello this private variable', self.privateVariable)


obj = ParentClass()
print(obj.a)
print(obj.b)  # working good
print(obj.privateVariable)  # working good
