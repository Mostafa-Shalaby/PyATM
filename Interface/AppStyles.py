from tkinter import *
from pathlib import Path

# Hardcoded Stylized Widgets: (Subclass of Existing Widgets)
class TitleLabel(Label):
    """Stylized Custom Label For a Service's Titles"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes a Label, and Hard Codes Few Styles.
        Label.__init__(self, parent, *args, **kwargs)
        self['font'] = ("Calibri", 24, "bold")
        self['bg'] = "#0c3b97"
        self['fg'] = "#f1f1f1"
    
class DetailsLabel(Label):
    """Stylized Custom Label For A Service's Details/Sub Titles"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes a Label, and Hard Codes Few Styles.
        Label.__init__(self, parent, *args, **kwargs)
        self['font'] = ("Calibri", 18)
        self['bg'] = "#0c3b97"
        self['fg'] = "#1a96dc"

class CustomButton(Button):
    """Stylized Custom Button For Various Parts of the GUI"""
    def __init__(self, parent, hbg, abg, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Button.__init__(self, parent, *args, **kwargs)
        self['border'] = 0
        self['font'] = ("Calibri", 19, "bold")
        self['fg']="#f1f1f1"
        self['activebackground'] = abg
        self['activeforeground'] = "#afafaf"
        self.Background = self['bg']
        self.HoverColor = hbg
        # Binds the hover over events to a set of functions
        self.bind("<Enter>", self.OnEnter)
        self.bind("<Leave>", self.OnLeave)
    # When Mouse is Over
    def OnEnter(self, e):
        self['bg'] = self.HoverColor
    # When Mouse Leaves
    def OnLeave(self, e):
        self['bg'] = self.Background

class ReturnCardButton(CustomButton):
    """Stylized Custom Button For Use as a Force Return Card Control"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes a Custom Button, and Hard Codes Few Styles.
        CustomButton.__init__(self, parent,bg="#0c3b97", hbg="#0066ae", abg="#004373", *args, **kwargs)
        self.photo = PhotoImage(file=Path(__file__).parent / "Assets/CustomButton2.png")    
        self.config(image=self.photo, compound=LEFT)

class CardButton(CustomButton):
    """Stylized Custom Button For Card Selection Controls"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        CustomButton.__init__(self, parent,bg="#0066ae", hbg="#0077cc", abg="#004373", *args, **kwargs)
        self['width'] = 144
        self['padx'] = 3
        self['pady'] = 8
        self['font'] = ("Calibri", 17, "bold")
        self.photo = PhotoImage(file=Path(__file__).parent / "Assets/CustomButton1.png")  
        self.config(image=self.photo, compound=LEFT)

class PinPadButton(CustomButton):
    """Stylized Custom Button For Entering Pin Values"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        CustomButton.__init__(self, parent,bg="#0077cc", hbg="#0095ff", abg="#2257bf", *args, **kwargs)
        self['width'] = 3
        self['padx'] = 21
        self['pady'] = 10

class PinControlButton(CustomButton):
    """Stylized Custom Button For Controling Pin Value"""
    def __init__(self, parent, hbg, abg, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        CustomButton.__init__(self, parent, hbg, abg, *args, **kwargs)
        self['width'] = 3
        self['padx'] = 21
        self['pady'] = 10

class ServiceButton(CustomButton):
    """Stylized Custom Button For Service Selection Frame"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes a Custom Button, and Hard Codes Few Styles.
        CustomButton.__init__(self, parent,bg="#0077cc", hbg="#0095ff", abg="#2257bf", *args, **kwargs)
        self['width'] = 26
        self['height'] = 2

class SwitchButton(CustomButton):
    """Stylized Custom Button For Switching Back from Services."""
    def __init__(self, parent, hbg, abg, *args, **kwargs):
        # Initalizes a Custom Button, and Hard Codes Few Styles.
        CustomButton.__init__(self, parent, hbg, abg, *args, **kwargs)
        self['width'] = 26
        self['height'] = 1

class WithdrawButton(CustomButton):
    """Stylized Custom Button For Withdraw Service."""
    def __init__(self, parent, mode="mini", *args, **kwargs):
        # Initalizes a Custom Button, and Hard Codes Few Styles.
        if mode == "menu":
            CustomButton.__init__(self, parent, bg="#e5ac00", hbg="#ffbf00", abg="#bf8f00", *args, **kwargs)
            self['height'] = 1
        else :
            CustomButton.__init__(self, parent,bg="#0077cc", hbg="#0095ff", abg="#2257bf", *args, **kwargs)
            self['width'] = 8
            self['height'] = 1

class DepositButton(CustomButton):
    """Stylized Custom Button For Deposit Service."""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes a Custom Button, and Hard Codes Few Styles.
        CustomButton.__init__(self, parent,bg="#0077cc", hbg="#0095ff", abg="#2257bf", *args, **kwargs)
        self['width'] = 2


# class NumPadButton(CustomButton):
#     def __init__(self, parent, *args, **kwargs):
#         # Initalizes a Custom Button, and Hard Codes Few Styles.
#         CustomButton.__init__(self, parent,bg="#0077cc", hbg="#0095ff", abg="#2257bf", *args, **kwargs)
#         self['width'] = 4
#         self['height'] = 1