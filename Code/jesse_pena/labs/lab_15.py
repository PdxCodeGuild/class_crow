numbers_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
tens_dict = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
twenty_plus_dict = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
hundred_plus_dict = {1: 'One Hundred', 2: 'Two Hundred', 3: 'Three Hundred', 4: 'Four Hundred', 5: 'Five Hundred', 6: 'Six Hundred', 7: 'Seven Hundred', 8: 'Eight Hundred', 9: 'Nine Hundred'}

def hundreds_to_phrase():
    # number = 520
    number =int(input('Enter a number between 1 - 999: '))
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

def clock_to_phrase():

    time_hours_dict = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve'}

    time_minutes_dict = {'01': 'one', '02': 'two', '03': 'three', '04': 'four', '05': 'five', '06': 'six', '07': 'seven', '08': 'eight', '09': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15':'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '21': 'twenty - one', '22': 'twenty-two', '23': 'twentry-three', '24': 'twenty-four', '25': 'twenty-five', '26': 'twenty-six', '27': 'twenty-seven', '28': 'twenty-eight', '29': 'twenty-nine', '30': 'thirty', '31': 'thirty-one', '32': 'thirty-two', '33': 'thirty-three', '34': 'thirty-four', '35': 'thirty-five', '36': 'thirty-six', '37': 'thirty-seven', '38': 'thirty-eight', '39': 'thirty-nine', '40': 'forty', '41': 'forty-one', '42': 'forty-two', '43': 'forty-three', '44': 'forty-four', '45': 'forty-five', '46': 'forty-six', '47': 'forty-seven', '48': 'forty-eight', '49': 'forty-nine', '50': 'fifty', '51': 'fifty-one', '52': 'fifty-two', '53': 'fifty-three', '54': 'fifty-four', '55': 'fifty-five', '56': 'fifty-six', '57': 'fifty-seven', '58': 'fifty-eight', '59': 'fifty-nine'}
    
    user_time_hours = input('What are the hours you need to convert? No leading zeros i.e. (12, 1, 2, 3) ')
    # user_time_hours = '1'

    user_time_minutes = input('What are the minutes you need to convert? Use leading zeros i.e. (12, 01, 02, 03, 47, 00) ')
    # user_time_minutes = '01'

    if int(user_time_hours) > 12:
        print('Invalid input')
        user_time_hours = input('What are the hours you need to convert? (12, 1, 2, 3) ')

    if int(user_time_minutes) > 59:
        print('Invalid input')
        user_time_minutes = input('What are the minutes you need to convert? (12, 01, 02, 03, 47, 00) ')

    if user_time_hours in time_hours_dict and user_time_minutes == '00':
        conversion = print(time_hours_dict.get(user_time_hours) + ' o\'clock')
        return conversion

    elif user_time_hours in time_hours_dict and int(user_time_minutes) < 10:
        conversion = print(f'{time_hours_dict.get(user_time_hours)} o\'{time_minutes_dict.get(user_time_minutes)}')
        return conversion

    elif user_time_hours in time_hours_dict and user_time_minutes in time_minutes_dict:
        conversion = print(time_hours_dict.get(user_time_hours) + ' ' + time_minutes_dict.get(user_time_minutes))
        return conversion
   
if __name__ == "__main__":
    # numbers_to_phrase()
    # hundreds_to_phrase()
    clock_to_phrase()
