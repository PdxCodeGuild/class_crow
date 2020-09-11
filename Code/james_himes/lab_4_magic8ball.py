import random

while True:
    answers = ['It is certain', 'It is decidedly so', 'Without a doubt',
     'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely',
      'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again',
       'Ask again later', 'Better not tell you now', 'Cannot predict now',
        'Concentrate and ask again', 'Dont count on it', 'My reply is no',
         'My sources say no', 'Outlook not so good', 'Very doubtful'
    ]
    print('Ask me a question.')
    input()
    print (random.choice(answers))
    repeat = input('Would you like to play again? y/n? ').lower()
    if repeat == 'n':
        break
    elif repeat == 'y':
        continue



