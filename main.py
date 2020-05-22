def create_matrix() -> list:
    """
    Creates the matrix of the game
    """
    game = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    return game


def print_matrix(matrix: list):
    print('---------')
    for i in range(3):
        print('| ', end='')
        for j in range(3):
            if matrix[i][j] == 'X' or matrix[i][j] == 'O':
                print(matrix[i][j] + ' ', end='')

            else:
                print('  ', end='')

        print('|')

    print('---------')


def write_in_matrix(matrix: list, column: int, row: int, player: str):
    matrix[row - 1][column - 1] = player


def check_game_finished(matrix: list) -> bool:
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            print('Player', matrix[i][0], 'won')
            return True

    if (matrix[0][1] == matrix[1][1] == matrix[2][1] or
            matrix[0][0] == matrix[1][1] == matrix[2][2] or
            matrix[0][2] == matrix[1][1] == matrix[2][0]):

        print('Player', matrix[0][1], 'won')

        return True

    if matrix[0][0] == matrix[1][0] == matrix[2][0]:
        print('Player', matrix[0][0], 'won')

        return True

    if matrix[0][2] == matrix[1][2] == matrix[2][2]:
        print('Player', matrix[0][0], 'won')

        return True

    filled = 0

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 'O' or matrix[i][j] == 'X':
                filled += 1

    if filled == 9:
        print('TIE')
        return True

    return False


def valid_input(matrix: list, column: str, row: str) -> bool:
    try:
        column = int(column)
        row = int(row)
        matrix[row-1][column-1]

        return True

    except ValueError:
        return False

    except IndexError:
        return False

    except TypeError:
        return False


def possible_to_play(matrix: list, column: int, row: int):
    if matrix[row-1][column-1] == 'X' or matrix[row-1][column-1] == 'O':
        return False

    return True


if __name__ == '__main__':
    GAME = create_matrix()
    FINISHED = check_game_finished(GAME)

    PLAYER_O = [True, 'O']
    PLAYER_X = [False, 'X']

    while not FINISHED:
        print_matrix(GAME)
        COL, RO = map(int, input('Your turn: ').split())

        while not possible_to_play(GAME, COL, RO):
            print('INVALID\nTRY AGAIN')
            COL, RO = map(int, input('Your turn: ').split())

        COL = int(COL)
        RO = int(RO)
        if PLAYER_O[0]:
            write_in_matrix(GAME, COL, RO, PLAYER_O[1])
            PLAYER_O[0] = False
            PLAYER_X[0] = True

        else:
            write_in_matrix(GAME, COL, RO, PLAYER_X[1])
            PLAYER_O[0] = True
            PLAYER_X[0] = False

        FINISHED = check_game_finished(GAME)

    print_matrix(GAME)
