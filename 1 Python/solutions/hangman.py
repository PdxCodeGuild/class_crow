import random

def word_chooser():
    open('/home/jpchato/class_crow/Code/jesse_pena/lectures/english.txt', 'r')
    f = open('/home/jpchato/class_crow/Code/jesse_pena/lectures/english.txt', 'r')
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
        print(random_word)
        counter += 1
        guess = input('Whats your guess? ')
        if guess in guesses:
            guess = input('You already guessed that! Try again. ')
        guesses.append(guess)
        for i in range(len(random_word)):
            if guess == random_word[i]:
                compare[i] = guess 
                # print(random_word)
                # print(''.join(compare))
                # if random_word == ''.join(compare):
                #     print('Success')
                if '_' not in compare:
                    print('success')
                    counter = 10
        # print(compare)
    print('You\'ve reached 10 guesses')
    print(random_word)
    play_again = input('Do you want to play again? ')
    play_again.lower()
    if play_again == 'yes' or 'y':
        hangman()


hangman()           

>>>>>>> 3b728005f260edec20b74119249ebbaae94c2d90


list = ['1','2']

hello = ''.join(list)
print(hello)
