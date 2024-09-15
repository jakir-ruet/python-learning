from abc import ABC, abstractmethod


# abstraction base class
class Polygon(ABC):
    @abstractmethod
    def edges(self):
        pass


class Triangle(Polygon):
    # overriding abstraction method
    def edges(self):
        print('Triangle has 3 sides')


class Quadrilateral(Polygon):
    # overriding abstraction method
    def edges(self):
        print('Quadrilateral has 4 sides')


class Pentagon(Polygon):
    # overriding abstraction method
    def edges(self):
        print('Pentagon has 5 sides')


class Hexagon(Polygon):
    # overriding abstraction method
    def edges(self):
        print('Hexagon has 6 sides')


t = Triangle()
t.edges()

q = Quadrilateral()
q.edges()

p = Pentagon()
p.edges()

h = Hexagon()
h.edges()
