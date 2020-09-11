deck = {
    'A': 1, 
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9, 
    '10': 10, 
    'J': 10, 
    'Q': 10, 
    'K': 10}

def blackjack():
    print(deck.keys())
    card_1 = input('What\'s your first card?' ).upper()
    card_2 = input('What\'s your second card?' ).upper()
    card_3 = input('What\'s your third card?' ).upper()
    # card_1 = deck['A']
    # card_2 = deck['2']
    # card_3 = deck['3']

    initial_hand = deck.get(card_1) + deck.get(card_2) + deck.get(card_3)

    if int(initial_hand) < 17:
        print(initial_hand, 'Hit')
        
    elif 21 > initial_hand >= 17:
        print(initial_hand, 'Stay')

    elif initial_hand == 21:
        print(initial_hand, 'Blackjack')
        
    elif initial_hand > 21:
        print(initial_hand, 'Bust')

def blackjack_aces():
    deck = {
    'A': 1, 
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9, 
    '10': 10, 
    'J': 10, 
    'Q': 10, 
    'K': 10
    }

    hand = []
    card_1 = input('What\'s your first card?' ).upper()
    card_2 = input('What\'s your second card?' ).upper()
    card_3 = input('What\'s your third card?' ).upper()
    hand.append(card_1)

    # card_1 = deck['A']
    # card_2 = deck['2']
    # card_3 = deck['3']

    initial_hand = deck.get(card_1) + deck.get(card_2) + deck.get(card_3)

    if 'A' in hand:
        print('hi')

    if int(initial_hand) < 17:
        print('Hit')
        
    elif 21 > initial_hand >= 17:
        print('Stay')

    elif initial_hand == 21:
        print('Blackjack')
        
    elif initial_hand > 21:
        print('Bust')


if __name__ == "__main__":
    # blackjack()
    blackjack_aces()