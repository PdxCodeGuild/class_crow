class Board:
    piece_x = 'x'
    piece_o = 'o'
    piece_empty = '-'

    def __init__(self):
        self.board = [[self.piece_empty] * 3,[self.piece_empty] * 3,[self.piece_empty] * 3]
        self.winner = None

    def take_turn(self, symbol, row, column):
        # a turn is making sure no winner
        # placing the pice
        # checking for winner
        if self.winner != None:
            raise RuntimeError(f'Player {self.winner} has already won')
        if symbol != self.piece_x and symbol != self.piece_o:
            raise ValueError('Symbol must be an x or o')
        self.board[row][column] = symbol

        if self.check_for_winner():
            print('game over no more playing')

    def check_line(self, iterable, player):
        return all(map(lambda piece: piece == player, iterable))

    def check_for_winner(self):
        for player in [self.piece_x, self.piece_o]:
            # check for row three in a row
            for row in self.board:
                if self.check_line(row, player):
                    self.winner = player
                    return True
                # check for three in a column
                for column in zip(*self.board):
                    if self.check_line(column, player):
                        self.winner = player
                        return True
                # diagonals = [
                    # [self.board[0], self.board[4], self.board[8]], self.board[2], self.board[4], self.board[6]
                # ]
                # for diagonal in diagonals:
                #     if self.check_line(diagonal, player):
                #         self.winner = player
                #         return True
        return False
    
    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.board)

newBoard = Board()
print(newBoard)
print('\n')
newBoard.take_turn('o', 0, 0)
print(newBoard)
print('\n')
newBoard.take_turn('o', 0, 1)
print(newBoard)
print('\n')
newBoard.take_turn('o', 0, 2)
print(newBoard)
print('\n')
