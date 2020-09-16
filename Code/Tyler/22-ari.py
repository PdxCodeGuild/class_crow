

import string
import math



def charactersNum(file):
    with open(file, 'r') as f:
        f = f.read()

    count = 0
    for char in f:
        if char != ' ':
            count += 1

    return count

def sentencesNum(file):
    with open(file, 'r') as f:
        f = f.read()

    count = 0
    for item in f.split('. '):
        count += 1
    
    for punc in string.punctuation:
        count = count + len(f.split(punc+' ')) - 1


    return count

def wordsNum(file):
    with open(file, 'r') as f:
        f = f.read()

    f = f.split(' ')
    # print(f)

    count = 0
    for item in f:
        count += 1

    return count

def main():
    input('Enter file for evalutation: #(notional block of code)')

    file = 'C:\\Users\\tyler\Desktop\\PDX-Code\\class_crow\\Code\\Tyler\\22-paragraph-for-program'

    characters = float(charactersNum(file))

    sentences = float(sentencesNum(file))

    words = wordsNum(file)

    result = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43

    result = math.ceil(result)

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


    agelevel = ari_scale[result]['ages']

    gradelevel = ari_scale[result]['grade_level']

    print(f'''   The ARI for {file} is {result}
    This corresponds to a {gradelevel} level of difficulty
    that is suitable for an average person {agelevel} years old.
''')

main()