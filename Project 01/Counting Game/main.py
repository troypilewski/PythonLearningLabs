import player
import computer

play = True

playername = player.getPlayerName(
        input("What is your first name? "), input("What is you last name? ")
    )

while play:
    message = input("{}, Do you want to play a game? [yes/no]: ".format(playername["first"]))

    if message == "yes":
        play = True
        rules = "Take turns with the computer. Select one of the provided values during your turn."
        rules += "\nThe player to select 20 first wins the game."
        print(rules)
    else:
        play = False
        break

    message = input("{}, Do you want to go first? [yes/no]: ".format(playername["first"]))

    if message == "yes":
        value = 0
        print("The starting value is {}.".format(value))
        while value < 20:
            # print("The current value is {}.".format(value))
            selection = player.getPlayerValue(value)
            value = player.validatePlayerValue(selection, value)
            print("{}'s selected value is {}.".format(playername["first"],value))
            if value >= 20:
                print("{} won the game.".format(playername["first"]))
                print("Thank you for playing, {}".format(playername["first"]))
                break
            value = computer.getComputerValue(value)
            print("The computer's selected value is {}.".format(value))
            if value >= 20:
                print("The Computer wan the game.")
                print("Thank you for playing, {}".format(playername["first"]))
                break
    else:
        value = 0
        print("The starting value is {}.".format(value))
        while value < 20:
            print("The current value is {}.".format(value))
            value = computer.getComputerValue(value)
            print("The computer's selected value is {}.".format(value))
            if value >= 20:
                print("The Computer wan the game.")
                break
            value = player.getPlayerValue(value)
            print("{}'s selected value is {}.".format(playername["first"],value))
            if value >= 20:
                print("{} won the game.".format(playername["first"]))
                break
