class Player:
    def __init__(self,name,color):
        pass

class Game:
    def __init__(self, board):
        pass

    def get_height(self,position):
        pass
    
    def move(self, player, position):
        pass

    def calc_winner(self):
        pass

    def is_full():
        pass

    def is_game_over():
        pass

def main():
    #getting user input
    print('Welcome to connect four!\n')
    player1_name = input('Who is player 1?: ')
    player1_color = input('What color do you want? (yellow/red): ')
    player1 = Player(player1_name,player1_color)

    player2_name = input('Who is player 2?: ')
    player2_color = input('What color do you want? (yellow/red): ')
    player2 = Player(player2_name,player2_color)

    #initial blank board for game
    rows = [['x','x','x','x','x','x','x'],['x','x','x','x','x','x','x'],['x','x','x','x','x','x','x'],['x','x','x','x','x','x','x'],['x','x','x','x','x','x','x'],['x','x','x','x','x','x','x']]

    # with open('moves.txt', 'r') as file:
    #     file = file.read().splitlines()

    #creating game loop
    while True:

        #printing the board
        count = 0
        rows.reverse()
        for item in rows:
            print(str(item).replace("'", '').replace(',', '').replace('[', '').replace(']', ''))
            count += 1

        move = int(input('Player1: Pick a column to place your piece: ')) - 1

        #assigning players piece in desired row and checking if there is a winner
        y_count = 0
        r_count = 0
        rows.reverse()
        for item in rows:
            if item[move] == 'x':
                item[move] = player1_color
                if item[move] == 'y':
                    r_count = 0
                    y_count += 1
                    if y_count == 4:
                        print('Yellow is the winner!')
                        break
                elif item[move] == 'r':
                    y_count = 0
                    r_count += 1
                    if r_count == 4:
                        print('Red is the winner!')
                        break
                break
            if item[move] == 'y':
                r_count = 0
                y_count += 1
                if y_count == 4:
                    print('Yellow is the winner!')
                    break
            elif item[move] == 'r':
                y_count = 0
                r_count += 1
                if r_count == 4:
                    print('Red is the winner!')
                    break
        
                
        #checking rows for a pattern of 4
        y_count = 0
        r_count = 0

        for item in rows:
            for pos in item:
                if pos == 'y':
                    r_count = 0
                    y_count += 1
                    if y_count == 4:
                        print('Yellow is the winner!')
                        break
                elif pos == 'r':
                    y_count = 0
                    r_count += 1
                    if r_count == 4:
                        print('Red is the winner!')
                        break
            y_count = 0
            r_count = 0

        
        

        #printing the board
        count = 0
        rows.reverse()
        for item in rows:
            print(str(item).replace("'", '').replace(',', '').replace('[', '').replace(']', ''))
            count += 1

        move = int(input('Player2: Pick a column to place your piece: ')) - 1

        #adding players piece to the board and checking for a winner in the columns
        y_count = 0
        r_count = 0
        rows.reverse()
        for item in rows:
            if item[move] == 'x':
                item[move] = player2_color
                if item[move] == 'y':
                    r_count = 0
                    y_count += 1
                    if y_count == 4:
                        print('Yellow is the winner!')
                        break
                elif item[move] == 'r':
                    y_count = 0
                    r_count += 1
                    if r_count == 4:
                        print('Red is the winner!')
                        break
                break
            elif item[move] == 'y':
                r_count = 0
                y_count += 1
                if y_count == 4:
                    print('Yellow is the winner!')
                    break
            elif item[move] == 'r':
                y_count = 0
                r_count += 1
                if r_count == 4:
                    print('Red is the winner!')
                    break
        
        #checking rows for a winning pattern
        y_count = 0
        r_count = 0

        for item in rows:
            for pos in item:
                if pos == 'y':
                    r_count = 0
                    y_count += 1
                    if y_count == 4:
                        print('Yellow is the winner!')
                        break
                elif pos == 'r':
                    y_count = 0
                    r_count += 1
                    if r_count == 4:
                        print('Red is the winner!')
                        break
            y_count = 0
            r_count = 0

            

        

#running main
main()


