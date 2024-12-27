class Polygons:
    def area(self):
        pass

class Triangle(Polygons):    
    def area(self):
        tri_h = int(input("What is the height of the triangle?\n"))
        tri_b = int(input("What is the base of the triangle?\n"))
        tri_area = (tri_h*tri_b)/2
        print("Area is", tri_area)

class Square(Polygons):
    def area(self):
        sqr = int(input("What is the length of the square?\n"))
        sqr_area = sqr*sqr
        print("Area is", sqr_area)

class Pentagon(Polygons):
    def area(self):
        pent_l = int(input("What is the length of the pentagon?\n"))
        pent_area = 0.25*6.88*pent_l*pent_l
        print("Area is", pent_area)
        
class Hexagon(Polygons):
    def area(self):
        hex_l = int(input("What is the length of the hexagon?\n"))
        hex_area = 0.5*1.73*3*hex_l*hex_l
        print("Area is", hex_area)

tri = Triangle()
sqr = Square()
pent = Pentagon()
hex = Hexagon()

print("What shape's area do you want?\n1. Triangle\n2. Square\n3. Pentagon\n4. Hexagon")
ch = int(input())
if(ch == 1):
    print("\nTriangle")
    tri.area()
elif(ch == 2):
    print("\nSquare")
    sqr.area()
elif(ch == 3):
    print("\nPentagon")
    pent.area()
elif(ch == 4):
    print("\nHexagon")
    hex.area()
else:
    print("I said 1, 2, 3, or 4...")
