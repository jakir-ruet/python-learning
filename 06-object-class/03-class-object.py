class Mango:
    # init method or constructor
    def __init__(self, fruit_id, name, origin):
        self.fruitId = fruit_id
        self.name = name
        self.origin = origin

    # create a function
    def output(self):
        print(f'Fruit ID : {self.fruitId}, Name : {self.name}, Origin : {self.origin}')


objOne = Mango(100, 'Monhonvog', 'Chapai Nawabganj')
objOne.output()
