from tkinter import *

class ServicePage(Frame):
    # Class Description
    """Creates a Frame that holds the service options """
    def __init__(self, parent, *args, **kwargs):
        # Initalizes a frame with the give parameters of the constructor
        Frame.__init__(self, parent, bg=parent['bg'], *args, **kwargs)

        # Creates Few Properties to Manipulate the Interface
        self.Background = parent['bg']

        # Populates the Frame
        Label(self,text="Services Under CONSTRUCTION",font=("Calibri", 18, "bold"),fg="#f1f1f1",bg=self.Background).pack(pady=20)