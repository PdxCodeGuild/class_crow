def Encrypt():
    #get user input
    string = input('Enter a string to encrypt: ').lower()
    ciphernum = int(input('Enter Cipher number: '))

    #create alphbet list
    alpha = []
    alphaAdjusted = []
    for char in 'abcdefghijklmnopqrstuvwxyz':
        alpha.append(char)
        alphaAdjusted.append(char)
    #adjust alphabet list to cipher order
    count = 0
    while count < ciphernum:
        alphaAdjusted.append(alphaAdjusted.pop(0))
        count += 1

    #create list from user string
    spacecount = 0
    spacepositions = []
    userslist = []
    for char in string:
        userslist.append(char)
        #some code to get positions of spaces for reentering on decryption
        spacecount += 1
        if char == ' ':
            spacepositions.append(spacecount)


    #combine lists into dictionary for reference
    combined_dict = dict(zip(alphaAdjusted, alpha))
    print(combined_dict)
    #get keys of each letter in users string
    encryptedlist = []
    for letter in userslist:
        encryptedlist.append(combined_dict[letter])

    encryptedstring = ''.join(encryptedlist)

    print('Encrypted message: ' + encryptedstring + '\n')

def Decrypt():
    #get user input
    string = input('Enter a string to decrypt: ').lower()
    ciphernum = int(input('Enter Cipher number: '))

    #create alphbet list
    alpha = []
    alphaAdjusted = []
    for char in 'abcdefghijklmnopqrstuvwxyz':
        alpha.append(char)
        alphaAdjusted.append(char)

    #adjust alphabet list to cipher order
    count = 0
    while count < ciphernum:
        alphaAdjusted.append(alphaAdjusted.pop(0))
        count += 1

    #create list from user string
    count = 0
    spacepositions = []
    userslist = []
    for char in string:
        userslist.append(char)
        #some code to get positions of spaces for reentering on decryption
        count += 1
        if char == ' ':
            spacepositions.append(count)

    #combine lists into dictionary for reference (flipped for decryption)
    combined_dict = dict(zip(alpha, alphaAdjusted))

    #get keys of each letter in users string
    encryptedlist = []
    for letter in userslist:
        encryptedlist.append(combined_dict[letter])

    encryptedstring = ''.join(encryptedlist)

    print('Decrypted message: ' + encryptedstring + '\n')



def main():
    while True:

        answer = input('Would you like to encrypt or decrypt a message? (1/2)\n1)Encrypt\n2)Decrypt\n')
        if answer == '1':
            Encrypt()
        elif answer == '2':
            Decrypt()
        else:
            print('Invalid response. Please try again. \n')
            
        againanswer = input('Would you like to restart? (y/n): ')
        if againanswer == 'y':
            continue
        elif againanswer == 'n':
            print('Exiting.... \n')
            break
        else:
            print('Invalid response. Exiting.... \n')




main()