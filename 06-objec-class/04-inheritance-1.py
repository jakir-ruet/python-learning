class Polygon:
    def __init__(self, edges):
        self.edges = edges

    def display_info(self):
        print('A polygon')

    def get_perimeter(self):
        perimeter = sum(self.edges)
        return perimeter


class Triangle(Polygon):
    def display_info(self):
        print('the triangle')


class Quadrilateral(Polygon):
    def display_info(self):
        print('Quadrilateral')


t1 = Triangle([2, 3, 4])
perimeter = t1.get_perimeter()
print('Perimeter of Triangle', perimeter)

r1 = Quadrilateral([2, 3, 4, 5])
perimeter = r1.get_perimeter()
print('The area of Quadrilateral', perimeter)
