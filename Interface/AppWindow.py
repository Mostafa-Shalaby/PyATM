from pathlib import Path
from tkinter import *
from Interface.AppStyles import ReturnCardButton
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
        self.title('PyATM')
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
            self.ReturnButton.pack(side=TOP, padx=(870,20), pady=(30,0))
            self.CurrentPage.destroy()
            self.CurrentPage=PinPage(self, PredefinedCards[cardIndex])
            self.CurrentPage.pack(side=TOP, pady=(45,0))
        else :
            self.ReturnCard("Invalid")

    def OpenServicePage(self,selectedCard):
        # Method Description
        """Switches to the Service Page"""
        self.CurrentPage.destroy()
        self.CurrentPage=ServicePage(self,selectedCard)
        self.CurrentPage.pack(side=TOP, pady=(55,0))