class Cat:
    def __init__(self, name, age, color):
        self.Name = name
        self.Age = age
        self.Color = color

    def details(self):
        print(self.Name, self.Color, self.Age)

    def make_sound(self):
        print('Meow')


class Dog:
    def __init__(self, name, age, color):
        self.Name = name
        self.Age = age
        self.Color = color

    def details(self):
        print(self.Name, self.Age, self.Color)

    def make_sound(self):
        print('Bark')


cat = Cat('Kitty', 23, 'Red')
dog = Dog('Raven', 24, 'White')

for animal in (cat, dog):
    animal.make_sound()
    animal.details()
