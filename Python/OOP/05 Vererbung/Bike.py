from dataclasses import dataclass, field
from Vehicle import vehicle

@dataclass
class bike(vehicle):
    airpressure : float