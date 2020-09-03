import random
open('lectures/english.txt', 'r')
f = open('lectures/english.txt', 'r')
word_list = []
words = f.read().split('\n')
for word in words:
    if len(word) <= 5:
        word_list.append(word)

random_word = random.choice(word_list)

counter = 0

guess_list = []
while counter < 10:
    counter += 1
    guess = input('What\'s your guess? ') 
    if guess in random_word:
        guess_list.append(guess)
print(guess_list)




# print(random_word)

# guess = input('Guess a letter: ')
# guess_list = []

# if guess in random_word:
#     guess_list.append(guess)
#     if guess not in random_word:
#         guess = input('Guess a letter' + '_'*)
#     if len(guess_list) == len(random_word):
#         print('success')
