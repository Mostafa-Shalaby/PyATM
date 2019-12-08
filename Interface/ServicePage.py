from tkinter import *
from pathlib import Path

class ServicePage(Frame):
    # Class Description
    """Creates a Frame that holds the service options """
    def __init__(self, parent, card, *args, **kwargs):
        # Initalizes a frame with the give parameters of the constructor
        Frame.__init__(self, parent, bg=parent['bg'], *args, **kwargs)

        # Creates Few Properties to Manipulate the Interface
        self.Background = parent['bg']
        self.SelectedCard = card

        # Populates the Frame
        self.UserDescriptor().grid(row=0,column=0,padx=(0,145),pady=10,sticky=NW)
        self.ServiceSelector().grid(row=0,column=1,pady=10, sticky=W)
        self.QuickCash().grid(row=1,column=1,pady=(20,0),sticky=NSEW)

    def UserDescriptor(self):
        # Method Description:
        """Creates a Frame and populates it with Numbered Buttons"""
        # Create a Frame to hold the various controls/buttons and sets its Background.
        userFrame = Frame(self, bg=self.Background)
        TitleLabel(userFrame, text="Welcome,").pack(anchor=W)
        DetailsLabel(userFrame, text=self.SelectedCard.UserName).pack(anchor=W)
        TitleLabel(userFrame, text="Account Type:").pack(anchor=W)
        DetailsLabel(userFrame, text=self.SelectedCard.accountType).pack(anchor=W)
        return userFrame

    def ServiceSelector(self):
        # Method Description:
        """Creates a Frame and populates it with Numbered Buttons"""
        # Create a Frame to hold the various controls/buttons and sets its Background.
        selectorFrame = Frame(self, bg=self.Background)
        TitleLabel(selectorFrame, text="Available Services:").grid(row=0,column=0,padx=(5,10),pady=(5,10), sticky=W)
        ServiceButton(selectorFrame,text="Withdraw").grid(row=1,column=0,padx=(5,10),pady=(5,10))
        ServiceButton(selectorFrame,text="Deposit").grid(row=1,column=1,padx=(10,5),pady=(5,10))
        ServiceButton(selectorFrame,text="Balance").grid(row=2,column=0,padx=(5,10),pady=(10,5))
        ServiceButton(selectorFrame,text="Transactions").grid(row=2,column=1,padx=(10,5),pady=(10,5))
        return selectorFrame

    def QuickCash(self):
        quickFrame = Frame(self, bg=self.Background)
        QuickButton(quickFrame,text="Quick Cash - 100 L.E.").pack(expand=1, fill=X)
        return quickFrame


# Hardcoded Stylized Widgets: (Subclass of Existing Widgets)
class ServiceButton(Button):
     # Class Description
    """Stylized Buttons For Use In ATM Service Selection Controls"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Button.__init__(self, parent, *args, **kwargs)
        self['width'] = 26
        self['height'] = 2
        self['border'] = 0
        self['font'] = ("Calibri", 19, "bold")
        self['bg']="#0077cc"
        self['fg']="#f1f1f1"
        self['activebackground'] = "#2257bf"
        self['activeforeground'] = "#afafaf"
        # self.photo = PhotoImage(file=Path(__file__).parent / photoname)  
        # self.config(image=self.photo, compound = CENTER)
        # Binds the hover over events to a set of functions
        self.bind("<Enter>", self.OnEnter)
        self.bind("<Leave>", self.OnLeave)
    # When Mouse is Over
    def OnEnter(self, e):
        self['bg'] = "#0095ff"
    # When Mouse Leaves
    def OnLeave(self, e):
        self['bg'] = "#0077cc"

class QuickButton(Button):
    # Class Description
    """Stylized Buttons For Use In ATM Quick Cash Service"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Button.__init__(self, parent, *args, **kwargs)
        self['height'] = 1
        self['font'] = ("Calibri", 19, "bold")
        self['border'] = 0
        self['bg'] = "#e5ac00"
        self['fg'] = "#f1f1f1"
        self['activebackground'] = "#bf8f00"
        self['activeforeground'] = "#afafaf"
        # Binds the hover over events to `a set of functions
        self.bind("<Enter>", self.OnEnter)
        self.bind("<Leave>", self.OnLeave)
    # When Mouse is Over
    def OnEnter(self, e):
        self['bg'] = "#ffbf00"
    # When Mouse Leaves
    def OnLeave(self, e):
        self['bg'] = "#e5ac00"

class TitleLabel(Label):
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Label.__init__(self, parent, *args, **kwargs)
        self['font'] = ("Calibri", 24, "bold")
        self['border'] = 0
        self['justify'] = LEFT
        self['bg'] = "#0c3b97"
        self['fg'] = "#f1f1f1"
    
class DetailsLabel(Label):
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Label.__init__(self, parent, *args, **kwargs)
        self['font'] = ("Calibri", 18)
        self['border'] = 0
        self['anchor'] = W
        self['justify'] = LEFT
        self['bg'] = "#0c3b97"
        self['fg'] = "#1a96dc"