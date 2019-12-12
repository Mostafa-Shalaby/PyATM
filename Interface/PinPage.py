#Import Modules
from tkinter import *
from pathlib import Path
from Interface.AppStyles import PinPadButton, PinControlButton

class PinPage(Frame):
    # Class Description
    """Creates a Frame with NumPad and A Textbox to hold a Pin Number """
    def __init__(self, parent, card, *args, **kwargs):
        # Initalizes a frame with the give parameters of the constructor
        Frame.__init__(self, parent, bg=parent['bg'], *args, **kwargs)

        # Creates Few Properties to Manipulate the Interface
        self.InputPin = StringVar()
        self.SelectedCard = card
        self.Background = parent['bg']
        self.Parent = parent

        # Populates The Frame With A NumPad and TextBox Entering Pin With Instruction Message.
        self.Photo = PhotoImage(file=Path(__file__).parent / "Assets/Message4.png")
        Label(self, image=self.Photo, bg=self.Background).pack()
        self.PinTextBox().pack(expand=1, fill=X, padx=2)
        self.NumPad().pack(pady=(8,0))
        self.StatusMessage = Label(self,text="",font=("Segoe UI",12,'bold'),fg="#ffd400",bg=self.Background)
        self.StatusMessage.pack(pady=(5,0))

    def NumPad(self):
        # Method Description:
        """Creates a Frame and populates it with Numbered Buttons"""

        # Create a Frame to hold the various controls/buttons and sets its Background.
        padFrame = Frame(self, bg=self.Background)

        # Initalizes NumPad Buttons and Puts them in different location in a Gird that is auto generated.
        PinPadButton(padFrame, text="1", command=lambda: self.WritePin("1")).grid(row=0,column=0, padx=2, pady=2)
        PinPadButton(padFrame, text="2", command=lambda: self.WritePin("2")).grid(row=0,column=1, padx=2, pady=2)
        PinPadButton(padFrame, text="3", command=lambda: self.WritePin("3")).grid(row=0,column=2, padx=2, pady=2)
        PinPadButton(padFrame, text="4", command=lambda: self.WritePin("4")).grid(row=1,column=0, padx=2, pady=2)
        PinPadButton(padFrame, text="5", command=lambda: self.WritePin("5")).grid(row=1,column=1, padx=2, pady=2)
        PinPadButton(padFrame, text="6", command=lambda: self.WritePin("6")).grid(row=1,column=2, padx=2, pady=2)
        PinPadButton(padFrame, text="7", command=lambda: self.WritePin("7")).grid(row=2,column=0, padx=2, pady=2)
        PinPadButton(padFrame, text="8", command=lambda: self.WritePin("8")).grid(row=2,column=1, padx=2, pady=2)
        PinPadButton(padFrame, text="9", command=lambda: self.WritePin("9")).grid(row=2,column=2, padx=2, pady=2)
        PinPadButton(padFrame, text="0", command=lambda: self.WritePin("0")).grid(row=3,column=1, padx=2, pady=2)
        # Control Buttons On the Side.
        PinControlButton(padFrame,bg="#00b300",hbg="#00cc00",abg="#008000",text="Enter", command=lambda: self.EnterPin()).grid(row=3,column=0, padx=2, pady=2)
        PinControlButton(padFrame,bg="#cc0058",hbg="#eb0066",abg="#990042",text="Clear", command=lambda: self.ClearPin()).grid(row=3,column=2, padx=2, pady=2)     
        return padFrame    
    
    def PinTextBox(self):
        # Method Description
        """Create The Frame and Textbox to Hold the pin."""

        # Create a Frame to hold the various controls/buttons and sets its Background.
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
        # Method Description
        """Checks the Entered PIN Pin Value written in the Button"""
        try:
            pin = int(self.InputPin.get())
            if self.SelectedCard.CheckPin(pin):
                self.Parent.OpenServicePage(self.SelectedCard)
            else:
                if (self.SelectedCard.ErrorCounter < 5):
                    self.StatusMessage.config(text="Incorrect Pin, Remaining Retries: "+str(5-self.SelectedCard.ErrorCounter))
                else:
                    self.Parent.ReturnCard("Invalid")
            self.ClearPin()
        except: pass

    def KeyChecker(self,P,d,s):
        # Method Description
        """"Limits the Input From Keyboard into Textbox"""
        #If the Keyboard is trying to insert value
        if d == '1': 
            # If the value enter is a value and the current value is not longer than 4 char.
            if not (P.isdigit() and len(s) < 4):
                return False
        return True