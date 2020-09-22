class ATM:
    def __init__(self, name = '', balance = 0, transaction_list = []):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        
    def check_balance(self, name):
        return self.balance

    def deposit(self, balance, deposit_amount):
        self.balance += deposit_amount
        self.transaction_list.append(f'You have deposited ${self.balance}')
        return self.balance

    def check_withdrawal(self, balance, withdrawal_amount):
        new_balance = self.balance-withdrawal_amount
        if new_balance > 0:
            return True
        else:
            return False

    def withdrawal(self, balance, withdrawal_amount):
        self.balance -= withdrawal_amount
        self.transaction_list.append(f'You have withdrawn ${self.balance}')
        return self.balance

    def calc_interest(self, balance, interest_rate = 0.1):
        self.interest_rate = interest_rate
        account_interest = self.balance*self.interest_rate
        return account_interest

    def print_transactions(self):
        return self.transaction_list

jesse_account = ATM('jesse', 100)
print('balance', jesse_account.balance)
print('account name', jesse_account.name)
print('deposit ', jesse_account.deposit(jesse_account.balance, 100))
print('withdrawal ', jesse_account.withdrawal(jesse_account.balance, 20))
print('Am I safe to withdraw? ', jesse_account.check_withdrawal(jesse_account.balance, 20))
print('Amount of interest calculated on account ', jesse_account.calc_interest(jesse_account.balance))
print(jesse_account.print_transactions())