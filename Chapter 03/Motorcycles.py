motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

motorcycles.insert(0, 'ducati')
print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)

# poppedMotorcycle = motorcycles.pop(0)
# print(motorcycles)
# print(poppedMotorcycle)
# print("The first owned motercycle was a {}.".format(poppedMotorcycle.title()))
print(motorcycles)

tooExpensive = 'ducati'
motorcycles.remove(tooExpensive)
print(motorcycles)
print("A {} is too expensive for me.".format(tooExpensive.title()))

print(motorcycles[3])