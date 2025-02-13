from dataclasses import dataclass

@dataclass
class Point():
    x : int = 0
    y : int = 0

    def __str__(self) -> str:
        return f"({self.x} | {self.y})"
    
    @property
    def coords(self) -> tuple:
        return (self.x,self.y)
    
    # def __iter__(self):
    #     yield self.x
    #     yield self.y