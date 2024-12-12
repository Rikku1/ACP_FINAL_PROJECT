from abc import ABC, abstractmethod
 
class UserAccount(ABC):
    def __init__(self):
        self._balance = 0.0
        self._MAXBALANCE = 10000000.0
        self._TRANSACTIONFEE = 12.0

    @property # Getter for balance
    def balance(self):
        return self._balance

    @balance.setter # Setter for balance
    def balance(self, amount): # Use setter to validate balance
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        elif amount > self._MAXBALANCE:
            raise ValueError(f"Balance exceeds maximum limit of {self._MAXBALANCE} PHP.")
        self._balance = amount # Set the new balance

    @abstractmethod 
    def menu(self): # Abstract method for menu to be implemented by subclass
        pass

    def showBalance(self): # Display the current account balance
        print(f"Account balance: {self.balance:.2f} PHP")

    def deposit(self, amount): # Deposit method
        try: # Error handling
            if amount <= 0:
                raise ValueError("Cannot deposit negative or zero amount!")
            self.balance += amount
            print(f"New Account Balance: {self.balance:.2f} PHP")
        except ValueError as e: # Error handling
            print(e)

    def withdraw(self, amount): # Withdraw method
        try: # Error handling
            if amount <= 0:
                raise ValueError("Cannot withdraw negative or zero amount!")
            if (amount + self._TRANSACTIONFEE) > self.balance:
                print("Insufficient balance! Please try again.")
                return
            self.balance -= (amount + self._TRANSACTIONFEE)
            print(f"New Account Balance: {self.balance:.2f} PHP")
        except ValueError as e: # Error handling
            print(e)

    def accountsMenu(self): # Menu for checking and savings
        while True:
            print("===================================")
            print("|      ATM     |")
            print("===================================")
            print("  1. Check Balance\n  2. Deposit\n  3. Withdraw\n  4. Back")
            print("-----------------------------------")
            choice = input("Select an option: ")
            print("-----------------------------------")
            try: # Error handling
                if choice == "1":
                    self.showBalance() # Display balance
                elif choice == "2":
                    money = float(input("Enter amount to deposit: "))
                    self.deposit(money) # Deposit money
                elif choice == "3":
                    print(f"Note: {self._TRANSACTIONFEE:.2f} PHP transaction fee applies.")
                    money = float(input("Enter amount to withdraw: ")) 
                    self.withdraw(money) # Withdraw money
                elif choice == "4":
                    break
                else:
                    print("Invalid Input! Try Again.")
            except ValueError: # Error handling
                print("Invalid amount! Please enter a valid number.")
