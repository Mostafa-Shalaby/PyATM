# Imports Interface and tkinter modules
from Interface.AppWindow import *
from Interface.CardPage import *
from Interface.PinPage import *
from tkinter import *
from Modules import CardModule

# Code For Testing, Will be commented next commit when finilized.
# i am done FAR FAR from done it.
# this script is mostly experimental
# it will be rewritten
# But do run this script to see where the GUI is at.

print()
def CardCheck(a,b,c):
    if cardPage.CardIndex.get() in (0,1,2,3,4):
        cardPage.pack_forget()
        SelectedCardIndex = cardPage.CardIndex.get()
        pinPage.GetCard(CardModule.PredefinedCards[SelectedCardIndex])
        print(pinPage.SelectedCard.UserName)
        pinPage.pack(side=LEFT, padx=(428,0))

root = Window()
cardPage = CardPage(root)
pinPage = PinPage(root)
cardPage.pack(side=LEFT, padx=(35,0))
cardPage.CardIndex.trace('w',CardCheck)
if cardPage.CardIndex.get() in (0,1,2,3,4):
    cardPage.pack_forget()
root.mainloop()