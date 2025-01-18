from copy import deepcopy
import pawns_ai_player as player1
import pawns_ai_player as player2


class Board:
    def __init__(self, player_1, player_2, board_size=6, empty_square='\u00B7'):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_sign = 'x'
        self.player_2_sign = 'o'
        self.board_size = board_size
        self.empty_square = empty_square
        self.board = [[self.empty_square] * self.board_size for _ in range(self.board_size)]
        self.board[0] = [self.player_1_sign] * self.board_size
        self.board[-1] = [self.player_2_sign] * self.board_size

    def draw_board(self):
        print(' ' * 2, end='')
        for index in range(self.board_size):
            print(' ', index, end='')
        print()
        for i, row in enumerate(self.board):
            print(i, '| ', end='')
            for j, element in enumerate(row):
                print(element, ' ' if j + 1 < len(row) else '', end='')
            print('|', 'Играч 1' if i == 0 else 'Играч 2' if i == self.board_size - 1 else '')
        print()

    def player_1_make_move(self, move):
        i, j, action = move
        self.board[i][j] = self.empty_square
        if action == 'a':
            self.board[i + 1][j] = self.player_1_sign
        elif action == 'l':
            self.board[i + 1][j + 1] = self.player_1_sign
        elif action == 'r':
            self.board[i + 1][j - 1] = self.player_1_sign

    def player_2_make_move(self, move):
        i, j, action = move
        self.board[i][j] = self.empty_square
        if action == 'a':
            self.board[i - 1][j] = self.player_2_sign
        elif action == 'l':
            self.board[i - 1][j - 1] = self.player_2_sign
        elif action == 'r':
            self.board[i - 1][j + 1] = self.player_2_sign

    def find_possible_moves(self, sign):
        sign_locations = [(i, j) for i, row in enumerate(self.board) for j, square in enumerate(row)
                          if self.board[i][j] == sign]
        possible_moves = []
        if sign == self.player_1_sign:
            for sign_i, sign_j in sign_locations:
                if self.board[sign_i + 1][sign_j] == self.empty_square:
                    possible_moves.append((sign_i, sign_j, 'a'))
                if sign_j > 0 and self.board[sign_i + 1][sign_j - 1] == self.player_2_sign:
                    possible_moves.append((sign_i, sign_j, 'r'))
                if sign_j < self.board_size - 1 and self.board[sign_i + 1][sign_j + 1] == self.player_2_sign:
                    possible_moves.append((sign_i, sign_j, 'l'))
        elif sign == self.player_2_sign:
            for sign_i, sign_j in sign_locations:
                if self.board[sign_i - 1][sign_j] == self.empty_square:
                    possible_moves.append((sign_i, sign_j, 'a'))
                if sign_j > 0 and self.board[sign_i - 1][sign_j - 1] == self.player_1_sign:
                    possible_moves.append((sign_i, sign_j, 'l'))
                if sign_j < self.board_size - 1 and self.board[sign_i - 1][sign_j + 1] == self.player_1_sign:
                    possible_moves.append((sign_i, sign_j, 'r'))
        return possible_moves

    def play(self):
        board.draw_board()
        while True:
            move = self.player_1.next_move(deepcopy(self.board), self.player_1_sign, self.player_2_sign)
            if move == None:
                print('Играч 2 победи')
                break
            self.player_1_make_move(move)
            board.draw_board()
            if self.check_victory():
                print('Играч 1 победи')
                break
            move = self.player_2.next_move(deepcopy(self.board), self.player_2_sign, self.player_1_sign)
            if move == None:
                print('Играч 1 победи')
                break
            self.player_2_make_move(move)
            board.draw_board()
            if self.check_victory():
                print('Играч 2 победи')
                break


    def check_victory(self):
        return True if self.player_2_sign in self.board[0] or self.player_1_sign in self.board[-1] else False

        
    
board = Board(player1, player2, board_size=3)
board.play()
