
# start with a blank output string
# loop through every character of the string that the user entered
# find the index of that character in the alphabet
# using that index, find the character in the rotated alphabet
# append that character to the output string


def rot13(text):
    alphabet         = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotated = 'nopqrstuvwxyzabcdefghijklm'

    translation = ''
    for character in text:
        index = alphabet.find(character)
        translation += alphabet_rotated[index]
    print(translation)

# rot13('uryyb')

def rot13v2(text, num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    translation = ''
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            translation += char
        else:
            index += num
            index %= len(alphabet)
            translation += alphabet[index]
    print(translation)

# rot13v2('hello', 15)

def main():
    text = input('what do you want to translate?')
    rotations = int(input('how many rotations?'))
    # print(rotations)
    rot13v2(text, rotations)

main()

