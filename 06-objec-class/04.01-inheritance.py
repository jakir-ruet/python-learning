import math
from pyclbr import Class
from re import I


class Polygon:
    def __init__(self, edgeNumber):
        self.n = edgeNumber
        self.edges = [
            0 for i in range(edgeNumber)
        ]

    def edgeInputs(self):
        self.edges = [
            float(input('Enter the Edge' + str(i + 1) + ' : '))
            for i in range(self.n)
        ]

    def showEdge(self):
        for i in range(self.n):
            print('The Edge', i + 1, self.edges[i])

    class Triangle(Polygon):
        def __init__(self):
            Polygon.__init__(self, 3)

        def findArea(self):
            a, b, c = self.edges
            s = (a + b + c) / 2
            area = math.sqrt((s * (s - a) * (s - b) * (s - c)))
            print('The are is %0.2f' % area)
