import random 

# returns list of 6 random numbers
def pick6():
    # create empty list to store numbers in
    ticket = []
    # instantiate counter
    counter = 0
    # add random numbers into list and increment counter
    while counter < 6:
        ticket.append(random.randint(1, 99))
        counter += 1
    return ticket

# takes two lists, counts matches, returns payout
def compare(winning_ticket, user_ticket):
    matches = 0 
    for i in range(6):
        if winning_ticket[i] == user_ticket[i]:
            matches += 1
    payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
    return(payout[matches])

# Return on investment requires:
# how much we spent
# how much we earned
# ROI = balance/expenses

earnings = 0
expenses = 0
counter = 0
while counter < 100000:
    counter += 1
    expenses += 2
    earnings += compare(pick6(), pick6())

balance = earnings - expenses
roi = balance/expenses
print('earnings:', earnings)
print('expenses:', expenses)
print('balance:', balance)
print('roi:', roi)


