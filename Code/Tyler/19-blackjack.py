def main():

    #getting user input
    userinput = list(input('Enter your three cards\n Available options: (A,2,3,4,5,6,7,8,9,10,J,Q,K): ').lower())

    #making dictionary to convert face cards
    convertDict = {'j':11,'q':12,'k':13,'a':1}

    #converting face cards with REPL
    count = 0
    for item in userinput:
        if item == 'j' or item == 'q' or item == 'k' or item == 'a':
            userinput.remove(item)
            userinput.insert(count,convertDict[item])
        
    #getting total of cards
    total = 0
    for item in userinput:
        total += int(item)

    if total < 17:
        print(str(total) + ' Hit')
    elif total >= 17 and total < 21:
        print(str(total) + ' Stay')
    elif total == 21:
        print(str(total) + ' Blackjack!')
    elif total > 21:
        print(str(total) + ' Already Busted :(')

    

main()