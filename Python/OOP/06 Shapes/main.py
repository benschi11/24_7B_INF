from circle import Circle
from color import Color
from point import Point
from rectangle import Rectangle
import turtle

t1 = turtle.Turtle("turtle")

circle1 = Circle(Point(0,0),Color(20,250,10),2,100)

print(circle1.centerPoint)

circle1.draw(t1)


rec1 = Rectangle(Point(100,-100),Color(10,100,10),2,100,200)
rec1.draw(t1)

turtle.done() # lässt den Zeichenbereich offen