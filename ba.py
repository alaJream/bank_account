class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.account = account_number
        self.balance = balance

    def deposit(self):
        # add parameter to take amount and add to balance
        print("Amount Deposited: $X.XX new balance: $Y.YY")

    def withdraw(self):
        # add parameter to subtract from balance
        print("Amount withdrawn: $X.XX new balance: $Y.YY")
        # if user withdraw account greater than balance account 
        print("Insufficient funds.")

    def get_balance(self):
        print(f"Welcome to Gonzales Banking, here is your current balance: {self.balance}.")

    def add_interest(self):
        # adds interest to the users balance, annual interest rate is 1%, 0.083%/month
        # interest = balance * 0.00083
        print("Interest rate")

    def print_statement(self):
        print(self.name)
        print(self.account)
        print(self.balance)