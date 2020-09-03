import random

def main():

    #creating lists of different emoji features
    eyes = [':',';','X','8']
    noses = ['*','-','>','o','']
    mouths = ['D','P',')','(','/','[']

    print('Here are 5 emojis:\n')

    #creating REPL for 5 emoji outputs
    counter = 1
    while counter < 6:
        randoEyes = random.choice(eyes)
        randoNose = random.choice(noses)
        randoMouth = random.choice(mouths)

        print(randoEyes + randoNose + randoMouth + '\n')
        counter += 1

main()