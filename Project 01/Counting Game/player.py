player = {'first': '','last': ''}

def getPlayerName(firstName, lastName):
    """Returns the players name"""
    player['first'] = firstName.title()
    player['last'] = lastName.title()
    return player

def getPlayerValue(value):
    """Returns the players selected value"""

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

    value = int(input("Please select from the following choices: [{}, {}, {}]: ".format(value1, value2, value3)))

    return value

def validatePlayerValue(selection, value):
    """Validates the players selected value is within parameters"""

    flag = selection > (value + 3)

    print("The selected value is not a selectable option.")

    while flag:
        selection = getPlayerValue(value)
        if selection <= (value + 3):
            value = selection
            break
        else:
            print("The selected value is not a selectable option.")

    return value
