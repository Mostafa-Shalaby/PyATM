from pathlib import Path
from tkinter import *
from Interface.CardPage import CardPage
from Interface.PinPage import PinPage
from Interface.ThanksPage import ThanksPage
from Interface.ServicePage import ServicePage
from Modules.CardModule import PredefinedCards


class Window(Tk):
    # Class Description
    """Customized Window with preset values and background."""
    def __init__(self, *args, **kwargs):
        # Initalizes a tk window with the give parameters of the constructor.
        Tk.__init__(self, *args, **kwargs)
        
        # Creates Few Properties to Set Window Size.
        self.width = 1120
        self.height = 630
        self.minsize(self.width, self.height)

        #Sets Few attributes about the Window
        self.title = "PyATM"
        self['bg'] = "#0c3b97"

        # Set adds a background Image.
        self.Photo = PhotoImage(file=Path(__file__).parent / "Assets/Backdrop.png")
        Label(self, image=self.Photo).place(x=0, y=0, relwidth=1, relheight=1)
        # Removes the option to maximize.
        self.resizable(0,0)
        # Sets the window to the Center On launch.
        self.CenterWindow()
        # Pack in the first Page and saves it in a attribute!
        self.ReturnButton=ReturnCardButton(self, command=self.ReturnCard)
        self.CurrentPage=CardPage(self)
        self.CurrentPage.pack(side=LEFT, padx=(35,0))
    
    def CenterWindow(self):
        # Method Description
        """Center the window on launch depending on the screen size."""
        x = (self.winfo_screenwidth()/2) - (self.width/2)
        y = (self.winfo_screenheight()/2) - (self.height/2) - 40
        self.geometry('+%d+%d' % (x, y))

    def ReturnCard(self, mode="normal"):
        # Method Description
        """Returns Card and Resets the matchine"""
        self.CurrentPage.destroy()
        TempPage = ThanksPage(self,mode)
        TempPage.pack(pady=(140,0))
        TempPage.after(2500,TempPage.destroy)
        self.ReturnButton.pack_forget()
        self.CurrentPage=CardPage(self)
        self.after(2500,lambda: self.CurrentPage.pack(side=LEFT, padx=(35,0)))

    def OpenPinPage(self, cardIndex):
        # Method Description
        """Switches to Pin Page If Card is valid, else returns card"""
        if PredefinedCards[cardIndex].IsValid:
            self.ReturnButton.pack(side=TOP, padx=(890,0), pady=(30,0))
            self.CurrentPage.destroy()
            self.CurrentPage=PinPage(self, PredefinedCards[cardIndex])
            self.CurrentPage.pack(side=TOP, pady=(45,0))
        else :
            self.ReturnCard("Invalid")

    def OpenServicePage(self):
        # Method Description
        """Switches to the Service Page"""
        self.CurrentPage.destroy()
        self.CurrentPage=ServicePage(self)
        self.CurrentPage.pack(side=TOP)

class ReturnCardButton(Button):
     # Class Description
    """Stylized Buttons For Use In ATM Pin Controls"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Button.__init__(self, parent, *args, **kwargs)
        self['border'] = 0
        self['fg']="#f1f1f1"
        self['activebackground'] = "#004373"
        self['activeforeground'] = "#72a3ff"
        self['bg'] = "#0c3b97"
        self.photo = PhotoImage(file=Path(__file__).parent / "Assets/CustomButton2.png")    
        self.config(image=self.photo, compound = LEFT)
        # Binds the hover over events to a set of functions
        self.bind("<Enter>", self.OnEnter)
        self.bind("<Leave>", self.OnLeave)
    # When Mouse is Over
    def OnEnter(self, e):
        self['bg'] = "#0066ae"
    # When Mouse Leaves
    def OnLeave(self, e):
        self['bg'] = "#0c3b97"