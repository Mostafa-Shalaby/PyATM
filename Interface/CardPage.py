#Import Modules
from tkinter import *
from pathlib import Path

class CardPage(Frame):
    # Class Description
    """Creates a Frame that Ask to Enter A Card / Select Preset One."""
    def __init__(self, parent, *arg, **kwargs):
        # Initalizes a frame with the give parameters of the constructor.
        Frame.__init__(self, parent, bg=parent['bg'], *arg, **kwargs)
        
        # Creates Few Properties to Manipulate the Interface.
        self.CardIndex = IntVar(value=10)
        self.Background = parent['bg']
        self.Photo = ""

        # Populates the frame with the CardButtons.
        self.CardButtons().grid(row=0,column=0,sticky=NSEW)
        # Populates the frame with an instruction Image.
        self.Photo = PhotoImage(file=Path(__file__).parent / "Assets/Message1.png")
        Label(self, image=self.Photo, bg=self.Background).grid(row=0,column=1,padx=(70,0))
    
    def CardButtons(self):
        # Method Description:
        """Creates a Frame and populates it with Numbered Card Buttons"""

        # Create a Frame to hold the various controls/buttons and sets its background.
        cardFrame = Frame(self, bg=self.Background)

        # Initalizes Card Buttons and puts them in column one after another.
        CardButton(cardFrame,text="Card 1", command=lambda: self.SelectCard(0)).grid(row=0,column=0,pady=5)
        CardButton(cardFrame,text="Card 2", command=lambda: self.SelectCard(1)).grid(row=1,column=0,pady=5)
        CardButton(cardFrame,text="Card 3", command=lambda: self.SelectCard(2)).grid(row=2,column=0,pady=5)
        CardButton(cardFrame,text="Card 4", command=lambda: self.SelectCard(3)).grid(row=3,column=0,pady=5)
        CardButton(cardFrame,text="Card 5", command=lambda: self.SelectCard(4)).grid(row=4,column=0,pady=5)
        return cardFrame
    
    def SelectCard(self, cardIndex):
        # Method Description
        """Selects The Card Index Using the CardButtons"""
        self.CardIndex.set(cardIndex)


# Hardcoded Stylized Widgets: (Subclass of Existing Widgets)
class CardButton(Button):
     # Class Description
    """Stylized Buttons For Use In ATM Pin Controls"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Button.__init__(self, parent, *args, **kwargs)
        self['padx'] = 18
        self['pady'] = 8
        self['font'] = ("Segoe UI", 14, "bold")
        self['border'] = 0
        self['fg']="#f1f1f1"
        self['activebackground'] = "#004373"
        self['activeforeground'] = "#72a3ff"
        self['bg'] = "#0066ae"
        self.photo = PhotoImage(file=Path(__file__).parent / "Assets/Card1.png") 
        self.logo = self.photo.subsample(4)      
        self.config(image=self.logo, compound = LEFT)
        # Binds the hover over events to a set of functions
        self.bind("<Enter>", self.OnEnter)
        self.bind("<Leave>", self.OnLeave)
    # When Mouse is Over
    def OnEnter(self, e):
        self['bg'] = "#0077cc"
    # When Mouse Leaves
    def OnLeave(self, e):
        self['bg'] = "#0066ae"