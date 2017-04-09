class Shape:
    def get_area(self):
        return 0.0
    def __str__(self):
        return 'This is a theorhetical shape'

class Triangle(Shape):
    baseW = 0.0
    height = 0.0

    def __init__(self, base=1.0, height2=1.0):
        self.baseW = base
        self.height = height2

    def get_area(self):
        return (.5 * self.baseW * self.height)

    def __str__(self):
        t = Triangle(self.baseW, self.height)
        return 'Base of: ' + str(self.baseW) + ' | ' + 'Height: ' + str(self.height) + ' | ' + 'Area: ' + str(
            t.get_area())

    def __add__(self, other):
        newTriangle = Triangle()
        newTriangle.baseW = self.baseW + other.baseW
        newTriangle.height = self.height + other.height
        return newTriangle

class Circle(Shape):
    radius = 1

    def PI(self):
        return 3.14159

    def __init__(self, r=0):
        self.radius = r

    def get_area(self):
        c = Circle(self.radius)
        return (c.PI() * self.radius * self.radius)

    def get_diameter(self):
        return (self.radius * 2)

    def get_circumference(self):
        c = Circle(self.radius)
        return (2 * c.PI() * self.radius)

    def __str__(self):
        return 'Radius: ' + str(self.radius) + ' | ' + 'Area: ' + str(
            Circle(self.radius).get_area()) + ' | ' + 'Diameter: ' + str(
            Circle(self.radius).get_diameter()) + ' | ' + 'Circumference: ' + str(
            Circle(self.radius).get_circumference()) + ' | '

    def __add__(self, otherR):
        newRadius = Circle()
        newRadius.radius = self.radius + otherR.radius
        return newRadius


ask = input('(1) Add a shape, (2) Display a shape, (3) Total Area, (4) Exit')

if ask == 1:
    askShape = input('What shape are you entering?')
    if askShape != 'circle' or 'shape':
        s = Shape()
    else:
        i = input('')