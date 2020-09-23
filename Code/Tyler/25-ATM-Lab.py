import time


class ATM:
    def __init__(self,balance=0.00,interest_rate=.1):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        print('$'+str(self.balance))

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append('DEPOSIT - $'+str(amount))
        print('$'+str(self.balance))

    def check_withdrawl(self, amount):
        self.transactions.append('WITHDRAWL CHECK')
        if self.balance >= amount:
            print('You will have $'+str(self.balance)+'remaining.\n')
            print('You\'re good to withdraw!')
        else:
            print('You will have $'+str(self.balance)+'remaining.\n')
            print('You do not have enough money :(')

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append('WITHDRAW - $'+str(amount))
        print('Withdrawing money...')
        time.sleep(3)
        print('You have $'+str(self.balance)+' remaining.\n')
        print('Dont forget your card.')

    def calc_interest(self):
        total_interest = self.balance * self.interest_rate
        self.transactions.append('INTEREST CALC')
        print('Your total interest is $'+str(total_interest))

    def print_transactions(self):
        print('Transaction History:\n')
        for item in self.transactions:
            print(item)

def main():
    my_account = ATM()

    while True:

        userinput = input('Select an option:\n1) Check Balance\n2) Make a Deposit\n3) Check Withdrawl\n4) Withdraw\n5) Calculate Interest\n6) Show Transaction History\n: ')
        if userinput == '2' or userinput == '3' or userinput == '4':
            useramt = float(input('Enter an amount: '))
        if userinput == '1':
            my_account.check_balance()
        elif userinput == '2':
            my_account.deposit(useramt)
        elif userinput == '3':
            my_account.check_withdrawl(useramt)
        elif userinput == '4':
            my_account.withdraw(useramt)
        elif userinput == '5':
            my_account.calc_interest()
        elif userinput == '6':
            my_account.print_transactions()

        userans = input('Would you like to start another transaction? (Y/N): ').lower()
        if userans == 'y':
            continue
        else:
            break 




    

main()