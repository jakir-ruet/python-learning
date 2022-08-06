class ParentClass:
    def __init__(self):
        # protected member
        self._a = 5


class DerivedClass(ParentClass):
    def __init__(self):
        # calling the parent class here
        ParentClass.__init__(self)
        print('call protected member', self._a)

        # modify the protected member
        self._a = 10
        print('call modified outside of the class', self._a)


obj1 = DerivedClass()
print('Access to the protected member', obj1._a)

obj2 = ParentClass()
print('Access to the protected member', obj2._a)
