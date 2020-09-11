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
    hand.append(card_2)
    hand.append(card_3)

    # card_1 = deck['A']
    # card_2 = deck['2']
    # card_3 = deck['3']

    initial_hand = deck.get(card_1) + deck.get(card_2) + deck.get(card_3)
    print(hand)

    if 'A' in hand:
        deck['A'] = 11
        initial_hand = deck.get(card_1) + deck.get(card_2) + deck.get(card_3)
        # print(initial_hand)
        if initial_hand == 33:
            initial_hand = 13
            print(initial_hand, 'hit')

        elif initial_hand == 32:
            initial_hand = 12
            print(initial_hand, 'hit')

        elif initial_hand == 31:
            initial_hand = 21
            print(initial_hand, 'Blackjack')

        elif initial_hand == 30:
            initial_hand = 20
            print(initial_hand, 'Stay')

        elif initial_hand == 29:
            initial_hand = 19
            print(initial_hand, 'Stay')

        elif initial_hand == 28:
            initial_hand = 18
            print(initial_hand, 'Stay')

        elif initial_hand == 27:
            initial_hand = 17
            print(initial_hand, 'Stay')

        elif initial_hand == 26:
            initial_hand = 16
            print(initial_hand, 'Hit')

        elif initial_hand == 25:
            initial_hand = 15
            print(initial_hand, 'Hit')

        elif initial_hand == 24:
            initial_hand = 14
            print(initial_hand, 'Hit')

        elif initial_hand == 21:
            print(initial_hand, 'Blackjack')

        elif initial_hand < 21:

            if int(initial_hand) < 17:
                print(initial_hand, 'Hit')
            
            elif 21 > initial_hand >= 17:
                print(initial_hand, 'Stay')

            elif initial_hand == 21:
                print(initial_hand, 'Blackjack')
            
            elif initial_hand > 21:
                print(initial_hand, 'Bust')

        elif 30 > initial_hand > 21:

            deck['A'] = 1
            initial_hand = deck.get(card_1) + deck.get(card_2) + deck.get(card_3)

            if int(initial_hand) < 17:
                print(initial_hand, 'Hit')
            
                if 21 > initial_hand >= 17:
                    print(initial_hand, 'Stay')

                elif initial_hand == 21:
                    print(initial_hand, 'Blackjack')
                    
                elif initial_hand > 21:
                    print(initial_hand, 'Bust')
    elif 'A' not in hand:
        
        if int(initial_hand) < 17:
            print(initial_hand, 'Hit')
            
        elif 21 > initial_hand >= 17:
            print(initial_hand, 'Stay')

        elif initial_hand == 21:
            print(initial_hand, 'Blackjack')
            
        elif initial_hand > 21:
            print(initial_hand, 'Bust')


if __name__ == "__main__":
    # blackjack()
    blackjack_aces()