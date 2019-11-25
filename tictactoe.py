# write your code here

symbols = list("_________")
print("---------")
print("| " + symbols[0] + " " + symbols[1] + " " + symbols[2] + " |")
print("| " + symbols[3] + " " + symbols[4] + " " + symbols[5] + " |")
print("| " + symbols[6] + " " + symbols[7] + " " + symbols[8] + " |")
print("---------")

impossible = False
game_finished = False

string = "X"
congrats = "{} wins"
winner = ""
winner_found = 0

coordinates = ""
player = "X"
place = -1
dict_of_coordinates = [[1, 3], [2, 3], [3, 3], [1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [3, 1]]
played = False
valid_input = False

while not game_finished:

    def are_in_bounds():
        if 1 <= int(coordinates[0]) <= 3 and 1 <= int(coordinates[1]) <= 3:
            return True
        else:
            print("Coordinates should be from 1 to 3!")
            return False


    def are_integers():
        for i in coordinates:
            if i.isdigit():
                # are_in_bounds()
                return are_in_bounds()
            else:
                print("You should enter numbers!")
                return False


    while not played:
        while not valid_input:  # number of requirements to satisfy (int, in bounds)
            coordinates = input("Enter the coordinates: ").split()
            valid_input = are_integers()
        valid_input = False
        coordinates = [int(x) for x in coordinates]
        place = dict_of_coordinates.index(coordinates)
        if symbols[place] == "_":
            symbols[place] = player
            print("---------")
            print("| " + symbols[0] + " " + symbols[1] + " " + symbols[2] + " |")
            print("| " + symbols[3] + " " + symbols[4] + " " + symbols[5] + " |")
            print("| " + symbols[6] + " " + symbols[7] + " " + symbols[8] + " |")
            print("---------")
            played = True
        else:
            print("This cell is occupied! Choose another one!")
    played = False
    if player == "X":
        player = "O"
    else:
        player = "X"

    if symbols.count("X") > symbols.count("O") + 1:
        print("Impossible")
        impossible = True
        game_finished = True
    elif symbols.count("O") > symbols.count("X") + 1:
        print("Impossible")
        impossible = True
        game_finished = True

    if not impossible:
        for num in range(2):
            if symbols[0] == string:
                if symbols[1] == string and symbols[2] == string:
                    winner = string
                    winner_found += 1
                if symbols[3] == string and symbols[6] == string:
                    winner = string
                    winner_found += 1
                if symbols[4] == string and symbols[8] == string:
                    winner = string
                    winner_found += 1
            if symbols[1] == string:
                if symbols[4] == string and symbols[7] == string:
                    winner = string
                    winner_found += 1
            if symbols[2] == string:
                if symbols[5] == string and symbols[8] == string:
                    winner = string
                    winner_found += 1
                if symbols[4] == string and symbols[6] == string:
                    winner = string
                    winner_found += 1
            if string == "X":
                string = "O"
            else:
                string = "X"

        if winner is not "" and winner_found != 0 and winner_found < 2:
            print(congrats.format(winner))
            game_finished = True

        if winner_found == 0:
            if "_" in symbols:
                game_finished = False
            else:
                print("Draw")
                game_finished = True
        elif winner_found >= 2:
            print("Impossible")
            game_finished = True
