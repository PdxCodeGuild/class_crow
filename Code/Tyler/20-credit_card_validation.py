def main():

    #getting user input
    userinput = input('Enter your credit card number to see if it\'s valid: ')

    #converting userinput to list of ints
    userinputlist = []
    for char in userinput:
        userinputlist.append(int(char))

    #getting last item in list
    lastnum = userinputlist[-1]

    #removing last item in list
    del userinputlist[-1]

    #reversing list
    userinputlist.reverse()


    # doing math and appending to list
    count = 0
    for item in userinputlist:
        if count % 2 == 0:
            item = item * 2
        if item > 9:
            item = item - 9
            userinputlist.insert(count, item)
            del userinputlist[count]
        count += 1



    #getting sum of all digits
    sumVar = 0
    for item in userinputlist:
        sumVar += item


    #getting second digit of sum
    second_digit = str(sumVar)[1]
    second_digit = int(second_digit)

    #final print
    if second_digit == lastnum:
        print('Card is valid!')
    else:
        print('Card is invalid :(')


main()