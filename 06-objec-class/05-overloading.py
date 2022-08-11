from multipledispatch import dispatch
class MethodOverloading:
    @dispatch(int)
    def product(self, a):
        print(a)

    @dispatch(int, int)
    def product(self, a, b):
        print(a * b)

    @dispatch(str, int)
    def product(self, a, b):
        print(int(a) * b)

    @dispatch(float, float, float)
    def product(self, a, b, c):
        print(a * b * c)

obj = MethodOverloading()
obj.product(3)
obj.product(3, 4)
obj.product('3', 4)
obj.product(3.0, 4.0, 5.0)
