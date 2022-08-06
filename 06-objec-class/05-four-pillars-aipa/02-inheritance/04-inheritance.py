def flyParent():
    print('I can fly independently > parent class')


class birdParent:
    def __init__(self):
        print('This is parent of bird > parent class')


def flyChild():
    print('I do not fly independently > child class')


class birdChild(birdParent):
    def __init__(self):
        super().__init__()  # call super function
        print('This is child bird > child class')


myObj = birdChild()
flyParent()
flyChild()
