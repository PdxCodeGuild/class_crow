import random

answers = ['It is certain', 'It is decidely so', 'Without a doubt', 'Yes, definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask me again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful' ]

def eight_ball():
    print('Welcome to the amazing Magic 8 Ball! Type done at anytime to exit')
    question = ''
    while question != 'done':
        question = input('Ask the 8 ball a question: ')
        print(random.choice(answers))


if __name__ == "__main__":
    eight_ball()