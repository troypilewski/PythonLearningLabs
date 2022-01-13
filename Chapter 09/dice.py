from random import randint

class Die:
    """Simulates a dice rolling"""

    def __init__(self, sides=6):
        """Creates a dice"""
        self.sides = sides

    def rollDice(self, roll):
        """Rolls the dice"""
        for die in range(roll):
            print("Roll {}: {}".format(die, randint(1, self.sides)))
    
d6 = Die(6)
print("Rolling a {} sided die.".format(d6.sides))
d6.rollDice(10)

d10 = Die(10)
print("Rolling a {} sided die.".format(d10.sides))
d10.rollDice(10)

d20 = Die(20)
print("Rolling a {} sided die.".format(d20.sides))
d20.rollDice(5)