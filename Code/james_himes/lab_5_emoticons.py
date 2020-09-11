import random
number_of_emoticons = 0


while number_of_emoticons < 5:
    eyes = [':', ';', '=', 'x', 'X']
    nose = ['-', '^', 'o']
    mouth = [')', '(', '[', ']', 'O', 'P']
    eyes = random.choice(eyes)
    nose = random.choice(nose)
    mouth = random.choice(mouth)
    random_emoticon = eyes + nose + mouth
    print(random_emoticon)
    number_of_emoticons += 1


    

