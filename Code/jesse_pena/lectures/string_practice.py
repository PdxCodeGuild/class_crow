def double_every_other_letter(string):
    counter = 0
    double_list = '[]'
    for char in string:
        counter += 1
        if counter % 2 == 0:
            doubles += char * 2
        else:
            doubles += char
        counter += 1 
    print(double_list)

def string_changer(string):

    str_list = [ string[0:x-1] + string[x:len(string)]  for x in range(1, len(string))]

    print(str_list)

def string_changer_loops(string):

    str_list = []

    for i in range(1, len(string)):
        str_list.append(string[0:i-1] + string[i:len(string)])

    print(str_list)

def latest_letter(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    value_initiator = 0

    for i in range(len(string)):
        for char in string:
            # print(alphabet.index(char))
            value_tracker = alphabet.index(char)
            if char in alphabet:
                if value_tracker > value_initiator:
                    value_initiator = value_tracker
    print(alphabet[value_initiator])
    
def hi_counter(string):
    '''
    Write a function that returns the number of occurances of 'hi' in a given string.

    count_hi('hihi') → 2
    '''
    hi_tracker = []

    for i in range(0 , len(string)):
        if string[i] == 'h' and string[i+1] == 'i':
            hi_tracker.append('hi')
    print(len(hi_tracker))

if __name__ == "__main__":
    # double_every_other_letter('hello')
    # string_changer('kitten')
    # string_changer_loops('kitten')
    # latest_letter('string')
    hi_counter('hihi')
