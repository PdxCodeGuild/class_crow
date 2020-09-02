import random

def word_chooser():
    open('english.txt', 'r')
    f = open('english.txt', 'r')
    word_list = []
    words = f.read().split('\n')
    for word in words:
        if len(word) <= 5:
            word_list.append(word)
    random_word = random.choice(word_list)
    return random_word

def hangman():
    random_word = word_chooser()
    counter = 0
    compare = []
    for letter in random_word:
        compare.append('_')
    guesses = []
    while counter < 10:
        counter += 1
        guess = input('Whats your guess?')
        if guess in guesses:
            guess = input('You already guessed that! Try again.')
        guesses.append(guess)
        for i in range(len(random_word)):
            if guess == random_word[i]:
                compare[i] = guess 
        print(compare)

hangman()           




