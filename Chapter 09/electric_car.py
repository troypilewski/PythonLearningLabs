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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describeBattery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

tesla = ElectricCar('tesla', 'model s', 2019)
print(tesla.getDescriptiveName())
tesla.describeBattery()