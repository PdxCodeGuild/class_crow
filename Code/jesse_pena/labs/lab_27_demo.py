# import argparse

class Piece:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color[0]

    # necessary for checking wins
    # checks types to ensure they're comparable
    def __eq__(self, other):
        if type(other) is Piece:
            if self.color == other.color:
                return True

class GameBoard:
    DEPTH = 6
    WIDTH = 7

    def __init__(self):
        self.board = [['0' for col in range(self.WIDTH)] for row in range(self.DEPTH)]
    
    def print_board(self):
        for row in range(len(self.board)):
            for cell in self.board[row]:
                print(cell, end='|')
            print()
        print()

    def get_height(self, position):
        for i in range(self.DEPTH-1, -1, -1):
            if self.board[i][position] == '0':
                return i # position the piece will fall to
        return False # column is full

    def place_piece(self, piece_color, position):
        height = self.get_height(position)
        if type(height) is bool:
            print('Column full, choose another')
            return False
        self.board[height][position] = Piece(piece_color)

    def check_win(self):
        for i in range(self.DEPTH - 1, -1, -1):

            for j in range(self.WIDTH):

                # checks rows in chunks of 4
                if j < self.WIDTH - 3:
                    chunk = self.board[i][j:j+4]

                    if all(item == self.board[i][j] and item != '0' for item in chunk):
                        print(f'${self.board[i][j]} won!')
                        return True
                        
                # check for vertical win
                if i < self.DEPTH - 3:
                    chunk = []
                    chunk.append(self.board[i][j])
                    chunk.append(self.board[i+1][j])
                    chunk.append(self.board[i+2][j])
                    chunk.append(self.board[i+3][j])

                    if all(item == self.board[i][j] and item != '0' for item in chunk):
                        print(f'${self.board[i][j]} won!')
                        return True

                # check for diagonal win
                if i < self.DEPTH-3 and j < self.WIDTH-3:
                    chunk = []
                    chunk.append(self.board[i][j:j+4])
                    chunk.append(self.board[i+1][j:j+4])
                    chunk.append(self.board[i+2][j:j+4])
                    chunk.append(self.board[i+3][j:j+4])

                    if chunk[0][0] == chunk[1][1] == chunk[2][2] == chunk[3][3] and chunk[0][0] != '0':
                        print(f'${chunk[0][0]} won!')
                        return True
                        
                    elif chunk[3][0] == chunk[1][2] == chunk[2][1] == chunk [0][3] and chunk[3][0] != '0':
                        print(f'${chunk[3][0]} won!')
                        return True

    
    def is_full(self):
        for row in self.board:
            if any(item=='0' for item in row):
                return False
        return True

    def game_over(self):
        return self.check_win()

# def main():
#     with open('/home/jpchato/class_crow/Code/jesse_pena/connect-four-moves.txt', 'r') as f:
#         moves = f.read().split()
#     board = GameBoard()

#     for i, move in enumerate(moves):
#         current_turn = 'Y' if i % 2 == 0 else 'R'
#         board.place_piece(current_turn, int(move) - 1)
    
#     board.print_board()
#     board.check_win()

if __name__ == "__main__":
    # main()
    while True:
        board = GameBoard()
        player1 = 'Y'
        player2 = 'R'
        game_round = 1

        while board.game_over != True:
            current_player = player1 if game_round %2 else player2
            move = input(f'{current_player}: Enter your move: ')
            try:
                move = int(move)
                if 1 <= move <=7:
                    move = board.place_piece(current_player, move-1)
                board.print_board()
                game_round += 1
                board.game_over()
            except(ValueError, IndexError):
                print('Invalid column choice')
            