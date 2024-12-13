from user import User

class ATM:
    def __init__(self):
        self.users = {} # Dictionary to store user information

    def createAccount(self):
        print("****************************************************************************")
        print("*\t\t\t\t\t\t\t\t\t   *")
        print("*\t\t\t\tCREATE ACCOUNT\t\t\t\t   *")
        print("*\t\t\t\t\t\t\t\t\t   *")
        print("****************************************************************************")
        name = input("  Enter your full name: ") # Get user's name
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
        print("****************************************************************************")
        print("*\t\t\t\t\t\t\t\t\t   *")
        print("*\t\t\t\t  LOG IN\t\t\t\t   *")
        print("*\t\t\t\t\t\t\t\t\t   *")
        print("****************************************************************************")
        account_number = input("  Enter your 8-digit Account Number: ") # Prompt for Account number 
        pin = input("  Enter your 4-digit PIN: ") # Prompt for pin

        user = self.users.get(account_number)  # Retrieve user information from dictionary using account number
        if user and user.pin == pin:  # Check if user exists and PIN matches
            print("Login successful!")
            return user  
        else:
            print("Invalid Account Number or PIN. Please try again.")  # Display error message
            return None

    def typeMenu(self, user):
        while True:
            print("****************************************************************************")
            print("*\t\t\t\t\t\t\t\t\t   *")
            print("*\t\t\t\t  ACCOUNT MENU\t\t\t\t   *")
            print("*\t\t\t\t\t\t\t\t\t   *")
            print("****************************************************************************")
            print("  1. Checking Account\n  2. Savings Account\n  3. Logout")
            choice = input("Select an option: ")

            if choice == "1":
                
                user.checking_account.menu() # Display the checking account menu
            elif choice == "2":
                
                user.savings_account.menu() # Display the savings account menu
            elif choice == "3":
                print("Logged out successfully.")
                break
            else:
                print("Invalid Input! Try Again.")

    def mainMenu(self):
        while True:
            print("****************************************************************************")
            print("*\t\t\t\t\t\t\t\t\t   *")
            print("*\t\t\t\t  MAIN MENU\t\t\t\t   *")
            print("*\t\t\t\t\t\t\t\t\t   *")
            print("****************************************************************************")
            print("  1. Create Account\n  2. Login\n  3. Exit")
            choice = input("Select an option: ")

            # Create a new account
            if choice == "1":
                self.createAccount()
            # Login to an existing account
            elif choice == "2":
                user = self.login()
                # If login is successful, display account menu
                if user:
                    self.typeMenu(user)
            # Exit the ATM system
            elif choice == "3":
                print("Thank you for using the ATM. Goodbye!")
                break
            # Handle invalid input
            else:
                print("Invalid Input! Try Again.")
