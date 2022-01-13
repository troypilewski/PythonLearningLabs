from car import Car

a4 = Car('audi', 'a4', 2019)
print(a4.getDescriptiveName())

a4.updateOdometer(23)
a4.readOdometer()