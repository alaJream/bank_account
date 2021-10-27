# import randomint to randomize numbers for account number
from random import randint

class BankAccount:
    def __init__(self, full_name, account_number, account_type, balance):
        self.name = full_name
        self.account = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        # add parameter to take amount and add to balance
        self.balance += amount
        print(f'\n\nAmount Deposited: ${amount}\nNew account Balance: ${self.balance}\n\n')
        return self.balance

    def withdraw(self, amount):
        # if user withdraw account greater than balance account 
        if (amount > self.balance):
            self.balance -= 10
            print(f"\n\nInsufficient funds. You have been charged $10 overdraft fee. New balance: ${self.balance}\n\n")
        # add parameter to subtract from balance
        else:
            self.balance -= amount
            print(f'\n\nAmount Withdrawn: ${amount}\nNew account Balance is: ${self.balance}\n\n')
            return self.balance

    def add_interest(self):
        # adds interest to the users balance, annual interest rate is 1%, 0.083%/month
        # interest = balance * 0.00083
        #Stretch challenge, add account type for either checking or savings to charge the correct amount of interest
        if (self.account_type == 'Checking'):
            interest = self.balance * 0.00083
        else:
            interest = self.balance * 0.001

        print(f'\n\nInterest has been charged on the {self.account_type} account for ${"{:.2f}".format(interest)}\n\n')
        self.balance -= interest
        return self.balance
    #print account information, hide the first 4 digits
    def print_statement(self):
        print(f"\n\n---------- {self.name}'s Statement ----------")
        print(f'\nAccount type: {self.account_type} \nAccount Numer: ****{str(self.account)[slice(4,8)]}\nBalance: ${"{:.2f}".format(self.balance)}\n')

class Bank:
    def __init__(self, full_name, create_account, deposit, withdraw, statement):
        self.full_name = full_name
        self.create_account = create_account
        self.deposit = deposit
        self.withdraw = withdraw
        self.statement = statement

# use randomint to create an 8 digit number for bank account
def account_number_generator():
    random_number = randint(00000000, 99999999)
    account_number = str(random_number)
    return account_number

#TEST

# #checking deposit and checking interest
# jeremys_account = BankAccount('Jeremy Renner', account_number_generator(), 'Checking', 10000)
# jeremys_account.print_statement()
# jeremys_account.deposit(1000)
# jeremys_account.add_interest()
# jeremys_account.print_statement

# #savings withdraw/overdraft and savings interest 
# bruces_account = BankAccount('Bruce Banner', account_number_generator(), 'Savings', 10000)
# bruces_account.withdraw(11000)
# bruces_account.print_statement()
# bruces_account.add_interest()
# bruces_account.print_statement()

mitchells_account = BankAccount('Mithcell Hudson', '03141592', 'Checking', 0)
mitchells_account.print_statement()
mitchells_account.deposit(400000)
mitchells_account.add_interest()
mitchells_account.print_statement()
mitchells_account.withdraw(150)
mitchells_account.print_statement()


