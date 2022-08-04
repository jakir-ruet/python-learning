class Mango:
   #init method or constructor
   def __init__(self, fruitId, name, origin):
      self.fruitId = fruitId
      self.name = name
      self.origin = origin
   #create a function   
   def Output(self):
      print(f'Fruit ID : {self.fruitId}, Name : {self.name}, Origin : {self.origin}')
      
objOne = Mango(100, 'Monhonvog', 'Chapai Nawabganj')
objOne.Output()