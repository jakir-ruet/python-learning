class ParentClass:
    def __init__(self, name):
        self.name = name
        print('This is parent class')

    def parent_guideline(self, name):
        self.name = name
        print('You must study equilibrium', self.name)

    def giving_property(self, name):
        self.name = name
        print('You will get all property', self.name)


class ChildClass(ParentClass):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        print('This is Child class')

    def parent_guideline(self, name):
        # if we use both method of parent & child class the use super method
        # super().parent_guideline(name)
        print('I must study regularly not always', self.name)


# where override the parent_guideline in parent class
obj1 = ChildClass('Jasim')
obj1.parent_guideline('Jasim')
obj1.giving_property('Jasim')

print(obj1)
print(obj1.__str__())
