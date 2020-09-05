import random

def main():

    balance = 0

    balancecounter = 0
    while balancecounter <= 100000:
        #generate winning numbers
        winners = []
        count = 1
        while count <= 3:
            winners.append(random.randint(1,99))
            count += 1

        # print(winners)

        #making users ticket
        ticket = []
        count = 1
        while count <= 3:
            ticket.append(random.randint(1,99))
            count += 1

        # print(ticket)

        balance = balance + -2

        #checking matches in lists
        count = 0
        wins = 0
        for num in ticket:
            if num == winners[count]:
                wins += 1
            count += 1

        # print(wins)

        if wins == 1:
            balance = balance + 4
        elif wins == 2:
            balance = balance + 7
        elif wins == 3:
            balance = balance + 100
        elif wins == 4:
            balance = balance + 50000
        elif wins == 5:
            balance = balance + 1000000
        elif wins == 6:
            balance = balance + 25000000

        print(f'Balance: ${balance}')

        balancecounter += 1


main()