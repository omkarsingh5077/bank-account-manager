class Account():
    
    def __init__(self, owner, balance=500):
        
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return(f"Owner: {self.owner} \nBalance: {self.balance}")
     
    
    
class CheckingAccount(Account):
        
    def __init__(self, owner, balance=0):
        Account.__init__(self, owner, balance=0)
        
        self.balance = balance
       
    def deposit(self, deposit_amount):
        
        self.deposit_amount = deposit_amount
        self.balance += deposit_amount
        print(f'You deposited {deposit_amount} to your checking account')
    
    def withdrawal(self, withdrawal_amount):
        
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
            print(f'You withdrew {withdrawal_amount} from your checking account')
        else:
            print('Sorry, insufficent funds!')
    
    def __str__(self):
        return(f"Owner: {self.owner} \nBalance: {self.balance}")

class SavingsAccount(Account):
    
    
    def __init__(self, owner, balance=0):
        Account.__init__(self, owner, balance=0)
        
        self.balance = balance
            
    def deposit(self, deposit_amount):
        
        self.deposit_amount = deposit_amount
        self.balance += deposit_amount
        print(f'You deposited {deposit_amount} to your savings account')
    
    def withdrawal(self, withdrawal_amount):
        
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
            print(f'You withdrew {withdrawal_amount} from your savings account')
        else:
            print('Sorry, insufficent funds!')
    
    def __str__(self):
        return(f"\nOwner: {self.owner} \nBalance: {self.balance}")
    
class BusinessAccount(Account):
    
    def __init__(self, owner, balance=0):
        Account.__init__(self, owner, balance=0)
        
        self.balance = balance
        
    def deposit(self, deposit_amount):
        
        self.deposit_amount = deposit_amount
        self.balance += deposit_amount
        print(f'You deposited {deposit_amount} to your business account')
    
    def withdrawal(self, withdrawal_amount):
        
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
            print(f'You withdrew {withdrawal_amount} from your business account')
        else:
            print('Sorry, insufficent funds!')
    
    def __str__(self):
        return(f"Owner: {self.owner} \nBalance: {self.balance}")
    
    
def verify_pin(pin):
        
        if pin == '1234':
            return True
        else:
            return False


b = BusinessAccount("\t Shashi", 1000)
c = CheckingAccount("\t Raju", 1000)
s = SavingsAccount("\t Gowda", 1000)


def welcome_message():
    print("\n Welcome to the ATM")   

    
def start_menu():
            
            print("""
            1:       Business Account
            2:       Checking Account
            3:       Savings Account
            4:       Exit
            """)

            Option = getUserInput()
            start_menu_handler(Option)


def start_menu_handler(Option):
    if Option == '1':
        main_menu(b)

    if Option == '2':
        main_menu(c)

    if Option == '3':
        main_menu(s)

    if Option == '4':
        print("Thank you for using our ATM! STAY SAFE!!")

def main_menu_handler(option, account):
    if option == '1':
        print(account.__str__())
        main_menu(account)

          
    elif option == '2':
        withdrawal_amount = int(input("How much would you like to withdraw?  "))
        account.withdrawal(withdrawal_amount)
        main_menu(account)

    
    elif option == '3':
          deposit_amount = int(input("How much would you like to deposit?  "))
          account.deposit(deposit_amount)
          main_menu(account)


    elif option == '4':
          start_menu()
    


def getUserInput():
    isInputValid = False

    while not(isInputValid):
        Option = input("Enter Option: ")
        if Option == '1' or Option == '2' or Option == '3' or Option == '4':
            isInputValid = True
            return Option
        else:
            print("Invalid input, please try again! ")



def print_account_menu():
    print("""
            1:    Balance
            2:    Withdraw
            3:    Deposit
            4:    Return to Main Menu
             """)


def main_menu(account):
            print_account_menu()
            option = getUserInput()
            main_menu_handler(option, account)


pinAttempts = 0
isValidPin = False    

    
while pinAttempts < 3 and not(isValidPin):

    pin = input("Please enter your four digit pin: ")
    pinAttempts += 1

    if verify_pin(pin):
        print("Successfully Logged-In!")
        isValidPin = True
        welcome_message()
        start_menu()

    elif (pinAttempts < 3):
        print("Invalid pin, please try again")
            

    elif (pinAttempts == 3):
        print("Too many incorrect tries, account locked!! ")