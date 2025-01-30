from dataclasses import dataclass, field
from Vehicle import vehicle


@dataclass
class car(vehicle):
    currentFuelAmount: float