
class Board:
    piece_x = 'x'
    piece_o = 'o'
    piece_empty = '-'

    def __init__(self):
        self.board = [[self.piece_empty]*3, [self.piece_empty]*3, [self.piece_empty]*3]
        self.winner = None

    
    def take_turn(self, symbol, row, column):
    # a turn is: making sure no winner
    # placing the piece
    # checking for winner
        if self.winner != None: 
            pass
            # raise RunTimeError(f'Player ${self.winner} has already won')
        if symbol != self.piece_x and symbol !=self.piece_o:
            raise ValueError('Symbol must be x or 0')
        self.board[row][column] = symbol

        if self.check_for_winner():
            print('game over no more playing')
    def check_line(self, iterable, player):
        return all(map(lambda piece: piece == player, iterable))

    def check_for_winner(self):
        for player in [self.piece_x, self.piece_o]:
            # check row three in a row
                for i in range(3):
                    row = self.board[i]
                    if all(item==row[0] and item != '-' for item in row):
                        self.winner = player
            # check for three in a column
                col = [self.board[j][i] for j in range(3)]
                if all(item == col[0] and item != '-' for item in col):
                    self.winner= player
            # check the diagonals
            if (self.board[2][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '-'):
                self.winner= player
            if (self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[2][0] != '-'):
                self.winner= player
                     

        return False
    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.board)


class Player:
    def __init__(self):
        numWins = 0
        

newBoard = Board()

print(newBoard)
newBoard.take_turn('o', 0, 0)
print(newBoard)

newBoard.take_turn('o', 1, 1)
print(newBoard)

newBoard.take_turn('o', 2, 2)
print(newBoard)

newBoard.take_turn('o', 2, 2)
print(newBoard)


gameOne = Board()
gameTwo = Board()

print('__________________')
print(newBoard)

# print(newBoard.board)