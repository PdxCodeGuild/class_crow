import string
import random 

# print(string.digits)
# print(string.punctuation)
# print(string.ascii_letters)

def password_generator(n):
    char = string.ascii_letters + string.digits + string.punctuation
    # print (random.choice(char))
    password = ''
    while len(password) < n:
        password = password + random.choice(char)
    print(password)

def password_generator_2():
    password_length = input('How long do you want your password to be? Use integers: ')
    char = string.ascii_letters + string.digits + string.punctuation
    # print (random.choice(char))
    password = ''
    while len(password) < int(password_length):
        password = password + random.choice(char)
    print(password)



if __name__ == "__main__":
    password_generator(5)
    password_generator_2()