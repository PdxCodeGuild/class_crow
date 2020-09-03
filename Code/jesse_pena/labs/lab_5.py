import random

eyes = ['B', ':', ';', 'X']
noses = ['^', '-', '3', '']
mouths = [')', '(', 'X', '|', 'P']

def face_maker():
    counter = 0
    while counter < 5:
        counter += 1

        random_eyes = random.choice(eyes)

        random_noses = random.choice(noses)

        random_mouths = random.choice(mouths)

        face = random_eyes + random_noses + random_mouths

        print(face)

if __name__ == "__main__":
    face_maker()