class ATM(object):

    def __init__(self):
        self.balance = 0
        self.interest = 0.001
        self.transactions = []
    
    def check_balance(self):
        # returns the account balance
        self.transactions.append(f'User check balance: ${self.balance}')
        return self.balance

    def print_transactions(self):
        # print a list of user transactions
        for line in self.transactions: 
            print(line)
    
    def deposit(self, amount):
        # deposits the given amount into account
        self.transactions.append(f'User deposited: ${amount}')
        self.balance += amount
    
    def check_withdrawal(self, amount):
        # returns true if withdrawn amnt wont put account in negative
        return self.balance > amount

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.transactions.append(f'User withdrew ${amount}')
            self.balance -= amount
            return amount
        else: 
            self.transactions.append(f'User unsuccessfully tried to withdraw ${amount}')
            return amount
    

# my_account.deposit(10000)
# my_account.withdraw(1000000)
# my_account.print_transactions()

def main():
        my_account = ATM()
        valid_inputs = ['deposit', 'd', 'withdraw', 'w', 'check balance', 'b', 'history', 'h', 'exit', 'x']
        while True:
            while True: 
                operation = input("What would you like to do? \n((d)eposit, (w)ithdraw, check (b)alance, check (h)istory, or e(x)it): ").strip().lower()
                if operation in valid_inputs:
                    break
            if operation in ['exit', 'x']:
                print('Goodbye!')
                break
            elif operation in ['deposit', 'd', 'withdraw', 'w']:
                while True:
                    operation = 'deposit' if operation.startswith('d') else 'withdraw'
                    try:
                        amount = int(input(f'How much would you like to {operation}').strip('$'))
                        break
                    except ValueError:
                        print('Invalid input.')
                if operation == 'deposit':
                    my_account.deposit(amount)
                elif operation == 'withdraw':
                    my_account.withdraw(amount)

            elif operation in ['check balance', 'b']:
                print(f'Balance: ${my_account.check_balance()}')
            elif operation in ['check history', 'h']:
                my_account.print_transactions()

            
main()

