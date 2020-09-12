cards = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
    'BigA' : 11
}
while True:
    print('Welcome to the blackjack advice machine!')
    card1 ='A'#input('What is your first card? ').upper()
    card2 = '5' #input('What is your second card? ').upper()
    card3 ='1'#input('What is your third card? ').upper()
        
    total_cards = cards[card1] + cards[card2] + cards[card3]


    if total_cards < 17:
        print(total_cards)
        print('Hit!')  
    elif total_cards >= 17:
        print(total_cards)
        print('Stay!')
    elif total_cards == 21:
        print(total_cards)
        print('Blackjack!')
    elif total_cards > 21:
        print(total_cards)
        print('Already Busted!')
    repeat = input('Would you like to try again?: y/n ').lower()
    if repeat == 'n':
        break
    else:
        continue

