def fly_parent():
    print('I can fly independently > parent class')


class BirdParent:
    def __init__(self):
        print('This is parent of bird > parent class')


def fly_child():
    print('I do not fly independently > child class')


class BirdChild(BirdParent):
    def __init__(self):
        super().__init__()  # call super function
        print('This is child bird > child class')


myObj = BirdChild()
fly_parent()
fly_child()
