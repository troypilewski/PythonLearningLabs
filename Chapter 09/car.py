"""A class that can be used to represent a car"""

class Car:
    """A simple representation of a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        reading = "This care has {} miles on it.".format(self.odometer)
        print(f"This car has {self.odometer} miles on it.")

    def updateOdometer(self, mileage):
        """Sets the odometer to the given value"""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("The odometer reading cannot be less than the current value of {}.".format(self.odometer))

""" car = Car('audi', 'a4', 2019)
print(car.getDescriptiveName())
car.odometer = 23
car.readOdometer()
car.updateOdometer(35)
car.readOdometer() """