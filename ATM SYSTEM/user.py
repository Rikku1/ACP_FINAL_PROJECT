from checking import CheckingAccount
from savings import SavingsAccount

class User:
    def __init__(self, name, accountNumber, pin):
        # Initializing the user's name, account number, and PIN
        self.name = name
        self.name = name
        self.accountNumber = accountNumber
        self.pin = pin
        
        # Creating an instance of CheckingAccount for the user
        self.checking_account = CheckingAccount() 
        self.savings_account = SavingsAccount() # Creating an instance of SavingsAccount for the user
