# if the same method is define in both base & derived classes
# then the method of the derived class overrides the method of the base class
# here override the serve_juice method in base class instead of serve_juice method of drived method.
class Juice:
    def __init__(self, ingredient):
        self.ingredient = ingredient

    def serve_juice(self):
        print('This is a glass of juice')

    def making_juice(self):
        making = sum(self.ingredient)
        return making


class MangoJuice(Juice):
    def serve_juice(self):
        print('Serve the mango juice')
        #Juice.serve_juice(self)
        super().serve_juice()


class BananaJuice(Juice):
    def serve_juice(self):
        print('Serve banana juice')


m1 = MangoJuice([2, 3, 4, 5, 8])
making = m1.making_juice()
print('This is mango juice', making)
m1.serve_juice()

b1 = BananaJuice([3, 4, 5, 6])
making = b1.making_juice()
print('This is banana juice', making)

