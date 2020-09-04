# reference https://stackoverflow.com/q/38663417
# The index() method returns the position at the first occurrence of the specified value.

def rot_cipher():
    user_string = (input('Type a word: ')).lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    encryption = ''
    shift = 13

    for char in user_string:
        if char in letters:
            rot_index = letters.index(char) + shift
            # print(letters.index(char))
            if rot_index < 26:
                encryption = encryption + letters[rot_index]
            else:
                encryption = encryption + letters[rot_index % 26]
    print(encryption)

def rot_cipher_decrypt():
    user_string = (input('Type a word to decrypt: ')).lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    encryption = ''
    shift = -13

    for char in user_string:
        if char in letters:
            rot_index = letters.index(char) + shift
            # print(letters.index(char))
            if rot_index < 26:
                encryption = encryption + letters[rot_index]
            else:
                encryption = encryption + letters[rot_index % 26]
    print(encryption)

def rot_cipher_choice():
    user_string = (input('Type a word: ')).lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    encryption = ''
    shift = int(input('Enter the number of times you want to rotate the cipher as a number: '))

    for char in user_string:
        if char in letters:
            rot_index = letters.index(char) + shift
            # print(letters.index(char))
            if rot_index < 26:
                encryption = encryption + letters[rot_index]
            else:
                encryption = encryption + letters[rot_index % 26]
    print(encryption)


if __name__ == "__main__":
    # rot_cipher()
    # rot_cipher_choice()
    rot_cipher_decrypt()