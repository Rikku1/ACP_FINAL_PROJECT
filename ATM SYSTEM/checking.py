from useraccount import UserAccount

class CheckingAccount(UserAccount): 
    
    def menu(self): # Define a method menu that calls the accountsMenu method
        self.accountsMenu() # Call the accountsMenu method to display the accounts menu
