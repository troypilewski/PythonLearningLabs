from random import randint

class Player:
    """Creates a player in the game"""

    def __init__(self, first, last) -> None:
        """Creates a player object with a first and last name"""
        self.first = first
        self.last = last
        pass

    def getProperName(self):
        """Returns a the players name in Title Case"""
        # Builds the full name of the player from the objects first and last name
        fullName = "{} {}".format(self.first, self.last)
        return fullName.title()

    def selectValue(self, value):
        """Prompts the player to select a value/integer and returns the selected value"""
        if value + 3 > 20:
            value1 = value + 1
            value2 = value + 2
            value3 = 20
        elif value + 2 > 20:
            value1 = value + 1
            value2 = 20
            value3 = 20
        elif value + 1 > 20:
            value1 = 20
            value2 = 20
            value3 = 20
        else:
            value1 = value + 1
            value2 = value + 2
            value3 = value + 3

        # Prompt string for the input function
        prompt = "Please select from the following values [{}, {}, {}]: ".format(value1, value2, value3)
        
        # Prompts the player to select a value/integer and stores it in the value variable
        value = int(input(prompt))
        
        # Returns the value variable
        return value

    def validateSelectedValue(self, selection, value):
        """Validates player selected a valid value/integer"""

        # Sets the flag to True if the validation fails
        flag = selection > (value + 3)

        # Loops through the validation until the validations passes
        while flag:
            # Let the player know that the value/integer is not valid
            print("The selected value is not a selectable options.")
            # Prompts the player to select a new value/integer
            selection = self.selectValue(value)
            # Tests the value is less than value + 3
            if selection <= (value + 3):
                value = selection
                break
        
        # Assigns the selection to the value variable
        value = selection

        # Returns a valid value
        return value    

class Computer:
    """Creates an automated player to play against the human player"""

    def __init__(self) -> None:
        """Creates a computer player with a generic name"""
        self.name = "Computer"
        pass

    def selectValue(self, value):
        """Returns a random selected value/integer for the computer player"""
        # Assigns the random value to value variable
        value += randint(1, 3)
        
        # Returns the random value/integer
        return value