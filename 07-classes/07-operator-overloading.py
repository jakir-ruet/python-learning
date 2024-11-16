class OperatorOverloading:
    def __init__(self, water, salt):
        self.Water = water
        self.Salt = salt

    def saline(self):
        print('Make a glass of saline w:s = ', self.Water, self.Salt)

    def __add__(self, other):
        new_water = self.Water + other.Water
        new_salt = self.Salt + other.Salt
        obj = OperatorOverloading(new_water, new_salt)
        return obj


s1 = OperatorOverloading(4, 3)
s1.saline()
s2 = OperatorOverloading(5, 4)
s2.saline()
# if we want to add s1 & s1 then we must use operator overloading
s3 = s1 + s2  # s1.__add__(s2)
s3.saline()
