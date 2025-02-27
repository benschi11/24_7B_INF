from dataclasses import dataclass
from shape import Shape
from point import Point

import turtle

@dataclass
class Circle(Shape):
    radius : int

    @property
    def centerPoint(self) -> Point:
        center_x = self.topleft.x + self.radius
        center_y = self.topleft.y - self.radius
        centerPoint = Point(center_x, center_y)
        return centerPoint
    
    def draw(self, t:turtle.Turtle):
        super().draw(t)
        t.penup() # verhindert das zeichnen
        t.goto((self.topleft.x + self.radius, self.topleft.y - 2*self.radius))
        t.pendown()
        t.circle(self.radius)

