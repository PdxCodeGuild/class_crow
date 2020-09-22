import random

def random_list_item():
    fruits = ['apples', 'bananas', 'pears']
    return random.choice(fruits)

def number_list():
    user_input = ''
    num_list = []
    while user_input != 'done':
        user_input = input('Enter a number (or \'done\'): ')
        
        if user_input != 'done':
            num_list.append(user_input)
    
    print (num_list)

def even_even(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
    print(even_numbers)
    if len(even_numbers) % 2 == 0:
        return True
    else:
        return False

def print_every_other():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    counter = 0
    while counter < len(nums):
        for i in range(len(nums)):
            counter += 1
            if i % 2 == 0:
                print('while loop', nums[i])
    
    
    for i in range(len(nums)):
            if i % 2 == 0:
                print('for loop', nums[i])

def reverse_list():
    nums = [1, 2, 3, 4, 1, 2, 6] 
    print('original list', nums)
    nums.reverse()
    print('reversed list', nums)

def extract_less_than_ten(nums):
    '''
    Write a function to move all the elements of a list with value less than 10 to a new list and return it.
    '''
    # nums = [1, 2, 3, 10, 20, 30]
    new_list = []
    for num in nums:
        if num < 10:
            new_list.append(num)
    print(new_list)
    return new_list 

def common_elements():
    '''
    Write a function to find all common elements between two lists.
    '''
    nums_1 = [1, 2, 3, 10, 20, 30]
    nums_2 = [1, 2, 3, 4, 1, 2, 6] 
    shared_list = []

    for i in range(len(nums_1)):
        # if nums_1[i] in nums_2:
        #     shared_list.append(nums_1[i])
        for j in range(len(nums_2)):
            if nums_1[i] == nums_2[j]:
                shared_list.append(nums_1[i])
    print(shared_list)
    return(shared_list)

def combine(list_1, list_2):
    '''
    Write a function to combine two lists of equal length into one, alternating elements.
    '''
    # list_1 = ['a', 'b', 'c']
    # list_2 = [1, 2, 3]
    zipped_list = []

    if len(list_1) == len(list_2):
        for i in range(len(list_1)):
            list_1[i]
            list_2[i]
            zipped_list.append(list_1[i])
            zipped_list.append(list_2[i])
    else:
        print('lists are not of equal length')

    print(zipped_list)

def find_pairs():
    '''
    Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
    '''
    nums = [5, 6, 2, 3]
    target = 7
    pair = []
    for i in range(len(nums)):
        for num in nums:
            if nums[i] + num == target:
                print(f'{nums[i]} + {num} = {target}')
                pair.append(nums[i])
                pair.append(num)
    print(pair)
                
def merge():
    '''
    Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.
    '''
    list_1 = [5, 2, 1]
    list_2 = [6, 8, 2]

    new_list = []

    for i in range(len(list_1)):
        pair_list =[]
        pair_list.append(list_1[i])
        pair_list.append(list_2[i])
        if pair_list not in new_list:
            new_list.append(pair_list)
    print(new_list)

def combine_all():
    '''
    Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.
    '''
    nums = [[5,2,3],[4,5,1],[7,6,3]]

    combined_list = []

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            combined_list.append(nums[i][j])
    print(combined_list)

def fibonacci():
    n = 8
    
    fibonacci_number = 1
    fibonacci_list = []
    for i in range( n):
        fibonacci_list.append(fibonacci_number)
        fibonacci_number = fibonacci_list[i] + fibonacci_list[i-1]
    print(fibonacci_list)

def minimum():
    nums = [1,2,3,4,5,6]
    nums.sort()
    print(nums[0])

def maximum():
    nums = [1,2,3,4,5,6]
    nums.sort()
    print(nums[-1])

def mean():
    nums = [1,2,3,4,5,6]
    tally = 0
    for num in nums:
        tally += num
    # print(tally)
    nums_mean = tally/len(nums)
    print(nums_mean)






if __name__ == "__main__":
    # print(random_list_item())
    # number_list()
    # print(even_even([1,2,3,4,5,6]))
    # print(even_even([1,2,3,4]))
    # print_every_other()
    # reverse_list()
    # extract_less_than_ten([1, 2, 3, 10, 20, 30])
    # common_elements()
    # combine(['a', 'b', 'c'],[1, 2, 3])
    # find_pairs()
    # merge()
    # combine_all()
    # fibonacci()
    minimum()
    maximum()
    mean()
