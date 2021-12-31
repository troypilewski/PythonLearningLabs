player = {'first': '','last': ''}

def getPlayerName(firstName, lastName):
    """Returns the players name"""
    player['first'] = firstName.title()
    player['last'] = lastName.title()
    return player

def getPlayerValue(value):
    """Returns the players selected value"""
    value = int(input("Please select from the following choices: [{}, {}, {}]: ".format(value + 1, value + 2, value + 3)))
    return value
