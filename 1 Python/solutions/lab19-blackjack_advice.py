def card_value(card):
    # if card == 'A':
    #     return 1
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    return int(card)
def remove_aces(the_list, ace):
   return [value for value in the_list if value != ace]

def ace_check(card_list):
    total = 0
    counter = 0
    if 'A' in card_list:
        card_list = remove_aces(card_list, 'A')
        if len(card_list) == 0:
            total += 13 
        else:
            for item in card_list:
                counter += 1
                total += card_value(item)
            if total < 10 and counter == 2:
                print('your ace should be 11')
                total += 11
            elif total < 10 and counter == 1:
                print('one ace is 11, the other is 1')
                total += 12
            elif total == 10 and counter == 1:
                print('your aces should be 1')
                total += 2
            elif total == 10 and counter == 2:
                print('your ace should be 11')
                total += 11
            elif total > 10 and counter == 2:
                print('your ace should be 1')
                total += 1
            elif total > 10 and counter == 1:
                print('both aces are 1')
                total += 2
            else: 
                print('error: somethings missing')
    else:
        for card in card_list:
            total += card_value(card)
    return total

def main():
    cardList = []
    card1 = input('what is your first card? ')
    card2 = input('what is your second card? ')
    card3 = input('what is your third card? ')
    cardList.append(card1)
    cardList.append(card2)
    cardList.append(card3)
    print(cardList)

    total = ace_check(cardList)
    if total < 17:
        print('total:', total, ': hit!')
    elif total < 21:
        print('total:', total, ': hit!')
    elif total == 21:
        print('total:', total, ':blackjack!')
    else:
        print('total:', total, ': busted!')

main()
