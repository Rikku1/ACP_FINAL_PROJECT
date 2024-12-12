from useraccount import UserAccount
from datetime import datetime

class SavingsAccount(UserAccount):
    def __init__(self):
        super().__init__()
        self._interestRate = 0.03  # 3% annual interest
        self._lastInterestDate = datetime.now()

    @property
    def interestRate(self):
        return self._interestRate

    @interestRate.setter
    def interestRate(self, rate):
        if rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self._interestRate = rate

    def calculateInterest(self):
        currentDate = datetime.now()
        elapsedTime = (currentDate - self._lastInterestDate).days / 365.0
        if elapsedTime > 0:
            interest = self.balance * self._interestRate * elapsedTime
            self.balance += interest
            self._lastInterestDate = currentDate
            print(f"Interest of {interest:.2f} applied. New Balance: {self.balance:.2f}")

    def showBalance(self):
        self.calculateInterest()
        super().showBalance()

    def deposit(self, amount):
        self.calculateInterest()
        super().deposit(amount)

    def withdraw(self, amount):
        self.calculateInterest()
        super().withdraw(amount)

    def menu(self):
        self.accountsMenu()
