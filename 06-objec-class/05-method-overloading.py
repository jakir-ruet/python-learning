from multipledispatch import dispatch


class MethodOverloading:
    @dispatch(int)
    def product(self, a):
        print('Single parameter', a)

    @dispatch(int, int)
    def product(self, a, b):
        print('Double parameter same data type', a * b)

    @dispatch(str, int)
    def product(self, a, b):
        print('Double parameter diff data type', int(a) * b)

    @dispatch(float, float, float)
    def product(self, a, b, c):
        print('Triple parameter same data type', a * b * c)


obj = MethodOverloading()
obj.product(3)
obj.product(3, 4)
obj.product('3', 4)
obj.product(3.0, 4.0, 5.0)
