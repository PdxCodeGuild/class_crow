import random

# def manual_pick_6():
#     winning_list = winning_numbers()
    
#     balance = 0
#     match_tracker = []
#     loop = 0
#     while loop < 100000:
#         loop += 1
#         number_list = generate_list()
#         if winning_list[0] == number_list[0]:
#             match_tracker.append(1)
#         if winning_list[1] == number_list[1]:
#             match_tracker.append(1)
#         if winning_list[2] == number_list[2]:
#             match_tracker.append(1)
#         if winning_list[3] == number_list[3]:
#             match_tracker.append(1)
#         if winning_list[4] == number_list[4]:
#             match_tracker.append(1)
#         if winning_list[5] == number_list[5]:
#             match_tracker.append(1)
#         if len(match_tracker) == 6:
#             balance += 25000000
#         elif len(match_tracker) == 5:
#             balance += 1000000
#         elif len(match_tracker) == 4:
#             balance += 50000
#         elif len(match_tracker) == 3:
#             balance += 100
#         elif len(match_tracker) == 2:
#             balance += 7
#         elif len(match_tracker) == 1:
#             balance += 4

    
#     print(f'Your balance is {balance}')
#     roi = (balance - 200000)/200000
#     print(f'Your roi is {roi}')
#     # print(match_tracker)
    
def pick_6():
    winning_list = winning_numbers()
    # print(winning_list)
    balance = 0
    match_tracker = []
    loop = 0
    while loop < 100000:
        loop += 1
        number_list = generate_list()
        # print(number_list)
        for i in range(len(winning_list)):
            # print(winning_list[i])
            if winning_list[i] == number_list[i]:
                match_tracker.append(1)
        if len(match_tracker) == 6:
            balance += 25000000
        elif len(match_tracker) == 5:
            balance += 1000000
        elif len(match_tracker) == 4:
            balance += 50000
        elif len(match_tracker) == 3:
            balance += 100
        elif len(match_tracker) == 2:
            balance += 7
        elif len(match_tracker) == 1:
            balance += 4
    print(f'Your balance is {balance}')
    roi = (balance - 200000)/200000
    print(f'Your roi is {roi}')
    # print(match_tracker)



def generate_list():
    number_list = []
    
    while len(number_list) < 6:
        number_list.append(random.randint(1,99))
    # print(number_list)
    return number_list

def winning_numbers():
    winning_list = []
    
    while len(winning_list) < 6:
        winning_list.append(random.randint(1,99))
    # print(winning_list)
    return winning_list

if __name__ == "__main__":
    # manual_pick_6()
    pick_6()
    generate_list()
    winning_numbers()