from dataclasses import dataclass
from Vehicle import vehicle

@dataclass
class train(vehicle):
    numberWagons : int
    numberPassengers: int

    def info(self) -> str:
        return f"Der Zug der Marke {self.brand} fährt mit {self.speed} km/h. Er hat {self.numberWagons} Wagons angehängt und transportiert {self.numberPassengers} Personen."


