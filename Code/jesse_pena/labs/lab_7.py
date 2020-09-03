import random

def rock_paper_scissors():
    while True:
        choice = input('Do you choose rock, paper, or scissors? Type exit at any time to exit the game ')
        choice = choice.lower()
        rps = ['rock', 'paper', 'scissors']
        random_choice = random.choice(rps)

        if choice == random_choice:
            print(f'You selected {choice} and the computer selected {random_choice}. It\'s a tie')

        elif choice =='rock' and random_choice=='paper':
            print(f'You selected {choice} and the computer selected {random_choice}. You lose.')

        elif choice == 'rock' and random_choice=='scissors':
            print(f'You selected {choice} and the computer selected {random_choice}. You win')
            
        elif choice == 'paper' and random_choice=='rock':
            print(f'You selected {choice} and the computer selected {random_choice}. You win.')

        elif choice == 'paper' and random_choice=='scissors':
            print(f'You selected {choice} and the computer selected {random_choice}. You lose.')

        elif choice == 'scissors' and random_choice=='rock':
            print(f'You selected {choice} and the computer selected {random_choice}. You lose.')

        elif choice == 'scissors' and random_choice=='paper':
            print(f'You selected {choice} and the computer selected {random_choice}. You win.')

        elif choice == 'exit':
            return False

if __name__ == "__main__":
    rock_paper_scissors()