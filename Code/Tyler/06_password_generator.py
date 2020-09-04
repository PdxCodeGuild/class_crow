
import string
import random

while True:
    length = int(input('Enter your desired password length: '))
    lowercase = int(input('Enter your desired lowercase amount: '))
    uppercase = int(input('Enter your desired uppercase amount: '))
    number = int(input('Enter your desired number amount: '))
    special = int(input('Enter your desired special character amount: '))

    if length != (lowercase + uppercase + number + special):
        print('You\'ve exceeded your desired length. Please try again. \n')
        continue

    lowers = 'qwertyuiopasdfghjklzxcvbnm'.split()
    uppers = 'qwertyuiopasdfghjklzxcvbnm'.upper().split()
    numbers = '1234567890'.split()
    specialchars = str(string.punctuation).split()

    for char in lowers:
        lowers.append(char)

    for char in uppers:
        uppers.append(char)

    for char in numbers:
        numbers.append(char)

    for char in specialchars:
        specialchars.append(char)

    random.shuffle(lowers)
    random.shuffle(uppers)
    random.shuffle(numbers)
    random.shuffle(specialchars)

    firstpass = []
    while lowercase > 0:
        firstpass.append(lowers[lowercase])
        lowercase -+ 1
    
    while uppercase > 0:
        firstpass.append(uppers[uppercase])
        uppercase -+ 1

    while number > 0:
        firstpass.append(numbers[number])
        number -+ 1

    while special > 0:
        firstpass.append(specialchars[special])
        special -+ 1

    random.shuffle(firstpass)

    break

print(f'Your new password is: {firstpass}')


