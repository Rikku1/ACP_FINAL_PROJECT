from user import User

class ATM:
    def __init__(self):
        self.users = {} # Dictionary to store user information

    def createAccount(self):
        print("===================================")
        name = input("Enter your full name: ") # Get user's name
        account_number = input("Set an 8-digit Account Number: ") # Prompt for account number 
        while len(account_number) != 8 or not account_number.isdigit(): # Validate that the account number is 8 digits and numeric
            print("Invalid Account Number! Must be an 8-digit number.")
            account_number = input("Set an 8-digit Account Number: ")
        if account_number in self.users: # Check if account already exist
            print("Account Number already exists. Please choose a different Account Number.")
            return
        pin = input("Set a 4-digit PIN: ") # Prompt for PIN
        while len(pin) != 4 or not pin.isdigit(): # Validate that the PIN is 4 digits and numeric
            print("Invalid PIN! Must be a 4-digit number.")
            pin = input("Set a 4-digit PIN: ")

        # Create a User instance and store it using the account number as the key
        self.users[account_number] = User(name, account_number, pin)
        print(f"Account created successfully for {name} with Checking and Savings accounts!")

    def login(self):
        print("=== Login ===")
        account_number = input("Enter your 8-digit Account Number: ")
        pin = input("Enter your 4-digit PIN: ")

        user = self.users.get(account_number)
        if user and user.pin == pin:
            print("Login successful!")
            return user
        else:
            print("Invalid Account Number or PIN. Please try again.")
            return None

    def typeMenu(self, user):
        while True:
            print("===================================")
            print("|        ATM Menu                |")
            print("===================================")
            print("  1. Checking Account\n  2. Savings Account\n  3. Logout")
            choice = input("Select an option: ")

            if choice == "1":
                user.checking_account.menu()
            elif choice == "2":
                user.savings_account.menu()
            elif choice == "3":
                print("Logged out successfully.")
                break
            else:
                print("Invalid Input! Try Again.")

    def mainMenu(self):
        while True:
            print("===================================")
            print("|        Welcome to ATM           |")
            print("===================================")
            print("  1. Create Account\n  2. Login\n  3. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                self.createAccount()
            elif choice == "2":
                user = self.login()
                if user:
                    self.typeMenu(user)
            elif choice == "3":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid Input! Try Again.")
