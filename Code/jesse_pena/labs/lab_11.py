def simple_calculator():
    
    while True:    
        operand = input('What is the operation you would like to perform? + - * / or type done to terminate the program: ')
        if operand == 'done':
            break
        number_1 = input('What is the first nubmer? ')
        number_2 = input('What is the second number? ')
        if operand == '+':
            answer = sum(number_1, number_2)
            print(f'{number_1} plus {number_2} is equal to {answer}')

        if operand == '-':
            answer = subtract(number_1, number_2)
            print(f'{number_1} minus {number_2} is equal to {answer}')

        if operand == '*':
            answer = multiply(number_1, number_2)
            print(f'{number_1} multiplied by {number_2} is equal to {answer}')

        if operand == '/':
            answer = divide(number_1, number_2)
            print(f'{number_1} divided by {number_2} is equal to {answer}')
        
        simple_calculator()
        

def sum(number_1, number_2):
    return int(number_1) + int(number_2)
    
def subtract(number_1, number_2):
    return int(number_1) - int(number_2)
    
def multiply(number_1, number_2):
    return int(number_1) * int(number_2)

def divide(number_1, number_2):
    return int(number_1) / int(number_2)
    

if __name__ == "__main__":
    simple_calculator()