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

def cat_dog(string):
    cat_list = []
    dog_list= []
    for i in range(len(string)):
    # for char in string:
        if string[i] == 'c' and string[i+1] =='a' and string[i+2]=='t':
            cat_list.append(1)
        if string[i] == 'd' and string[i+1] =='o' and string[i+2]=='g':
            dog_list.append(1)
    return len(dog_list) == len(cat_list)

def count_letter(letter, word):
    counter = ''

    for char in word:
        if char == letter:
            counter += letter

    print(len(counter))

def lower_case(string):
    string = string.replace(' ', '').lower()
    print(string)






if __name__ == "__main__":
    # double_every_other_letter('hello')
    # string_changer('kitten')
    # string_changer_loops('kitten')
    # latest_letter('string')
    # hi_counter('hihi')
    # print(cat_dog('catcat'))
    # print(cat_dog('catdog'))
    # print(cat_dog('catdogcatdog'))
    # count_letter('i', 'antidisestablishmentterianism')
    # count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')
    # lower_case("SUPER!")
    # lower_case("        NANNANANANA BATMAN        ")

