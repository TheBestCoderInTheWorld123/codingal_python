class Shapes:
    def area(self):
        pass

class Square(Shapes):
    def area(self):
        sqr = int(input("What is the length of the square?\n"))
        sqr_area = sqr*sqr
        print("Area is", sqr_area)

class Rectangle(Shapes):
    def area(self):
        rec_l = int(input("What is the length of the rectangle?\n"))
        rec_w = int(input("What is the width of the rectangle?\n"))
        rec_area = rec_l*rec_w
        print("Area is", rec_area)
        
class Circle(Shapes):
    def area(self):
        circle_r = int(input("What is the radius of the circle?\n"))
        circle_area = 3.14*circle_r*circle_r
        print("Area is", circle_area)

class Triangle(Shapes):    
    def area(self):
        tri_h = int(input("What is the height of the triangle?\n"))
        tri_b = int(input("What is the base of the triangle?\n"))
        tri_area = (tri_h*tri_b)/2
        print("Area is", tri_area)

sqr = Square()
rec = Rectangle()
circle = Circle()
tri = Triangle()

print("What shape's area do you want?\n1. Square\n2. Rectangle\n3. Circle\n4. Triangle")
ch = int(input())
if(ch == 1):
    print("\nSquare")
    sqr.area()
elif(ch == 2):
    print("\nRectangle")
    rec.area()
elif(ch == 3):
    print("\nCircle")
    circle.area()
elif(ch == 4):
    print("\nTriangle")
    tri.area()
else:
    print("I said 1, 2, 3, or 4...")
