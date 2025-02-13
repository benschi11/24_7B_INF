from dataclasses import dataclass
from shape import Shape

import turtle

@dataclass
class Rectangle(Shape):
    width : int
    height : int

    def draw(self, t:turtle.Turtle):
        t.penup() # verhindert das zeichnen
        t.goto(self.topleft.coords)
        t.degrees(360)
        t.pendown() # Starte Zeichnen
        for _ in range(2):
            t.forward(self.width)
            t.right(90)
            t.forward(self.height)
            t.right(90)