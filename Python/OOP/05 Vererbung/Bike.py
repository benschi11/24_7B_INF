from dataclasses import dataclass, field
from Vehicle import vehicle

@dataclass
class bike(vehicle):
    airpressure : float

    def info(self) -> str:
        return f"Das Fahrrad der Marke {self.brand} fährt mit {self.speed} km/h. Luftdruck der Reifen: {self.airpressure} bar"