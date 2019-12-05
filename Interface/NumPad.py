from tkinter import *
# Classes Are HardCoded Stylized Subclass of Buttons
# To avoid restyling them each time a new one is created.
class NumPadButton(Button):
    # Class Description
    """Stylized Buttons For Use In A NumPads"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Button.__init__(self, parent, *args, **kwargs)
        self['width'] = 2
        self['padx'] = 21
        self['pady'] = 10
        self['font'] = ("Segoe UI", 15)
        self['border'] = 0
        self['bg']="#01b4f6"
        self['fg']="#fafafa"
        self['activebackground'] = "#2257bf"
        self['activeforeground'] = "#72a3ff"
        # Binds the hover over events to a set of functions
        self.bind("<Enter>", self.OnEnter)
        self.bind("<Leave>", self.OnLeave)
    # When Mouse is Over
    def OnEnter(self, e):
        self['bg'] = "#2d9de7"
    # When Mouse Leaves
    def OnLeave(self, e):
        self['bg'] = "#01b4f6"

class ControlButton (Button):
    # Class Description
    """Stylized Buttons For Use In ATM Pin Controls"""
    def __init__(self, parent, hovercolor, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Button.__init__(self, parent, *args, **kwargs)
        self['width'] = 2
        self['padx'] = 40
        self['pady'] = 10
        self['font'] = ("Segoe UI", 15, "bold")
        self['border'] = 0
        self['fg']="#fafafa"
        self['activebackground'] = "#333333"
        self['activeforeground'] = "#afafaf"
        self.Background = self['bg']
        self.HoverColor = hovercolor
        # Binds the hover over events to a set of functions
        self.bind("<Enter>", self.OnEnter)
        self.bind("<Leave>", self.OnLeave)
    # When Mouse is Over
    def OnEnter(self, e):
        self['bg'] = self.HoverColor
    # When Mouse Leaves
    def OnLeave(self, e):
        self['bg'] = self.Background


def NumPadFrame(parent, inputPin):
    # Method Description:
    """Creates a Frame and populates it with Numbered Buttons"""
    # Create a Frame to hold the various controls/buttons and sets its background.
    numFrame = Frame(parent, bg=parent['bg'])
    numFrame['bg'] = parent['bg']
    # Initalizes Various Buttons and Puts them in different location in a gird that is auto generated.
    # NumPad Buttons
    button1=NumPadButton(numFrame, text="1", command=lambda: WritePin("1", inputPin)).grid(row=0,column=0, padx=2, pady=2)
    button2=NumPadButton(numFrame, text="2", command=lambda: WritePin("2", inputPin)).grid(row=0,column=1, padx=2, pady=2)
    button3=NumPadButton(numFrame, text="3", command=lambda: WritePin("3", inputPin)).grid(row=0,column=2, padx=2, pady=2)
    button4=NumPadButton(numFrame, text="4", command=lambda: WritePin("4", inputPin)).grid(row=1,column=0, padx=2, pady=2)
    button5=NumPadButton(numFrame, text="5", command=lambda: WritePin("5", inputPin)).grid(row=1,column=1, padx=2, pady=2)
    button6=NumPadButton(numFrame, text="6", command=lambda: WritePin("6", inputPin)).grid(row=1,column=2, padx=2, pady=2)
    button7=NumPadButton(numFrame, text="7", command=lambda: WritePin("7", inputPin)).grid(row=2,column=0, padx=2, pady=2)
    button8=NumPadButton(numFrame, text="8", command=lambda: WritePin("8", inputPin)).grid(row=2,column=1, padx=2, pady=2)
    button9=NumPadButton(numFrame, text="9", command=lambda: WritePin("9", inputPin)).grid(row=2,column=2, padx=2, pady=2)
    button0=NumPadButton(numFrame, text="0", command=lambda: WritePin("0", inputPin)).grid(row=3,column=1, padx=2, pady=2)
    buttonP1=NumPadButton(numFrame, width=2).grid(row=3,column=0, padx=2, pady=2)
    buttonP2=NumPadButton(numFrame, width=2).grid(row=3,column=2, padx=2, pady=2)
    # Control Buttons On the Side.
    CancelButton = ControlButton(numFrame, hovercolor="#cc0066", bg="#f6006b", text="Cancel").grid(row=0,column=3, padx=(20,1), pady=1)
    ClearButton = ControlButton(numFrame, hovercolor="#cc9900", bg="#ffc300", text="Clear", command=lambda: ClearPin(inputPin)).grid(row=1,column=3, padx=(20,1), pady=1)
    EnterButton = ControlButton(numFrame, hovercolor="#009900", bg="#03d703", text="Enter").grid(row=2,column=3, padx=(20,1), pady=1)
    BlankButton = ControlButton(numFrame, hovercolor="#2d9de7", bg="#01b4f6", text="").grid(row=3,column=3, padx=(20,1), pady=1)
    return numFrame

def PinFrame(parent, inputPin):
    # Method Description
    """Create The Frame and Textbox to Hold the pin."""
    pinFrame = Frame(parent)
    pinFrame['bg'] = "#003366"
    pinEntry=Entry(pinFrame,text=inputPin, show="*", font=("Segoe UI", 15, "bold"), borderwidth=0, 
    bg="#003366", fg="#fafafa",justify=CENTER, validate="key")
    pinEntry['validatecommand'] = (pinEntry.register(ValidateKeys),'%P','%d','%s')
    pinEntry.pack(padx=20, pady=8,expand=1, fill=X)
    return pinFrame

def WritePin(text, entryText):
    # Method Description
    """Adds a number a Frame and populates it with Numbered Buttons"""
    if len(entryText.get()) < 4:
        entryText.set(entryText.get() + text)
    pass

def ClearPin(entryText):
    # Method Description
    """Clears the Pin Value written in the Button"""
    entryText.set("")
    pass

def ValidateKeys(P,d,s):
    # Method Description
    """"Limits the Input From Keyboard into Textbox"""
    #If the Keyboard is trying to insert value
    if P == '1': 
        # If the value enter is a value and the current value is not longer than 4 char.
        if not (d.isdigit() and len(s) < 4):
            return False
    return True


def NumPadWindow():
    # Main Function For calling and Testing this part of the ui
    # Very Subject To Change!!
    root=Tk()
    root.title('PyATM')
    root['bg'] = "#0c3b97"
    inputPin = StringVar()
    PinFrame(root, inputPin).grid(row=0, column=0, padx=30, pady=(20,0), sticky=N+S+E+W)
    NumPadFrame(root, inputPin).grid(row=1, column=0, padx=30, pady=20)
    root.mainloop()
    pass

NumPadWindow()