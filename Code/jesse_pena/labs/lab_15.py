numbers_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
tens_dict = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
twenty_plus_dict = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
hundred_plus_dict = {1: 'One Hundred', 2: 'Two Hundred', 3: 'Three Hundred', 4: 'Four Hundred', 5: 'Five Hundred', 6: 'Six Hundred', 7: 'Seven Hundred', 8: 'Eight Hundred', 9: 'Nine Hundred'}

def hundreds_to_phrase():
    number = 520
    ones_digit = number % 10
    tens_digit = number // 10
    tens_digit_for_hundreds = (number // 10) % 10
    modulus_hundred = number % 100
    hundreds_digit = number // 100
    # print(f'ones digit {ones_digit}')
    # print(f'tens digit {tens_digit}')
    # print(f'tens digit for hundreds {tens_digit_for_hundreds}')
    # print(f'hundreds digit {hundreds_digit}')
    # print(f'modulus hundred {modulus_hundred}')

    if number < 10:
        print(numbers_dict.get(number))
    if 10 <= number <= 19:
        print(tens_dict.get(number))

    if tens_digit in twenty_plus_dict:
        if ones_digit == 0:
            print(twenty_plus_dict.get(tens_digit))
        elif tens_digit != 1:
            print(twenty_plus_dict.get(tens_digit) + '-' + numbers_dict.get(ones_digit))
    
    if number >= 100:
        if 0 < modulus_hundred < 10:
            print(f'{hundred_plus_dict.get(hundreds_digit)} - {numbers_dict.get(ones_digit)}')
        elif 10 <= modulus_hundred < 20:
            print(f'{hundred_plus_dict.get(hundreds_digit)} - {tens_dict.get(modulus_hundred)}')
        elif  modulus_hundred == 0:
            print(f'{hundred_plus_dict.get(hundreds_digit)}')
        elif ones_digit == 0:
            print(f'{hundred_plus_dict.get(hundreds_digit)} - {twenty_plus_dict.get(tens_digit_for_hundreds)}')
        elif ones_digit != 0 and tens_digit_for_hundreds != 0:
            print(f'{hundred_plus_dict.get(hundreds_digit)} - {twenty_plus_dict.get(tens_digit_for_hundreds)} - {numbers_dict.get(ones_digit)}')


def numbers_to_phrase():
    number = 99
    tens_digit = number // 10
    ones_digit = number % 10
    # print(f'tens digit {tens_digit}')
    # print(f'ones digit {ones_digit}')
    if number <= 10:
        print(numbers_dict.get(number))
    if 10 < number <= 19:
        print(tens_dict.get(number))

    if tens_digit in twenty_plus_dict:
        if ones_digit == 0:
            print(twenty_plus_dict.get(tens_digit))
        else:
            print(twenty_plus_dict.get(tens_digit) + '-' + numbers_dict.get(ones_digit))


    

if __name__ == "__main__":
    # numbers_to_phrase()
    hundreds_to_phrase()
