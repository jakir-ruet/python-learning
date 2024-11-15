class ParentClass:
    __privateVariable = 0    # private variable

    def __init__(self):
        self.a = 'Jakir non private'
        self.__b = 'Jakir private'
        # not working
        self.__privateVariable = "I am talking from"


class ChildClass(ParentClass):
    def __init__(self):
        # call the parent class
        ParentClass.__init__(self)
        print('call the non private member', self.a)
        print('call the private member', self.__b)
        # not working
        print('hello this private variable', self.__privateVariable)


obj = ParentClass()
print(obj.a)
# print(obj.__b)   # not working
# print(obj.__privateVariable)   # not working
