#Import Modules
from tkinter import *

class PinPage(Frame):
    # Class Description
    """Creates a Frame with NumPad and A Textbox to hold a Pin Number """
    def __init__(self, parent, *args, **kwargs):
        # Initalizes a frame with the give parameters of the constructor
        Frame.__init__(self, parent, bg=parent['bg'], *args, **kwargs)

        # Creates Few Properties to Manipulate the Interface
        self.InputPin = StringVar()
        self.SelectedCard = "Unknown"
        self.IsValidPin = "Unknown"
        self.background = parent['bg']

        # Populates The Frame With A NumPad and TextBox Entering Pin With Instruction Message.
        Label(self,text="Please enter your PIN.",font=("Segoe UI",18),fg="#f1f1f1",bg=self.background).pack(pady=(0,5))
        self.PinTextBox().pack(expand=1, fill=X)
        self.NumPad().pack(pady=(20,0))

    def NumPad(self):
        # Method Description:
        """Creates a Frame and populates it with Numbered Buttons"""

        # Create a Frame to hold the various controls/buttons and sets its background.
        padFrame = Frame(self, bg=self.background)

        # Initalizes NumPad Buttons and Puts them in different location in a Gird that is auto generated.
        NumPadButton(padFrame, text="1", command=lambda: self.WritePin("1")).grid(row=0,column=0, padx=2, pady=2)
        NumPadButton(padFrame, text="2", command=lambda: self.WritePin("2")).grid(row=0,column=1, padx=2, pady=2)
        NumPadButton(padFrame, text="3", command=lambda: self.WritePin("3")).grid(row=0,column=2, padx=2, pady=2)
        NumPadButton(padFrame, text="4", command=lambda: self.WritePin("4")).grid(row=1,column=0, padx=2, pady=2)
        NumPadButton(padFrame, text="5", command=lambda: self.WritePin("5")).grid(row=1,column=1, padx=2, pady=2)
        NumPadButton(padFrame, text="6", command=lambda: self.WritePin("6")).grid(row=1,column=2, padx=2, pady=2)
        NumPadButton(padFrame, text="7", command=lambda: self.WritePin("7")).grid(row=2,column=0, padx=2, pady=2)
        NumPadButton(padFrame, text="8", command=lambda: self.WritePin("8")).grid(row=2,column=1, padx=2, pady=2)
        NumPadButton(padFrame, text="9", command=lambda: self.WritePin("9")).grid(row=2,column=2, padx=2, pady=2)
        NumPadButton(padFrame, text="0", command=lambda: self.WritePin("0")).grid(row=3,column=1, padx=2, pady=2)
        # Control Buttons On the Side.
        ControlButton(padFrame,bg="#00b300",hbg="#00cc00",abg="#008000",text="Enter", command=lambda: self.EnterPin()).grid(row=3,column=0, padx=2, pady=2)
        ControlButton(padFrame,bg="#cc0058",hbg="#eb0066",abg="#990042",text="Clear", command=lambda: self.ClearPin()).grid(row=3,column=2, padx=2, pady=2)
        
        # ControlButton(padFrame,bg="#cc0058",hbg="#eb0066",abg="#990042", text="Cancel").grid(row=0,column=3, padx=(20,1), pady=1)
        return padFrame    
    
    def PinTextBox(self):
        # Method Description
        """Create The Frame and Textbox to Hold the pin."""

        # Create a Frame to hold the various controls/buttons and sets its background.
        pinFrame = Frame(self, bg="#333")
        
        # Initalizes an Entry Widget(TextBox) (That Will Show * Instead of The actual Value)
        pinEntry=Entry(pinFrame,text=self.InputPin, show="*", font=("Segoe UI", 15, "bold"), borderwidth=0, bg=pinFrame['bg'], fg="#fafafa",justify=CENTER, validate="key")
        # This will limit keyboard from entering letters, or more than 4 numbers into the Textbox
        pinEntry['validatecommand'] = (pinEntry.register(self.KeyChecker),'%P','%d','%s')
        # Packs/Puts the TextBox into the Frame and adds some Padding to it.
        pinEntry.pack(padx=10, pady=7, expand=1, fill=X)
        return pinFrame

    def WritePin(self, text):
        # Method Description
        """Types In the Number of the Button Being Clicked. (Not Exceeding 4 Digits)"""
        if len(self.InputPin.get()) < 4:
            self.InputPin.set(self.InputPin.get() + text)

    def ClearPin(self):
        # Method Description
        """Clears the Pin Value written in the Button"""
        self.InputPin.set("")
    
    def EnterPin(self):
        print(self.SelectedCard.ID)
        pass

    def GetCard(self, card):
        self.SelectedCard = card

    def KeyChecker(self,P,d,s):
        # Method Description
        """"Limits the Input From Keyboard into Textbox"""
        #If the Keyboard is trying to insert value
        if d == '1': 
            # If the value enter is a value and the current value is not longer than 4 char.
            if not (P.isdigit() and len(s) < 4):
                return False
        return True
    

# Hardcoded Stylized Widgets: (Subclass of Existing Widgets)
class NumPadButton(Button):
    # Class Description
    """Stylized Buttons For Use In A NumPads"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Button.__init__(self, parent, *args, **kwargs)
        self['width'] = 3
        self['padx'] = 21
        self['pady'] = 10
        self['font'] = ("Segoe UI", 16, "bold")
        self['border'] = 0
        self['bg']="#0077cc"
        self['fg']="#f1f1f1"
        self['activebackground'] = "#2257bf"
        self['activeforeground'] = "#004a80"
        # Binds the hover over events to a set of functions
        self.bind("<Enter>", self.OnEnter)
        self.bind("<Leave>", self.OnLeave)
    # When Mouse is Over
    def OnEnter(self, e):
        self['bg'] = "#0095ff"
    # When Mouse Leaves
    def OnLeave(self, e):
        self['bg'] = "#0077cc"

class ControlButton (Button):
    # Class Description
    """Stylized Buttons For Use In ATM Pin Controls"""
    def __init__(self, parent, hbg, abg, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Button.__init__(self, parent, *args, **kwargs)
        self['width'] = 3
        self['padx'] = 21
        self['pady'] = 10
        self['font'] = ("Segoe UI", 16, "bold")
        self['border'] = 0
        self['fg']="#f1f1f1"
        self['activebackground'] = abg
        self['activeforeground'] = "#afafaf"
        self.Background = self['bg']
        self.HoverColor = hbg
        # Binds the hover over events to `a set of functions
        self.bind("<Enter>", self.OnEnter)
        self.bind("<Leave>", self.OnLeave)
    # When Mouse is Over
    def OnEnter(self, e):
        self['bg'] = self.HoverColor
    # When Mouse Leaves
    def OnLeave(self, e):
        self['bg'] = self.Background