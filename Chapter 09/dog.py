class Dog:
    """A model of a dog"""

    def __init__(self, name, age):
        """Initializes the name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulates a dog sitting in response to a command"""
        print("{} is sitting.".format(self.name))

    def down(self):
        """Simulates a dog laying down in response to a command"""
        print("{} is laying down.".format(self.name))