import random
computer_number = random.randint(1,10)
guesses = 0
while True:
    user_number = input("Guess a number between 1 and 10:")
    user_number = int(user_number)
    print(computer_number)

    if (user_number) == (computer_number):
        print("You guessed correctly!")

    else:
        guesses += 1
        print("Incorrect!")

        if user_number < computer_number:
            print('Too low')

        elif user_number > computer_number:
            print('Too high')

    print(f'You\'ve guessed {guesses} times')

    option = input('Would you like to try again? y/n ')

    if option == 'n':
        print('Thanks for playing!')
        break
