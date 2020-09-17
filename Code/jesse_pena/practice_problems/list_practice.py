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



if __name__ == "__main__":
    # print(random_list_item())
    # number_list()
    # print(even_even([1,2,3,4,5,6]))
    # print(even_even([1,2,3,4]))
    # print_every_other()
    reverse_list()