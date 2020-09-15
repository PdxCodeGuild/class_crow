
# data_list = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5]
# data_list = []

# data_str = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'

def credit_card_validation():
    data_list = []
    data_str = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'
    # 1234567891234567
    # data_str = input('What is your credit card number? ')
    data_str = data_str.replace(' ', '')
    print('data string', data_str)
    for char in data_str:
        data_list.append(int(char))
    print ('data list', data_list)
    check_digit = data_list.pop(-1)
    print('check digit', check_digit)

    data_list.reverse()
    print('reversed list', data_list)
    
    doubled_list = []
    # enumerate(): allows us to loop over something and have an automatic counter
    # https://book.pythontips.com/en/latest/enumerate.html

    for counter, value in enumerate(data_list):
        if counter % 2 == 0:
            value = value * 2
            doubled_list.append(value)
        elif counter % 2 != 0:
            doubled_list.append(value)
    print('doubled data list', doubled_list)

    subtract_nine = []
    for value in doubled_list:
        if value > 9:
            value = value - 9
            subtract_nine.append(value)
        else:
            subtract_nine.append(value)
    print('subtracted 9 from values over 9', subtract_nine)

    counter = 0
    for value in subtract_nine:
        counter += value
    print('sum of all values is', counter)
    

    second_digit = str(counter)[1]
    print('The second digit of the sum is', second_digit)

    if int(second_digit) == int(check_digit):
        print('Valid')
    return int(second_digit) == check_digit
    
        


    

if __name__ == "__main__":
    credit_card_validation()
    print(credit_card_validation())