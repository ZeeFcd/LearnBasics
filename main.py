# this code is based on the https://pythonprogramming.net/introduction-learn-python-3-tutorials/ tutorial
# I made some changes which I think makes the code better in quality or makes it resemble the way I code
# Used this for learning the syntax and to understand some things in python
import itertools


def all_same(list):
    if list[0] != '-' and list.count(list[0]) == len(list):
        return True
    else:
        return False


def game_board_visual(game):
    print("    " + "    ".join([str(i) for i in range(len(game))]))
    for count, rowc in enumerate(game):
        print(count, rowc)


def game_board(game, player, row, column):
    try:
        if game[int(row)][int(column)] != '-':
            print("This space is occupied, try another!")
            return False
        game[int(row)][int(column)] = player
        return True
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2?")
        return False
    except Exception as e:
        print(str(e))
        return False


def win(game):

    def horizontal():
        for row in game:
            if all_same(row):
                return True

    def vertical():
        for i in range(len(game[0])):
            actual_column = []
            for row in game:
                actual_column.append(row[i])
            if all_same(actual_column):
                return True

    def diagonal():
        diags_left_right = []
        diags_right_left = []
        for i in range(len(game)):
            diags_left_right.append(game[i][i])
            diags_right_left.append(game[i][len(game) - 1 - i])
        if all_same(diags_left_right):
            return True
        elif all_same(diags_right_left):
            return True

    if horizontal():
        return True
    elif vertical():
        return True
    elif diagonal():
        return True

    return False


def game_ending():
    again = input("The game is over, would you like to play again? (y/n) ")
    if again.lower() == "y":
        print("restarting!")
        return True
    elif again.lower() == "n":
        print("Byeeeee!!!")
        return False
    else:
        print("Not a valid answer, but... c ya!")
        return False


def tic_tact_toe():
    play = True
    while play:
        game = [['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']]
        game_ended = False
        player_cycle = itertools.cycle(['X', 'O'])
        step_number = 0
        while not game_ended:
            current_player = next(player_cycle)
            played = False
            while not played:
                game_board_visual(game)
                print(f"Player: {current_player}")
                column = input("Which column? ")
                row = input("Which row? ")
                played = game_board(game, current_player, row, column)
                step_number = step_number + 1
            if win(game):
                game_ended = True
                print("The winner is:", current_player)
                play = game_ending()
            elif step_number == 9:
                play = game_ending()


if __name__ == '__main__':
    tic_tact_toe()
