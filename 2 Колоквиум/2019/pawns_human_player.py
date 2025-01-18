BOARD_SIZE = 3
PAWN_ACTIONS = ['a', 'l', 'r']
EMPTY_SQUARE = '\u00B7'


def read_user_input(board, my_sign): # додадов да проверува дали нема повеќе потези за поместување
    if find_possible_moves(board, my_sign) == []:
        return None
    message = input('Внесете потег: ').split()
    while True:
        try:
            i, j, action = int(message[0]), int(message[1]), message[2]
            if 0 <= i < BOARD_SIZE and 0 <= j < BOARD_SIZE and action in PAWN_ACTIONS:
                return i, j, action
            message = input('Лоша синтакса. pawn_i pawn_j pawn_action: ').split()
        except (IndexError, ValueError):
            message = input('Лоша синтакса. pawn_i pawn_j pawn_action: ').split()


def next_move(board, my_sign, opponent_sign):
    return read_user_input(board, my_sign)


def find_possible_moves(board, sign):
    sign_locations = [(i, j) for i, row in enumerate(board) for j, square in enumerate(row) if board[i][j] == sign]
    possible_moves = []
    if sign == 'x':
        for sign_i, sign_j in sign_locations:
            if board[sign_i + 1][sign_j] == EMPTY_SQUARE:
                possible_moves.append((sign_i, sign_j, 'a'))
            if sign_j > 0 and board[sign_i + 1][sign_j - 1] == 'o':
                possible_moves.append((sign_i, sign_j, 'r'))
            if sign_j < BOARD_SIZE - 1 and board[sign_i + 1][sign_j + 1] == 'o':
                possible_moves.append((sign_i, sign_j, 'l'))
    elif sign == 'o':
        for sign_i, sign_j in sign_locations:
            if board[sign_i - 1][sign_j] == EMPTY_SQUARE:
                possible_moves.append((sign_i, sign_j, 'a'))
            if sign_j > 0 and board[sign_i - 1][sign_j - 1] == 'x':
                possible_moves.append((sign_i, sign_j, 'l'))
            if sign_j < BOARD_SIZE - 1 and board[sign_i - 1][sign_j + 1] == 'x':
                possible_moves.append((sign_i, sign_j, 'r'))
    return possible_moves