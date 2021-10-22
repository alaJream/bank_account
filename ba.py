class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.account = account_number
        self.balance = balance

    def deposit(self, amount):
        # add parameter to take amount and add to balance
        deposited_total = amount + self.balance
        print(f'Amount Deposited: ${amount} New Balance: ${deposited_total}')

    def withdraw(self, amount):
        # if user withdraw account greater than balance account 
        if amount > self.balance:
            self.balance -= 1
            return ("Insufficient funds.")
        # add parameter to subtract from balance
        total = self.balance - amount
        print(f'Amount withdrawn: ${amount} new balance: ${total}')
        
        

    def get_balance(self):
        print(f"Welcome to Gonzales Banking, here is your current balance: {self.balance}.")

    def add_interest(self, balance):
        # adds interest to the users balance, annual interest rate is 1%, 0.083%/month
        # interest = balance * 0.00083
        interest = balance * 0.00083
        interest_total = interest + balance
        return (interest_total)

    def print_statement(self, name, account, balance):
        return (f'{name} Account Number: {account} Balance: {balance}')


