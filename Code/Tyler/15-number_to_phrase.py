def tens(index):
    if userinput[index + 1] == '1':
        ones = 'one'
    elif userinput[index + 1] == '2':
        ones = 'two'
    elif userinput[index + 1] == '3':
        ones = 'three'
    elif userinput[index + 1] == '4':
        ones = 'four'
    elif userinput[index + 1] == '5':
        ones = 'five'
    elif userinput[index + 1] == '6':
        ones = 'six'
    elif userinput[index + 1] == '7':
        ones = 'seven'
    elif userinput[index + 1] == '8':
        ones = 'eight'
    elif userinput[index + 1] == '9':
        ones = 'nine'

    if userinput[index] == '1' and userinput[1] == '0':
        conversion = 'ten'
    elif userinput[index] == '1' and userinput[1] == '1':
        conversion = 'eleven'
    elif userinput[index] == '1' and userinput[1] == '2':
        conversion = 'twelve'
    elif userinput[index] == '1' and userinput[1] == '3':
        conversion = 'thirteen'
    elif userinput[index] == '1' and userinput[1] == '5':
        conversion = 'fifteen'
    elif userinput[index] == '1':
        conversion = ones + 'teen'
    elif userinput[index] == '2' and userinput[1] == 0:
        conversion = 'twenty'
    elif userinput[index] == '2':
        conversion = 'twenty' + ones
    elif userinput[index] == '3' and userinput[1] == '0':
        conversion = 'thirty'
    elif userinput[index] == '3':
        conversion = 'thirty'+ ones
    elif userinput[index] == '4' and userinput[1] == '0':
        conversion = 'forty'
    elif userinput[index] == '4':
        conversion = 'forty'+ ones
    elif userinput[index] == '5' and userinput[1] == '0':
        conversion = 'fifty'
    elif userinput[index] == '5':
        conversion = 'fifty'+ ones
    elif userinput[index] == '6' and userinput[1] == '0':
        conversion = 'sixty'
    elif userinput[index] == '6':
        conversion = 'sixty'+ ones
    elif userinput[index] == '7' and userinput[1] == '0':
        conversion = 'seventy'
    elif userinput[index] == '7':
        conversion = 'seventy' + ones
    elif userinput[index] == '8' and userinput[1] == '0':
        conversion = 'eighty'
    elif userinput[index] == '8':
        conversion = 'eighty'+ ones
    elif userinput[index] == '9' and userinput[1] == '0':
        conversion = 'ninety'
    elif userinput[index] == '9':
        conversion = 'ninety'+ ones

    return conversion

def hundreds(index):
    if userinput[index] == '1':
        convert = 'one-hundred and '
    if userinput[index] == '2':
        convert = 'two-hundred and '
    if userinput[index] == '3':
        convert = 'three-hundred and '
    if userinput[index] == '4':
        convert = 'four-hundred and '
    if userinput[index] == '5':
        convert = 'five-hundred and '
    if userinput[index] == '6':
        convert = 'six-hundred and '
    if userinput[index] == '7':
        convert = 'seven-hundred and '
    if userinput[index] == '8':
        convert = 'eight-hundred and '
    if userinput[index] == '9':
        convert = 'nine-hundred and '

    return convert

def main():
    #get user input
    global userinput
    userinput = input('Enter a number you want to convert: ')

    #create dictionary for reference
    global dictionary
    dictionary = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',\
        '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

    #get length of userinput to determine how to convert numbers
    length = len(userinput)

    #managing hundreds
    if length > 2:
        tens_number = tens(1)
        hundreds_number = hundreds(0)
        print('conversion: ' + hundreds_number + tens_number)

    #managing tens numbers
    elif length > 1:
        tens_number = tens(0)
        print('conversion: ' + tens_number)

    #managing single numbers
    else:
        conversion = dictionary[userinput]

        print('conversion: ' + conversion)

main()

