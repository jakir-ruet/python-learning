class ParentClass:
    def __init__(self):
        self.a = 'Jakir non private'
        self.__b = 'Jakir private'


class ChildClass(ParentClass):
    def __init__(self):
        # call the parent class
        ParentClass.__init__(self)
        print('call the non private member', self.a)
        print('call the private member', self.__b)


obj1 = ParentClass()
print(obj1.a)
