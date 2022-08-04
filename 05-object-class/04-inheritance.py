class birdParent:
   def __init__(self):
      print('This is parent of bird > parent class')
   def flyParent(self):
      print('I can fly independently > parent class')

class birdChild(birdParent):
   def __init__(self):
      super().__init__() #call super function
      print('This is child bird > child class')
   def flyChild(self):
      print('I do not fly independently > child class')
myObj = birdChild()
myObj.flyParent()
myObj.flyChild()