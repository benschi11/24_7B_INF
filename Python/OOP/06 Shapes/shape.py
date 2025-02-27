from dataclasses import dataclass
from turtle import Turtle
from color import Color
from point import Point
from abc import ABC, abstractmethod

@dataclass
class Shape(ABC):
    topleft : Point
    color : Color
    thickness : int

    @abstractmethod
    def draw(self, t:Turtle) -> None:
        t.pencolor(self.color.toTuple())
        t.pensize(self.thickness)