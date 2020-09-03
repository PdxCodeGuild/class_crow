grade = input('Enter a number between 0-100 that represents a letter grade: ')

def test_grade(grade):
    if (grade >= '98'):
        print('A+')
    elif (grade >= '92'):
        print('A')
    elif (grade >= '90'):
        print('A-')
    elif (grade >= '88'):
        print('B+')
    elif (grade >= '82'):
        print('B')
    elif (grade >= '80'):
        print('B-')
    elif (grade >= '78'):
        print('C+')
    elif (grade>'72'):
        print('C')
    elif (grade >= '70'):
        print('C-')
    elif (grade >= '68'):
        print('D+')
    elif (grade >= '62'):
        print('D')
    elif (grade >= '60'):
        print('D-')
    elif (grade <= '59'):
        print('F')

if __name__ == "__main__":
    test_grade(grade)