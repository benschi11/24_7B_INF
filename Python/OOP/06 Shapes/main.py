from circle import Circle
from point import Point
from rectangle import Rectangle
import turtle

t1 = turtle.Turtle("turtle")

circle1 = Circle(Point(0,0),100)

print(circle1.centerPoint)

circle1.draw(t1)


rec1 = Rectangle(Point(100,-100),100,200)
rec1.draw(t1)

turtle.done()