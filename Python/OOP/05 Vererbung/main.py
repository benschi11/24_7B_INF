from Car import car
from Bike import bike
from Train import train

michisAuto = car("BMW",0,20)
michisAuto.brand = "Audi"
michisAuto.accelerate(40)
michisAuto.decelerate(90)

print(michisAuto.info())

michisBike = bike("KTM",0,2)
michisBike.accelerate(10)
print(michisBike.info())

michisZug = train("Siemens", 200, 10,80)

print(michisZug.info())

# print(michisBike)

# print(michisAuto)