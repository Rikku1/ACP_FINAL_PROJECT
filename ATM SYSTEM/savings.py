from useraccount import UserAccount
from datetime import datetime

class SavingsAccount(UserAccount):
    # Initialize the SavingsAccount object
    def __init__(self):
        super().__init__() # Call the UserAccount constructor
        self._interestRate = 0.03   # Set the default interest rate to 3% per annum
        self._lastInterestDate = datetime.now() # Record the date when interest was last applied

    # Property to get the interest rate
    @property
    def interestRate(self):
        return self._interestRate

    # Setter to update the interest rate
    @interestRate.setter
    def interestRate(self, rate):
        if rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self._interestRate = rate

    
    def calculateInterest(self): # Method to calculate and apply interest
        currentDate = datetime.now()
        
        elapsedTime = (currentDate - self._lastInterestDate).days / 365.0 # Calculate the time elapsed since the last interest application
        if elapsedTime > 0:
            interest = self.balance * self._interestRate * elapsedTime
            self.balance += interest  
            self._lastInterestDate = currentDate# Update the last interest date
            # Print the interest applied and the new balance
            print(f"Interest of {interest:.2f} applied. New Balance: {self.balance:.2f}")

    
    def showBalance(self): # Method to display the account balance
        # Calculate and apply interest before displaying the balance
        self.calculateInterest()
        super().showBalance()

    def deposit(self, amount):
        # Calculate and apply interest before depositing funds
        self.calculateInterest()
        super().deposit(amount)


    def withdraw(self, amount):
        # Calculate and apply interest before withdrawing funds
        self.calculateInterest()
        super().withdraw(amount)


    def menu(self):
        # Call the UserAccount accountsMenu method
        self.accountsMenu()