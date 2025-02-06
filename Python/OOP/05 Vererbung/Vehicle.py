from dataclasses import dataclass, field

@dataclass
class vehicle():
    brand : str
    speed : int

    def accelerate(self, delta):
        self.speed += delta

    def decelerate(self, delta):
        if delta > self.speed:
            self.speed = 0
        else:
            self.speed -= delta

    def info(self) -> str:
        return f"Das Fahrzeug der Marke {self.brand} fährt mit {self.speed} km/h"

    
