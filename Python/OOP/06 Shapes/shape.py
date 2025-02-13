from dataclasses import dataclass
from turtle import Turtle
from point import Point
from abc import ABC, abstractmethod

@dataclass
class Shape(ABC):
    topleft : Point

    @abstractmethod
    def draw(self, t:Turtle) -> None:
        pass