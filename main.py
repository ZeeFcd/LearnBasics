def game_board(game, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game[row][column] = player
        for count, row in enumerate(game):
            print(count, row)
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2?")
    except Exception as e:
        print(str(e))


def win(game):
    for row in game:
        if row[0] != 0 and row.count(row[0]) == len(row):
            print("The winner is:", row[0])

    for i in range(len(game[0])):
        actual_column = []
        for row in game:
            actual_column.append(row[i])
        if actual_column[0] != 0 and actual_column.count(actual_column[0]) == len(actual_column):
            print("The winner is:", actual_column[0])


def tic_tact_toe():
    game_map = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    game_board(game_map, just_display=True)
    game_board(game_map, player=2, row=1, column=0)
    game_board(game_map, player=1, row=3, column=1)
    win(game_map)


if __name__ == '__main__':
    tic_tact_toe()