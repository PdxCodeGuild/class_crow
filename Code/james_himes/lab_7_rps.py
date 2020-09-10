import random

ai = ['rock','paper','scissors']
ai = random.choice(ai)
print('Lets play rock, paper, scissors')
gamer = input('Choose your weapon!: rock, paper, or scissors. ')
if ai == 'rock':
    if gamer == 'rock':
        print('Rock!? Its a tie!')
            
    elif gamer == 'paper':
        print('Paper!? Dang it! You got me.')
            
    elif gamer == 'scissors':
        print('HAHA scissors, Ive defeated you!')
            
    else:
        print('Enter a valid choice.')
            
if ai == 'paper':
    if gamer == 'paper':
        print('Paper!? Its a tie!')
            
    elif gamer == 'scissors':
        print('Scissors!? Dang it! You got me.')
            
    elif gamer == 'rock':
        print('Rock? Ive defeated you!')
            
    else:
        print('Please choose a valid choice.')
            
if ai == 'scissors':
    if gamer == 'scissors':
        print('Scissors!? Its a tie!')
            
    elif gamer == 'rock':
        print('Rock!? Dang it! You got me.')
            
    elif gamer == 'paper':
        print('Paper? Ive defeated you!')
            
    else:
        print('Please choose a valid choice.')
            