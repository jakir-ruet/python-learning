from abc import ABC, abstractmethod


class ParentClass(ABC):
    # common function
    def common_function(self):
        print('This is the parent class')

    @abstractmethod
    def abstraction_function(self):
        # this is different form of child class
        pass


class ChildOne(ParentClass):
    def abstraction_function(self):
        print('This is a abstract method of child one')


class ChildTwo(ParentClass):
    def abstraction_function(self):
        print('This is a abstract method of child two')


ch1 = ChildOne()
ch1.common_function()
ch1.abstraction_function()

ch2 = ChildTwo()
ch2.common_function()
ch2.abstraction_function()