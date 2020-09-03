
import random

def main():

    #creating list of possible 8-ball outcomes
    outcomes = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Don\'t count on it',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful'
    ]

    #create a loop for the user to continue asking questions
    while True:
        #get user input
        input('Ask me a question: ')

        #getting random outcome from list
        out = random.choice(outcomes)

        #printing outcom
        print(out + '\n')

main()