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

    print(userinputlist)

    #doing math and appending to list
    count = 1
    for item in userinputlist:
        if count % 2 != 0:
            item = item * 2
            del userinputlist[count - 1]
            userinputlist.insert(count - 1, item)
        count += 1
    count = 1
    for item in userinputlist:
        if item > 9:
            item = item - 9
            del userinputlist[count - 1]
            userinputlist.insert(count - 1, item)
        count += 1

    # count = 1
    # for item in userinputlist:
    #     if count % 2 != 0:
    #         item = item * 2
    #     if item > 9:
    #         item = item - 9
    #         del userinputlist[count - 1]
    #         userinputlist.insert(count - 1, item)
    #     count += 1


    print(userinputlist)

    #getting sum of all digits
    sumVar = 0
    for item in userinputlist:
        sumVar += item

    print(sumVar)

    #getting second digit of sum
    second_digit = str(sumVar)[1]

    print(second_digit)

    if second_digit == lastnum:
        print('Card is valid!')
    else:
        print('Card is invalid :(')

main()