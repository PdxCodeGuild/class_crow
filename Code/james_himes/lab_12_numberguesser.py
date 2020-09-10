import random
computerword=random.randint(1,10)
guesses = 0
while True:

    usernumber = input("Guess a number between 1 and 10:")
    usernumber = int(usernumber)
    print(computerword)
    if (usernumber)==(computerword):
        print("You guessed correctly!")
    else:
        guesses += 1
        print("You guessed wrong!")
        if usernumber < computerword:
            print('your too low')
        elif usernumber > computerword:
            print('Your too high')

    print(f'youve guessed {guesses} times')

    option = input('Would you like to try again? y/n ')
    if option == 'n':
        print('good luck next time!')
        break
