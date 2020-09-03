def main():

    #getting user input
    userinput = int(input('Enter your score for conversion: '))

    #comparing user input to letter grades and checking for '+'/'-'
    if userinput >= 90 and userinput <= 100:
        grade = 'A'
        if (100 - userinput) <= 3: 
            sym = '+'
        elif (100 - userinput) >= 7: 
            sym = '-'
        else:
            sym = ''
    if userinput >= 80 and userinput < 90:
        grade = 'B'
        if (90 - userinput) <= 3: 
            sym = '+'
        elif (90 - userinput) >= 7: 
            sym = '-'
        else:
            sym = ''
    if userinput >= 70 and userinput < 80:
        grade = 'C'
        if (80 - userinput) <= 3: 
            sym = '+'
        elif (80 - userinput) >= 7: 
            sym = '-'
        else:
            sym = ''
    if userinput >= 60 and userinput < 70:
        grade = 'D'
        if (70 - userinput) <= 3: 
            sym = '+'
        elif (70 - userinput) >= 7: 
            sym = '-'
        else:
            sym = ''
    if userinput < 60:
        grade = 'F'
        sym = ''

    #creating output
    if sym != '':
        print(f'Your letter grade is {grade}{sym}!')
    else:
        print(f'Your letter grade is {grade}!')

main()