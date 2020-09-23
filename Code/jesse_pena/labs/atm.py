class ATM:
    def __init__(self, name = '', balance = 0, transaction_list = []):
        self.name = name 
        self.balance = balance
        self.transaction_list = []
        
    def check_balance(self, name):
        return self.balance

    def deposit(self, balance, deposit_amount):
        self.balance += deposit_amount
        self.transaction_list.append(f'You have deposited ${deposit_amount}')
        return self.balance

    def check_withdrawal(self, balance, withdrawal_amount):
        new_balance = self.balance-withdrawal_amount
        if new_balance > 0:
            return True
        else:
            return False

    def withdrawal(self, balance, withdrawal_amount):
        self.balance -= withdrawal_amount
        self.transaction_list.append(f'You have withdrawn ${withdrawal_amount}')
        return self.balance

    def calc_interest(self, balance, interest_rate = 0.1):
        self.interest_rate = interest_rate
        account_interest = self.balance*self.interest_rate
        return account_interest

    def print_transactions(self):
        # counter = 1
        # for transaction in self.transaction_list:
        #     print (f'{transaction}')
        print(self.transaction_list)
        return self.transaction_list

def interact():
    start_name = input('What is the name of the account? ')
    start_amount = int(input('What is the starting amount of the account? '))
    user_account = ATM(start_name, start_amount)

    while True:
        user_input = input('what would you like to do (deposit, withdraw, check balance, history, done)? ')
        

        if user_input == 'deposit':
            deposit_amount = int(input('How much are you depositing? '))
            user_account.deposit(user_account.balance, deposit_amount)
            # user_account.print_transactions()
            
        if user_input == 'withdraw':
            withdrawal_amount = int(input('How much are you withdrawing? '))
            user_account.withdrawal(user_account.balance, withdrawal_amount)
            # user_account.print_transactions()

        if user_input == 'check balance':
            print('balance', user_account.balance)

        if user_input == 'history':
            user_account.print_transactions()

        if user_input == 'done':
            return False

if __name__ == "__main__":
    interact()


# jesse_account = ATM('jesse', 100)
# print('balance', jesse_account.balance)
# print('account name', jesse_account.name)
# print('deposit ', jesse_account.deposit(jesse_account.balance, 100))
# print('withdrawal ', jesse_account.withdrawal(jesse_account.balance, 20))
# print('Am I safe to withdraw? ', jesse_account.check_withdrawal(jesse_account.balance, 20))
# print('Amount of interest calculated on account ', jesse_account.calc_interest(jesse_account.balance))
# print(jesse_account.print_transactions())