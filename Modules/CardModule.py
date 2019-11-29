class Card:
  # Class Description:
  """The class for virtual ATM cards"""

  # Holds the number of times pin has entered wrong
  ErrorCounter = 0
  # Tells if the card is Valid to be used in the 
  IsValid = True

  def __init__(self, ID, Pin, BankName, ExpDate):
    # Holds the account ID (UserID in Bank Database)
    self.ID = ID
    # Holds the Pin of the Card
    self.Pin = Pin
    # Holds the Name of the Bank
    self.BankName = BankName
    # Holds the Card Expiration Date
    self.ExpDate = ExpDate

  def CheckPin(self, InputPin):
    # Method Description:
    """Checks if the correct Pin is entered for a valid card, invalidates cards after few attempts"""
    
    # if the card is if valid and the pin is correct, reset error counter and returns true
    if self.IsValid and (self.Pin == InputPin):
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
  Card(123456, 1568, "NBE", "Feb, 2020"),
  Card(234567, 1234, "NBE", "Feb, 2020"),
  Card(345678, 8746, "NBE", "Feb, 2020"),
  Card(456789, 5648, "NBE", "Feb, 2020"),
  Card(567890, 1564, "NBE", "Feb, 2020"),
]