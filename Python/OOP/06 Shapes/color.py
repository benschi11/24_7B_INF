from dataclasses import dataclass

@dataclass
class Color:
    r : int
    g : int
    b : int

    def __post_init__(self):
        if self.r < 0 or self.r > 255:
            raise TypeError("r must be between 0 and 255")
        
        if self.g < 0 or self.g > 255:
            raise TypeError("g must be between 0 and 255")
        
        if self.b < 0 or self.b > 255:
            raise TypeError("b must be between 0 and 255")
        
    
    def toTuple(self) -> tuple:
        return (self.r/255, self.g/255, self.b/255)