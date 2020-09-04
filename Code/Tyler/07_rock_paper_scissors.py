import random

while 1 == 1:
    choice = input('Choose an option (1,2,3):\n1)Rock\n2)Paper\n\
3)Scissors\n\nSelection: ')
    #print(choice)
    options = ['1','2','3']

    comp = random.choice(options)
    #print(comp)
    if choice == comp:
        print('\nIt\'s a tie!')
    elif choice == '1' and comp == '2':
        print('Paper beats Rock. You lose.')
    elif choice == '1' and comp == '3':
        print('Rock beats Scissors. You win!')
    elif choice == '2' and comp == '1':
        print('Paper beats Rock. You win!')
    elif choice == '2' and comp == '3':
        print('Scissors beats Paper. You lose.')
    elif choice == '3' and comp == '1':
        print('Rock beats Scissors. You lose.')
    elif choice == '3' and comp == '2':
        print('Scissors beats Paper. You win!')
    else:
        print('Invalid input. Please try again.\n\n')
        continue

    rematch = input('Would you like a rematch? (y/n)')
    if rematch == 'n':
        print('Goodbye...')
        break
    
    


