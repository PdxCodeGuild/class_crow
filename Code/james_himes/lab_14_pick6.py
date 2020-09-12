import random
balance = 0
num_of_plays = 0

def random_number():
    random_number = random.sample(range(0,99), 6)
    return random_number
def comparison(lista, listb):
    tally = 0
    winnings = 0
    for i in range(6):
        if lista[i] == listb[i]:
            tally += 1        
    if tally == 1:
        winnings += 4
    elif tally == 2:
        winnings += 7
    elif tally == 3:
        winnings += 100
    elif tally == 4:
        winnings += 50000
    elif tally == 5:
        winnings += 1000000
    elif tally == 6:
        winnings += 25000000
    return winnings
while num_of_plays < 100000:
    balance -= 2
    num_of_plays += 1
    winning_ticket = random_number()
    user_ticket = random_number()
    balance += comparison(user_ticket, winning_ticket)
ROI = (balance - 200000) /200000

print(f'Your balance is:{balance}')
print (f'you have spent {num_of_plays * 2}')
print(f'your return on investment is {ROI}')
