from players import Player
from players import Computer

competitors = []

numberOfCompetitors = int(input("How many players: [1 / 2]: "))

for player in range(numberOfCompetitors):
    print("Player {}, answer the following questions...".format(player +1))
    firstName = input("What is your first name? ")
    lastName = input("What is your last name? ")
    competitor = Player(first=firstName, last=lastName)
    print(competitor.getProperName())
    competitors.append(competitor)

# print(len(competitors))

flag = input("Do you want to read the rules? [yes / no] ")

if flag == "yes":
    rules = "Take turns with your opponent. Select one of the provided values during your turn."
    rules += "\nThe player to reach 20 first wins."
    print(rules)

if len(competitors) == 2:
    token = True
    while token:
        value = 0
        print("The current value is: {}".format(value))
        while value <= 20:
            for competitor in competitors:
                print("It is {}'s turn.".format(competitor.first.title()))
                selection = competitor.selectValue(value)
                value = competitor.validateSelectedValue(selection, value)
                print("{} selected the value: {}".format(competitor.first.title(), value))
                if value == 20:
                    print("{} won the game.".format(competitor.first.title()))
                    print("Thank you playing.")
                    break

    play = input("Do you want to play again? [yes / no] ")
    if play == "yes":
        token = True
    else:
        token = False

else:
    token = True
    while token:
        computer = Computer()
        value = 0
        print("The current value is: {}".format(value))
        while value <= 20:
            selection = competitors[0].selectValue(value)
            value = competitors[0].validateSelectedValue(selection, value)
            print("{} selected the value: {}".format(competitors[0].first.title(), value))
            if value == 20:
                print("{} won the game.".format(competitors[0].first.title()))
                print("Thank you for playing, {}".format(competitors[0].first.title()))
                break
            value = computer.selectValue(value)
            print("The {} selected the value: {}".format(computer.name.title(), value))
            if value == 20:
                print("The {} won the game.".format(computer.name.title()))
                break
        
        play = input("Do you want to play again? [yes / no] ")
        if play == "yes":
            token = True
        else:
            token = False