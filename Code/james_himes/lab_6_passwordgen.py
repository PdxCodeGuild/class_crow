import random
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
passwords = input('How many passwords would you like to generate?: ')
passwords = int(passwords)
length = input('Password length?')
length =int(length)
for i in range(passwords):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)