def list_addition():
    list_1 = [2,3,4,2,2,3,4,0,9,2,3,4,1,0,3,4,0,2,3,9,4,8,2,3,0,4]
    list_2 =           [3,0,3,0,0,3,0,2,5,0,5,0,0,2,0,2,0,3,4,9,2]
    big_num = []
    

    while len(list_1) and len(list_2) != 0:

        if len(list_1) > 0:

            x = list_1.pop()
            print('len list1',len(list_1))
            # print('x', x)
        
        if len(list_2) > 0:
            y = list_2.pop()
            print('len list2', len(list_2))
            # print('y', y)
        sum = x + y
        big_num.append(sum)
        print('sum', sum)
        
        # print('length of list one', len(list_1))
        # print('length of list two', len(list_2))
    print (big_num)

    # for num in list_1:
    #     while len(list_1) > 0: 
    #         x = list_1.pop(-1)
    #     while len(list_2) > 0:
    #         y = list_2.pop(-1)
    #     sum = x+y
    #     # print(sum)
    #     tally += sum
    #     # print(tally)

    #     print(x)
    #     print(y)
    #     print(tally)

if __name__ == "__main__":
    list_addition()