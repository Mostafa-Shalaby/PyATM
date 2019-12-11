from tkinter import *
from pathlib import Path
from Modules import DbModule

class ServicePage(Frame):
    # Class Description
    """Creates a Frame that holds the service options """
    def __init__(self, parent, card, *args, **kwargs):
        # Initalizes a frame with the give parameters of the constructor
        Frame.__init__(self, parent, bg=parent['bg'], *args, **kwargs)

        # Creates Few Properties to Manipulate the Interface
        self.Background = parent['bg']
        self.SelectedCard = card
        self.Parent = parent

        # Populates the Frame
        self.UserDescriptor().pack(side=LEFT,padx=(0,155),anchor=N)
        # Create a service variable to deal with it in other classes.
        self.Selector=self.ServiceSelector()
        self.Selector.pack(side=LEFT)

    def UserDescriptor(self):
        # Method Description:
        """Creates a Frame and populates it with Numbered Buttons"""
        # Create a Frame to hold few Labels that provide basic information about the user.
        userFrame = Frame(self, bg=self.Background)
        TitleLabel(userFrame, text="Welcome,").pack(anchor=W)
        DetailsLabel(userFrame, text=self.SelectedCard.UserName).pack(anchor=W)
        TitleLabel(userFrame, text="Account Type:").pack(anchor=W)
        DetailsLabel(userFrame, text=self.SelectedCard.accountType).pack(anchor=W)
        return userFrame

    def ServiceSelector(self):
        # Method Description:
        """Creates a Frame and populates it with Services Selection Buttons"""
        # Create a Frame to a set of buttons that selects various ATM services.
        selectorFrame = Frame(self, bg=self.Background)
        TitleLabel(selectorFrame, text="Available Services:").grid(row=0,column=0,padx=(0,10),pady=(5,10),sticky=W)
        ServiceButton(selectorFrame,text="Withdraw",command=self.WithdrawService).grid(row=1,column=0,padx=(0,10),pady=(5,10))
        ServiceButton(selectorFrame,text="Deposit",command=self.DepositService).grid(row=1,column=1,padx=(10,0),pady=(5,10))
        ServiceButton(selectorFrame,text="Balance",command=self.BalanceService).grid(row=2,column=0,padx=(0,10),pady=(10,5))
        ServiceButton(selectorFrame,text="Transactions",command=self.TransactionsService).grid(row=2,column=1,padx=(10,0),pady=(10,5))
        QuickButton(selectorFrame,text="Quick Cash - 100 L.E.").grid(row=3,column=0,columnspan=2,pady=(25,0),sticky=EW)
        return selectorFrame

    def WithdrawService(self):
        # Method Description
        """First Service Avaliable is (Checking Balance)"""
        # Puts a title for the deposit to be displayed as text by UI elements.
        withdrawTitle=self.SelectedCard.accountType+" Account's Withdraw:"
        # Hids the Service Options Selector.
        self.Selector.pack_forget()

        # Create a Frame to hold a title.
        self.CurrentService = withdrawFrame = Frame(self,bg=self.Background)
        TitleLabel(withdrawFrame,text=withdrawTitle).pack(anchor=W)
        # Creates a button to go back to service selector.
        self.SwitchService(withdrawFrame).pack(pady=(25,0))
        withdrawFrame.pack(side=LEFT)
    
    def DepositService(self):
        # Method Description
        """First Service Avaliable is (Checking Balance)"""
        # Puts a title for the deposit to be displayed as text by UI elements.
        depositTitle=self.SelectedCard.accountType+" Account's Deposit:"
        # Hids the Service Options Selector.
        self.Selector.pack_forget()

        # Create a Frame to hold a title.
        self.CurrentService = depositFrame = Frame(self,bg=self.Background)
        TitleLabel(depositFrame,text=depositTitle).pack(anchor=W)
        # Creates a button to go back to service selector.
        self.SwitchService(depositFrame).pack(pady=(25,0))
        depositFrame.pack(side=LEFT)

    def BalanceService(self):
        # Method Description
        """First Service Avaliable is (Checking Balance)"""
        # Gets the current Balance from the Database.
        currentBalance, currency = DbModule.BalanceCheck(self.SelectedCard.ID, self.SelectedCard.accountType)       
        # Puts the Balance in a string and a title to be displayed as text by UI elements.
        balanceTitle=self.SelectedCard.accountType+" Account's Balance:"
        balanceString=str(currentBalance)+' '+currency

        # Hids the Service Options Selector.
        self.Selector.pack_forget()

        # Create a Frame to hold a title and a list of labels each holding a transcation info.
        self.CurrentService = balanceFrame = Frame(self,bg=self.Background)
        TitleLabel(balanceFrame,text=balanceTitle).pack(anchor=W)
        Label(balanceFrame,text=balanceString,font=("Calibri",28),bg="#0c3b97",fg="#1a96dc").pack(anchor=W)
        # Creates a button to go back to service selector.
        self.SwitchService(balanceFrame).pack(pady=(25,0))
        balanceFrame.pack(side=LEFT)

    def TransactionsService(self):
        # Method Description
        """First Service Avaliable is (Checking Balance)"""
        # Gets the transactions from the database
        transactions=DbModule.TransCheck(self.SelectedCard.ID, self.SelectedCard.accountType)
        transTitle=self.SelectedCard.accountType+" Account's Transactions:"
        # Hids the Service Options Selector.
        self.Selector.pack_forget()

        # Create a Frame to hold the balance and populates it with Two Labels.
        self.CurrentService = transFrame = Frame(self,bg=self.Background)
        TitleLabel(transFrame,text=transTitle).pack(padx=(0,10),pady=(5,10),anchor=W)
        for x in transactions:
            transText="On "+str(x[3])+', '+str(x[0]).capitalize()+' '+str(x[1])+' '+str(x[2])
            Label(transFrame,text=transText,font=("Calibri",18),bg="#0c3b97",fg="#1a96dc").pack(anchor=W)
        # Creates a button to go back to service selector.
        self.SwitchService(transFrame).pack(pady=(25,0))
        transFrame.pack(side=LEFT)
    
    def SwitchService(self,parent):
        # Method Description:
        """Creates a Frame and populates it with Services Selection Buttons"""
        # Create a Frame that holds two buttons to select another service or return card.
        switchFrame = Frame(parent, bg=self.Background)
        SwitchButton(switchFrame,bg="#e5ac00",hbg="#ffbf00",abg="#bf8f00",text="Select Another Service",command=self.BackToSelector).grid(row=0,column=0,padx=(0,10))
        SwitchButton(switchFrame,bg="#cc0058",hbg="#eb0066",abg="#990042",text="Return Card",command=self.Parent.ReturnCard).grid(row=0,column=1,padx=(10,0))
        return switchFrame

    def BackToSelector(self):
        self.CurrentService.pack_forget()
        self.Selector.pack(side=LEFT)


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
        # Binds the hover over events to a set of functions
        self.bind("<Enter>", self.OnEnter)
        self.bind("<Leave>", self.OnLeave)
    # When Mouse is Over
    def OnEnter(self, e):
        self['bg'] = "#0095ff"
    # When Mouse Leaves
    def OnLeave(self, e):
        self['bg'] = "#0077cc"

class SwitchButton(Button):
     # Class Description
    """Stylized Buttons For Use In ATM Service Selection Controls"""
    def __init__(self, parent, hbg, abg, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Button.__init__(self, parent, *args, **kwargs)
        self['width'] = 26
        self['height'] = 1
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
        self['bg'] = "#0c3b97"
        self['fg'] = "#f1f1f1"
    
class DetailsLabel(Label):
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Label.__init__(self, parent, *args, **kwargs)
        self['font'] = ("Calibri", 18)
        self['bg'] = "#0c3b97"
        self['fg'] = "#1a96dc"