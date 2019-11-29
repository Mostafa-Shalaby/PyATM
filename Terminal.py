import Modules.CardModule as CardModule

# Testing Input
def AskForPin():
  i= int(input("Please Choose A Card 1-5: ")) - 1
  pin = int(input("Please Enter Card Pin: "))
  SelectedCard = CardModule.PredefinedCards[i]
  if SelectedCard.CheckPin(pin):
    print("Welcome To PyATM")
  else:
    if SelectedCard.IsValid:
      print("Incorrect Pin")
      print("Remaining Retries:", 5-CardModule.PredefinedCards[i].ErrorCounter)
      retry = input("Would U like to Try Again? Y/N: ")
      if retry == "Y": AskForPin()
      else: print("Thank You for Using PyATM")
    else:
      print("Invalid Card")
  pass

AskForPin()