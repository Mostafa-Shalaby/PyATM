# Imported Modules
import Modules.CardModule as CardModule
import Modules.DbModule as DbModule
import Modules.CalculationModule as CalculationModule

# A dictionary for available bills and their count in PyATM {bill: bill_count}
bills = {20: 200, 50: 150, 100: 100, 200: 50}

def SelectCard():
    # Method Description:
    """Selects A Card Using A Terminal As UI"""

    # Endless Loop Till User Enters A Valid Card Number
    while(True):
        # Prompt user to select card
        i= int(input("Please choose a card: "))
        # If the position entered is correct
        if (i > 0) and (i < len(CardModule.PredefinedCards) + 1):
            break
        else:
            print("Invalid Input, Please Try Another Card.")

    # Holds and gets a card using a valid index.
    selectedCard = CardModule.PredefinedCards[i-1]

    # Checks if the card is valid and displays corresponding messages.
    if (selectedCard.IsValid == True):
        print ("Welcome", selectedCard.UserName, "!")
        return selectedCard
    else:
        print("This card has been deactivated or invalid, please contact your bank.")
        pass

def AskForPin(userCard):
    # Method Description:
    """Asks and Checks the Pin of a Given Card in A Terminal As UI"""

    # Endless Loop Till User Enters A correct PIN or cancels
    while(True):
        pin = int(input("Please Enter Card Pin: "))
        if userCard.CheckPin(pin):
            print("Welcome To PyATM")
            return True
        else:
            print("Incorrect Pin!")
            if (userCard.ErrorCounter == 5):
                print("Pin has been entered incorrectly too many times, Card deactivated!")
                return False
            print("Remaining Retries:", 5-userCard.ErrorCounter)
            retry = input("Would U like to Try Again? Y/N: ")
            if retry not in ["Y","y","Yes","yes","Yea","yea"]:
                return False

def SelectService(userCard):
    # Method Description:
    """Selects and Runs Different ATM Services in A Terminal As UI"""

    # Endless Loop For User To Select a Service
    while(True):
        print("Avaliable Services Are:", "1. Check Balance", "2. Withdraw", "3. Deposit", "4. Transaction History", "5. Quit", sep="\n")
        service = input("Which Service would u like to use: ")

        # First Service Avaliable is (Checking Balance)
        if service in ["1", "Check Balance", "check balance", "Balance", "balance"]:
            currentBalance, currency = DbModule.BalanceCheck(userCard.ID, userCard.accountType)
            print("Your Current Balance is:", str(currentBalance) + ' ' + currency, sep='\n')
            retry = input("Would U like to Use Another Service? Y/N: ")
            if retry not in ["Y","y","Yes","yes","Yea","yea"]:
                break

        # Second Service is (Withdraw) [Ammar]
        elif service in ["2", "withdraw", "Withdraw"]:

            # Amount to be withdrawn
            # Enter a loop until a valid amount is entered
            while(True):
                amount = int(input("Enter the amount you want to withdraw: "))
                if amount > 0: break

            # Check if the client has enough amount in balance
            oldBalance, currency = DbModule.BalanceCheck(userCard.ID, userCard.accountType)

            # If the amount > oldBalance enter a loop until a valid amount is entered
            while(True):
                if amount > oldBalance or amount < 0:
                    if amount > oldBalance:
                        print("Sorry, not enough cash in your balance, " + str(oldBalance) + ' ' + currency + "! Please, try again!")
                    amount = int(input("Enter the amount you want to withdraw: "))
                else:
                    break

            # Deduct the amount from the balance in the database
            DbModule.UpdateBalance((oldBalance - amount), userCard.ID, userCard.accountType)

            # Record the transaction
            DbModule.RecordTrans(userCard.ID, userCard.accountType, 'withdraw', amount)

            # Balance after withdraw
            newBalance, currency = DbModule.BalanceCheck(userCard.ID, userCard.accountType)
            print("Your Transaction Done Successfully!", "Your balance now is ", str(newBalance) + ' ' + currency, sep='\n')

            # Eject cash
            amount_bills = CalculationModule.GetMinBills([bill for bill in bills], amount)
            for bill in bills:
                bill_count = amount_bills.count(bill)
                print(bill, bill_count, sep=' ==> ')

            retry = input("Would U like to Use Another Service? Y/N: ")
            if retry not in ["Y", "y", "Yes", "yes", "Yea", "yea"]:
                break

        # Third service is deposit
        elif service in ["3", "deposit", "Deposit"]:

            # Amount to be deposited
            # Enter a loop until a valid amount is entered
            while(True):
                amount = int(input("Enter the amount you want to deposit: "))
                if amount > 0: break

            # Add the amount to the balance in the database
            oldBalance, currency = DbModule.BalanceCheck(userCard.ID, userCard.accountType)
            DbModule.UpdateBalance((oldBalance + amount), userCard.ID, userCard.accountType)

            # Record the transaction
            DbModule.RecordTrans(userCard.ID, userCard.accountType, 'deposit', amount)

            # Balance after depositing
            newBalance, currency = DbModule.BalanceCheck(userCard.ID, userCard.accountType)
            print("Your Transaction Done Successfully!", "Your balance now is ", str(newBalance) + ' ' + currency, sep='\n')

            retry = input("Would U like to Use Another Service? Y/N: ")
            if retry not in ["Y", "y", "Yes", "yes", "Yea", "yea"]:
                break

        # Fourth service is Transaction history
        elif service in ["4", "Transaction History", "transaction history", "History", "history", "Transaction", "transaction"]:
            # Retrieve the transaction history from the database
            trans = DbModule.TransCheck(userCard.ID, userCard.accountType)

            # Print the transaction history
            for log in trans:
                print(log)

        # Exit point
        elif service in ["5", "Quit", "quit"]:
            break

        # For invalid entries, display a message, and loop the function.
        else:
            print("Invalid Input, Please choose one of the Avaliable Services")

    print("Thank you for Using PyATM")
    print("Card Returned!")
    pass

# Main Function:-

# Selects Card
UserCard = SelectCard()

# Checks the Pin
if (UserCard):
    access = AskForPin(UserCard)

# If access is granted continues doing stuff...
if (access):
    print("Your Account type is", UserCard.accountType)
    SelectService(UserCard)

# if access is denied, card is returned.
else:
    print("Card Returned!")
