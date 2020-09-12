# lab 20: validate a credit card number



def validate_cc(cc_str):
    #put string into list as integers
    cc = []
    for i in range(len(cc_str)):
        cc.append(int(cc_str[i]))
    # 1) Slice off the last digit. That is the check digit.
    check_digit = cc.pop(-1)
    # 2) Reverse the digits.
    cc.reverse()
    # 3) Double every other element in the reversed list.
    for i in range(0, len(cc), 2):
        cc[i] *= 2
    # 4) Subtract nine from numbers over nine.
    counter = 0

    for i in range (len(cc)):
        if cc[i] > 9:
            cc[i] -= 9
    # 5) Sum all values.
        counter += cc[i]
    # 6) Take the second digit of that sum.
    second_digit = str(counter)[1]
    print('second', second_digit)

    # 7) If that matches the check digit, the whole card number is valid.
    return int(second_digit) == check_digit
    # return 7 > 9




print(validate_cc('4556937586899855'))