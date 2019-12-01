class Card:
    # Class Description:
    """The class for virtual ATM cards"""

    def __init__(self, id, pin, bankName, userName, expDate, errorCounter = 0 , isValid = True):
        # Holds the account ID (UserID in Bank Database)
        self.ID = id
        # Holds the Pin of the Card
        self.Pin = pin
        # Holds the Name of the Bank
        self.BankName = bankName
        # Holds the Name of the User
        self.UserName = userName
        # Holds the Card Expiration Date
        self.ExpDate = expDate
        # Hold the number of times Pin has Entered Incorrectly (Defaults to 0, unless initialized otherwise)
        self.ErrorCounter = errorCounter
        # Tells if the card is Valid (Defaults to True, unless initialized otherwise)
        self.IsValid = isValid

    def CheckPin(self, inputPin):
        # Method Description:
        """Checks if the correct Pin is entered for a valid card, invalidates cards after few attempts"""   
        # if the card is if valid and the pin is correct, reset error counter and returns true
        if self.IsValid and (self.Pin == inputPin):
          self.ErrorCounter = 0
          return True
        # if the pin is incorrect, increase the error counter and makes the card invalid if entered 5 times incorrectly
        else:
          self.ErrorCounter += 1
          if self.ErrorCounter > 5:
            self.IsValid = False
          return False

# A list of instances of cards with some random data for testing.
PredefinedCards = [
    Card(123456, 1568, "NBE", "Ahmed Saeed" , "Feb, 2020"),
    Card(234567, 1234, "NBE", "Mohammed Khalid" ,"Feb, 2020"),
    Card(345678, 8746, "NBE", "Osama Khalid" ,"Feb, 2020", 4),
    Card(456789, 5648, "NBE", "Hatiem Yasser" ,"Feb, 2020", 2),
    Card(567890, 1564, "NBE", "Samir Ganim" ,"Feb, 2020", 5, False),
]

def SearchCardsByID(searchID):
    # Method Description:
    """Returns a card instance By searching the list of PredefinedCards using a Number from 0 to (MaxIndex)"""
    # If the searchIndex is below length of predefinedcards, it gets that card item.
    for x in PredefinedCards:
        if x.ID == searchID: return x