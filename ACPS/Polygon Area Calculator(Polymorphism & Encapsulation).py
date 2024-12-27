class Triangle:
    def __init__(self):
        self.__base = None
        self.__height = None

    def polygon(self):
        print("\nTriangle")

    def set_dimensions(self):
        self.__base = int(input("What is the base of the triangle?\n"))
        self.__height = int(input("What is the height of the triangle?\n"))

    def calculate_area(self):
        return 0.5*self.__base*self.__height

    def area(self):
        self.set_dimensions()
        print(f"Area is {self.calculate_area()}")


class Square:
    def __init__(self):
        self.__length = None

    def polygon(self):
        print("\nSquare")

    def set_dimensions(self):
        self.__length = int(input("What is the length of the square?\n"))

    def calculate_area(self):
        return self.__length*self.__length

    def area(self):
        self.set_dimensions()
        print(f"Area is {self.calculate_area()}")


class Pentagon:
    def __init__(self):
        self.__length = None

    def polygon(self):
        print("\nPentagon")

    def set_dimensions(self):
        self.__length = int(input("What is the length of the pentagon?\n"))

    def calculate_area(self):
        return 0.25*6.88*self.__length*self.__length

    def area(self):
        self.set_dimensions()
        print(f"Area is {self.calculate_area()}")

class Hexagon:
    def __init__(self):
        self.__length = None

    def polygon(self):
        print("\nHexagon")

    def set_dimensions(self):
        self.__length = int(input("What is the length of the hexagon?\n"))

    def calculate_area(self):
        return 0.5*1.73*3*self.__length*self.__length

    def area(self):
        self.set_dimensions()
        print(f"Area is {self.calculate_area()}")

tri = Triangle()
sqr = Square()
pent = Pentagon()
hex = Hexagon()

for i in (tri, sqr, pent, hex):
    i.polygon()
    i.area()
