class ParentClass:
    _protectedVariable = 0    # private variable

    def __init__(self):
        self.a = 'Jakir non projected'
        self._b = 'Jakir projected'
        # working good
        self._protectedVariable = "I am talking from"


class ChildClass(ParentClass):
    def __init__(self):
        # call the parent class
        ParentClass.__init__(self)
        print('call the non private member', self.a)
        print('call the private member', self._b)
        # working good
        print('hello this private variable', self._protectedVariable)


obj = ParentClass()
print(obj.a)
print(obj._b)   # working good
# print(obj._privateVariable)   # not working
