# Imported Modules
import Modules.CardModule as CardModule

def SelectCard():
    # Method Description:
    """Selects A Card Using A Terminal As UI"""
    # Endless Loop Till User Enters A Valid Card Number
    while(True):
        # Prompt user to select card
        i= int(input("Please choose a card: "))
        # If the position entered is correct
        if (i > 0) and (i < len(CardModule.PredefinedCards) + 1): break
        else: print("Invalid Input, Please Try Another Card.")
    # Holds and gets a card using a valid index.
    selectedCard = CardModule.PredefinedCards[i-1]
    # Checks if the card is valid and displays corresponding messages.
    if (selectedCard.IsValid == True): 
        print ("Welcome", selectedCard.UserName, "!")
        return selectedCard
    else: 
        print("This card has been deactivated or invalid, please contact your nank.")
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

# Main Function:-

# Selects Card
UserCard = SelectCard()
# Checks the Pin
if (UserCard): access = AskForPin(UserCard)
# If access is granted continues doing stuf...
if (access): print("you can do bla bla bla bla......")
# if access is denied, card is returned.
else: print("Card Returned!")