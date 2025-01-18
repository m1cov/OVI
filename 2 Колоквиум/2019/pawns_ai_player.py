from time import sleep
import random
from copy import deepcopy

BOARD_SIZE = 3
PAWN_ACTIONS = ['a', 'l', 'r']
EMPTY_SQUARE = '\u00B7'


def check_victory(board):
    return True if 'o' in board[0] or 'x' in board[-1] else False


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


def make_move(board, move, sign):
    i, j, action = move
    board[i][j] = EMPTY_SQUARE
    if sign == 'x':
        if action == 'a':
            board[i + 1][j] = 'x'
        elif action == 'l':
            board[i + 1][j + 1] = 'x'
        elif action == 'r':
            board[i + 1][j - 1] = 'x'
    elif sign == 'o':
        if action == 'a':
            board[i - 1][j] = 'o'
        elif action == 'l':
            board[i - 1][j - 1] = 'o'
        elif action == 'r':
            board[i - 1][j + 1] = 'o'

def expand_state(board, player):
        symbol = 'x' if player == 'MAX' else 'o'
        for possible_move in find_possible_moves(board, symbol):
            new_board = deepcopy(board)
            make_move(new_board, possible_move, symbol)
            yield new_board, possible_move

def my_check_victory(board):
    if 'o' in board[0]:
        return 'o'
    elif 'x' in board[-1]:
        return 'x'           

def other_symbol(symbol):
    return 'x' if symbol == 'o' else 'o'
    
scores = {'x': 1, 'o': -1}
def minimax(board, player, alpha=-2, beta=2, depth=0):
    symbol = 'x' if player == 'MAX' else 'o'
    if check_victory(board):
        winner = my_check_victory(board)
        return scores[winner], None
    if find_possible_moves(board, symbol) == []:
        return scores[other_symbol(symbol)], None
    best_value = 2 if player == 'MIN' else -2
    best_move = None
    for child, move in expand_state(board, player):
        other_player = 'MIN' if player == 'MAX' else 'MAX'
        result, _ = minimax(child, other_player, alpha, beta, depth+1)
        if player == 'MIN':
            if result <= alpha:
                return result, best_move
            if result < beta:
                beta = result
            if result < best_value:
                best_value = result
                best_move = move
        elif player == 'MAX':
            if result >= beta:
                return result, best_move
            if result > alpha:
                alpha = result
            if result > best_value:
                best_value = result
                best_move = move
    return best_value, best_move

def next_move(board, my_sign, opponent_sign):
    player = 'MAX' if my_sign == 'x' else 'MIN'
    best_value, move = minimax(board, player)
    print(best_value)
    return move
    
    
    
    
    """
    Тука треба да го вратите следниот потег кој би го одиграле.
    Потег се состои од (локација i на пиунот кој го поместувате, цел број во опсег [0..BOARD_SIZE),
                        локација j на пиунот кој го поместувате, цел број во опсег [0..BOARD_SIZE),
                        тип на поместување - може да биде:
                            'a' - оди напред
                            'l' - преземи пиун лево од тебе
                            'r' - преземи пиун десно од тебе
    На влез добивата табла како листа од листи. Секогаш Играч 1 е 'x', а Играч 2 е 'o'.
    Внимавајте на перспективата: Играч 1 'x' секогаш почнува од горе и напаѓа надолу.
                                 Играч 2 'o' секогаш почнува од доле и напаѓа нагоре.
    Бидејќи скриптата која ја пишувате може некогаш да биде Играч 1, а некогаш Играч 2, ја гледате променливата my_sign
    за да знаете со кој знак играте вие.

    Ваша задача е да имплементирате минимакс алгоритам кој ќе оцени кој потег е најдобро да се изигра од сите можни
    потези.
    :param board:
    :param my_sign:
    :param opponent_sign:
    :return:
    """
