from Car import car
from Bike import bike

michisAuto = car("BMW",0,20)
michisAuto.accelerate(40)
michisAuto.decelerate(90)

michisBike = bike("KTM",0,2)
michisBike.accelerate(10)

print(michisBike)

print(michisAuto)