from tkinter import *
from pathlib import Path

class ThanksPage(Frame):
    # Class Description
    """Creates a Frame that Ask to Enter A Card / Select Preset One."""
    def __init__(self, parent, mode="normal", *arg, **kwargs):
        # Initalizes a frame with the give parameters of the constructor.
        Frame.__init__(self, parent, bg=parent['bg'], *arg, **kwargs)
        
        # Creates Few Properties to Manipulate the Interface.
        self.Parent = parent
        self.Background = parent['bg']
        self.Mode = mode
        self.Photo = ""

        # Populates the frame with an instruction Image.
        self.SelectMessage().pack()
        
    def SelectMessage(self):
        if self.Mode == "Invalid":
            self.Photo = PhotoImage(file=Path(__file__).parent / "Assets/Message3.png")
        else:
            self.Photo = PhotoImage(file=Path(__file__).parent / "Assets/Message2.png")
        Message = Label(self, image=self.Photo, bg=self.Background)
        return Message
