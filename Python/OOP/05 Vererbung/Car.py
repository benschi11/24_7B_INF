from dataclasses import dataclass, field
from Vehicle import vehicle


@dataclass
class car(vehicle):
    currentFuelAmount: float

    def info(self) -> str:
        return f"Das Auto der Marke {self.brand} fährt mit {self.speed} km/h. Tankfüllstand: {self.currentFuelAmount} Liter"