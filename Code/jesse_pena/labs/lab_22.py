import math

def automated_readability_index():

    ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

    book = open('/home/jpchato/class_crow/Code/jesse_pena/labs/lab_21.txt', 'r')
    contents = book.read()
    contents = contents.lower()

    

    word_list = []
    sentence_list = []
    word_string = ''

    for word in contents.replace('?', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('-', '').replace(',', '').replace('/', '').replace('\\', '').replace(':', '').replace('$', '').replace('%', '').replace('*', '').replace('"', '').replace('_', '').split():
        word_list.append(word)
        word_string += word
    
    for char in contents:
        if char == '.' or char == '!' or char == '?':
            sentence_list.append(char)


    characters = len(word_string)
    words = len(word_list)
    sentences = len(sentence_list)

    ari = math.ceil((4.71*(characters/words)) + (0.5*(words/sentences)) - 21.43)
    if ari > 14:
        ari = 14
    
    if ari < 1:
        ari = 1

    # print(ari)

    if ari in ari_scale:
        reader_age = ari_scale[ari]['ages']
        reader_grade_level = ari_scale[ari]['grade_level']

    print (f'The ARI for the text is {ari}')
    print(f'This corresponds to a {reader_grade_level} grade level of difficulty')
    print(f'That is suitable for an average person {reader_age} years old')
    

    
    
    


if __name__ == "__main__":
    automated_readability_index()