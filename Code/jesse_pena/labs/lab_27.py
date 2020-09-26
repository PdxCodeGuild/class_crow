class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Game():
    piece_x = 'x'
    piece_o = 'o'
    piece_empty = '-'

    def __init__(self):
        self.board = [[self.piece_empty] * 7,[self.piece_empty] * 7,[self.piece_empty] * 7, [self.piece_empty] * 7,[self.piece_empty] * 7,[self.piece_empty] * 7, [self.piece_empty] * 7]

    def get_height(self, position):
        '''
        returns int of how many pieces occupy a column
        '''
        column_count = []

        for column in self.board:
            if column[position] == 'o' or column[position] == 'x':
                    column_count.append(column)

        where_to_place = 0

        if len(column_count) == 0:
            where_to_place = -1
        elif len(column_count)  == 1:
            where_to_place = 5
        elif len(column_count)  == 2:
            where_to_place = 4
        elif len(column_count)  == 3:
            where_to_place = 3
        elif len(column_count)  == 4:
            where_to_place = 2
        elif len(column_count)  == 5:
            where_to_place = 1
        elif len(column_count)  == 6:
            where_to_place = 0

        # print(f'The height of the the {position} column is {len(column_count)} pieces high')
        return(where_to_place)

    def move(self, player, position):
        '''
        adds a player token to a column after figuring out the current height of the column
        '''
        self.board[new_game.get_height(position)][position] = player
        

    # def calc_winner(self):
    #     '''
    #     returns true if a match (four in a row) is found

    #     '''
    #     pass

    # def is_full(self):
    #     pass

    # def is_game_over(self):
    #     pass


# ************************************* FILE GAME ***********************
if __name__ == "__main__":
    new_game = Game()
    f = open("/home/jpchato/class_crow/Code/jesse_pena/connect-four-moves.txt", "r")
    counter = 0
    for line in f:
        counter += 1
        if counter % 2 == 0:
            new_game.move('x', int(line) - 1 )
            for line in new_game.board:
                print(line)
            print('*'*100)
        else:
            new_game.move('o', int(line) - 1)
            for line in new_game.board:
                print(line)
            print('*'*100)
# ********************************* FILE GAME *********************

# new_game = Game()
# new_game.move('x', 1 )
# new_game.move('o', 0)
# new_game.move('x', 2)
# new_game.move('o', 0)
# new_game.move('x', 3)
# new_game.move('o', 0)
# new_game.move('x', 4)
# for line in new_game.board:
#     print(line)
# new_game.get_height(1)
# new_game.calc_winner()

