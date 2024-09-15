class chipsSelection:
    def __init__(self):
        self.lays = 10  # here default value 10
        self.potato = 5  # here default value 5

    def show(self):
        print(self.lays, "Lays chips", self.potato, "potato")


chipsObj1 = chipsSelection()
chipsObj1.show()  # print here default values
chipsObj2 = chipsSelection()
chipsObj2.show()  # print here default values

# updating the default chips numbers
chipsObj1.lays = 40
chipsObj1.potato = 50
chipsObj1.show()

chipsObj2.lays = 20
chipsObj2.potato = 30
chipsObj2.show()
