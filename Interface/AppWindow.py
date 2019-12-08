from tkinter import *
from pathlib import Path

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
    
    def CenterWindow(self):
        """Center the window on launch depending on the screen size."""
        x = (self.winfo_screenwidth()/2) - (self.width/2)
        y = (self.winfo_screenheight()/2) - (self.height/2) - 40
        self.geometry('+%d+%d' % (x, y))