class Computer:

    def __init__(self):
        self.__maxPrice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxPrice))

    def set_max_price(self, price):
        self.__maxPrice = price


c = Computer()
c.sell()

# change the price
c.__maxPrice = 1000
c.sell()

# using setter function
c.set_max_price(1200)
c.sell()
