# this code is based on the https://pythonprogramming.net/introduction-learn-python-3-tutorials/ tutorial
# I made some changes which I think makes the code better in quality or makes it resemble the way I code
# Used this for learning the syntax and to understand some things in python
import itertools


def all_same(list):
    if list[0] != '-' and list.count(list[0]) == len(list):
        return True
    else:
        return False


def game_board(game, player=0, row=0, column=0, just_display=False):
    try:
        if game[row][column] != '-':
            print("This space is occupied, try another!")
            return False

        print("    "+"    ".join([str(i) for i in range(len(game))]))
        if not just_display:
            game[row][column] = player
        for count, rowc in enumerate(game):
            print(count, rowc)
        return True
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2?")
        return False
    except Exception as e:
        print(str(e))
        return False


def win(game):
    # horizontal
    for row in game:
        if all_same(row):
            print("The winner is:", row[0])
            return True
    # vertical
    for i in range(len(game[0])):
        actual_column = []
        for row in game:
            actual_column.append(row[i])
        if all_same(actual_column):
            print("The winner is:", actual_column[0])
            return True
    # diagonal
    diags_left_right = []
    diags_right_left = []
    for i in range(len(game)):
        diags_left_right.append(game[i][i])
        diags_right_left.append(game[i][len(game)-1-i])
    if all_same(diags_left_right):
        print("The winner is:", diags_left_right[0])
        return True
    elif all_same(diags_right_left):
        print("The winner is:", diags_right_left[0])
        return True
    return False


def tic_tact_toe():
    play = True
    players = [1, 2]
    while play:
        game = [['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']]
        game_won = False
        player_cycle = itertools.cycle(['X', 'O'])
        game_board(game, just_display=True)
        while not game_won:
            current_player = next(player_cycle)
            played = False
            while not played:
                print(f"Player: {current_player}")
                column = int(input("Which column? "))
                row = int(input("Which row? "))
                played = game_board(game, current_player, row, column)

            if win(game):
                game_won = True
                again = input("The game is over, would you like to play again? (y/n) ")
                if again.lower() == "y":
                    print("restarting!")
                elif again.lower() == "n":
                    print("Byeeeee!!!")
                    play = False
                else:
                    print("Not a valid answer, but... c ya!")
                    play = False


if __name__ == '__main__':
    tic_tact_toe()
