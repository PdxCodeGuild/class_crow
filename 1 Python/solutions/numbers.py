# find tens digit
# find ones digit
# create dictionary of basic number words
# return tens word + ones word (return sixteen; twenty two, fourty seven)
# exceptions: 11-- eleven

# floor division: 124 // 10  = 12
# modulus: 124 % 10 = 4

# use lists
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zeroty', 'onety', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

num = 1111

def get_tens(num):
    # check if num is less than ten-> then return ones
    if num < 10:
        return ones[num]
    # check if num is in the teens-> then return teens
    elif num < 20:
        return teens[num -10]
    # else: separate tens and ones digits and return strings
    elif num < 100:
        tens_digit = num // 10
        ones_digit = num % 10
        if ones_digit == 0:
            return tens[tens_digit]
        else: 
            return tens[tens_digit] + '-' + ones[ones_digit]

def get_hundreds(num):
    # get hundreds digit 
    hundreds_digit = num // 100
    tens_num = num % 100
    hundreds_phrase = ones[hundreds_digit] + ' hundred'
    return hundreds_phrase + " " + get_tens(tens_num)

def get_thousands(num):
    thousands_digit = num // 1000
    thousands_phrase = ones[thousands_digit]+ ' thousand'
    hundreds_num = num % 1000 
    return thousands_phrase + ' ' + get_hundreds(hundreds_num)


num = int(input('Whats the number????'))

if num < 100:
    print(get_tens(num))
elif num < 1000:
    print(get_hundreds(num))
else:
    print(get_thousands(num))