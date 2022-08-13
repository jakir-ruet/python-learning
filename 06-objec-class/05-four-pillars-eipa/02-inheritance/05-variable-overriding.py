class Animal:
    def __init__(self, name):
        self.Name = name
        self.ColorDefault = 'White'         # default variable using color

    def eat(self):
        print(self.ColorDefault, self.Name, 'is eating')


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.ColorDefault = color   # where override ColorDefault variable of the default color

    def bark(self):
        print(self.ColorDefault, self.Name, 'is barking')


d1 = Dog('Dog1', 'Red')
d1.eat()
d1.bark()

d2 = Dog('Dog2', 'Black')
d2.eat()
d2.bark()
