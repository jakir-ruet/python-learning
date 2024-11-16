class Employee:

    def __init__(self, shirt, pant):
        self.Shirt = shirt
        self.Pant = pant

    def create(self):
        print(self.Shirt, self.Pant)

    def update(self, shirt, pant):
        self.Shirt = shirt
        self.Pant = pant
        print(self.Shirt, self.Pant)


rahim = Employee('black', 'green')
rahim.create()

rahim.update('white', 'green')
