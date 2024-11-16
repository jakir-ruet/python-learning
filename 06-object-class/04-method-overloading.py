# class MethodOverloading:
#     def product(self, a, b):
#         print(a * b)
#
#     def product(self, a, b, c):
#         print(a * b * c)
#
# obj = MethodOverloading()
# # obj.product(3, 5)
# # if we try to use three value then it will through an error
# obj.product(3, 5, 7)

# # this type of problem we can overcome using overloading WAY ONE
# class MethodOverloading:
#     def product(self, a, b = None, c = None):
#         if a != None and b != None and c != None:
#             print(a * b * c)
#         elif a != None and b != None:
#             print(a * b)
#         else:
#             print(1 * a)
# obj = MethodOverloading()
# obj.product(3)
# obj.product(3, 4)
# obj.product(3, 4, 5)

# this type of problem we can overcome using overloading WAY TWO
class MethodOverloading:
    def product(self, *nums):
        mul = 1
        print(nums)
        for n in nums:
            mul = mul * n
            print(mul)


obj = MethodOverloading()
obj.product(3)
obj.product(3, 4)
obj.product(3, 4, 5)
obj.product(3, 4, 5, 6)  # here we can use any number of digit
