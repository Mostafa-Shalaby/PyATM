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

        # Deposit Values Properties (Entry Textboxes Values)
        self.DepositBill20=IntVar()
        self.DepositBill50=IntVar()
        self.DepositBill100=IntVar()
        self.DepositBill200=IntVar()
        self.DepositTotal=IntVar()

        # Loads In few Photos to use for the interface.
        self.Bill20 = PhotoImage(file=Path(__file__).parent / "Assets/Bill20.png")
        self.Bill50 = PhotoImage(file=Path(__file__).parent / "Assets/Bill50.png")
        self.Bill100 = PhotoImage(file=Path(__file__).parent / "Assets/Bill100.png")
        self.Bill200 = PhotoImage(file=Path(__file__).parent / "Assets/Bill200.png")
        self.SuccessOp = PhotoImage(file=Path(__file__).parent / "Assets/Message5.png")

        # Populates the Frame
        self.UserDescriptor().pack(side=LEFT,padx=(0,155),anchor=N)
        # Create a service variable to deal with it in other classes.
        self.Selector=self.ServiceSelector()
        self.Selector.pack(side=LEFT)

    def UserDescriptor(self):
        # Method Description:
        """Creates a Frame and populates it with Numbered Buttons"""
        # Create a Frame to hold controls.
        userFrame = Frame(self, bg=self.Background)
        # Welcome and UserName Labels
        TitleLabel(userFrame, text="Welcome,").pack(anchor=W)
        DetailsLabel(userFrame, text=self.SelectedCard.UserName).pack(anchor=W)
        # Account Type Labels.
        TitleLabel(userFrame, text="Account Type:").pack(anchor=W)
        DetailsLabel(userFrame, text=self.SelectedCard.accountType).pack(anchor=W)
        return userFrame

    def ServiceSelector(self):
        # Method Description:
        """Creates a Frame and populates it with Services Selection Buttons"""
        # Create a Frame to hold controls.
        selectorFrame = Frame(self, bg=self.Background)
        # Service Selector Title
        TitleLabel(selectorFrame, text="Available Services:").grid(row=0,column=0,padx=(0,10),pady=(5,10),sticky=W)
        # Service Selector Buttons for each service
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
        # Create a Frame to hold controls.
        self.CurrentService = withdrawFrame = Frame(self,bg=self.Background)
        # Withdraw Title
        TitleLabel(withdrawFrame,text=withdrawTitle).pack(anchor=W)
        # Option buttons to go back to service selector.
        self.SwitchService(withdrawFrame).pack(pady=(25,0))
        withdrawFrame.pack(side=LEFT)
    
    def DepositService(self):
        # Method Description
        """First Service Avaliable is (Checking Balance)"""
        # Puts a title for the deposit to be displayed as text by UI elements.
        depositTitle=self.SelectedCard.accountType+" Account's Deposit:"
        # Hides the Service Options Selector.
        self.Selector.pack_forget()
        # Create a Frame to hold controls.
        self.CurrentService = depositFrame = Frame(self,bg=self.Background)
        # Deposit Title and Instruction Labels
        TitleLabel(depositFrame,text=depositTitle).grid(row=0,column=0,columnspan=4,sticky=W)
        DetailsLabel(depositFrame,text="Please enter the amount you want to deposit:").grid(row=1,column=0,columnspan=4,sticky=W,pady=(0,5))
        # Setting Bill Amount Buttons
        self.BillFrame(depositFrame,self.DepositBill20,self.Bill20).grid(row=2,column=0,sticky=W,padx=(0,16))
        self.BillFrame(depositFrame,self.DepositBill50,self.Bill50).grid(row=2,column=1,sticky=W,padx=16)
        self.BillFrame(depositFrame,self.DepositBill100,self.Bill100).grid(row=2,column=2,sticky=W,padx=16)
        self.BillFrame(depositFrame,self.DepositBill200,self.Bill200).grid(row=2,column=3,sticky=W,padx=(16,0))
        # Total Deposit Amount Labels
        DetailsLabel(depositFrame,text="Total Deposit is:").grid(row=3,column=0,columnspan=4,sticky=W,pady=(5,0))
        Entry(depositFrame,text=self.DepositTotal,font=("Calibri",19),borderwidth=0,disabledbackground="#0c3b97",disabledforeground="#fafafa",justify=LEFT,state=DISABLED).grid(row=4,column=0,columnspan=4,sticky=W,pady=(0,5))
        # Accept and Cancel Buttons
        SwitchButton(depositFrame,bg="#00b300",hbg="#00cc00",abg="#008000",text="Deposit Cash",command=self.DepositCash).grid(row=5,column=0,columnspan=2,padx=(0,10))
        SwitchButton(depositFrame,bg="#e5ac00",hbg="#ffbf00",abg="#bf8f00",text="Cancel Service",command=self.BackToSelector).grid(row=5,column=2,columnspan=2,padx=(10,0))
        # Displays the entire Deposit Frame and Controls on the screen
        depositFrame.pack(side=LEFT)

    def BalanceService(self):
        # Method Description
        """First Service Avaliable is (Checking Balance)"""
        # Gets the current Balance from the Database.
        currentBalance, currency = DbModule.BalanceCheck(self.SelectedCard.ID, self.SelectedCard.accountType)       
        # Puts the Balance Value in a string to be displayed in Label.
        balanceString=str(currentBalance)+' '+currency
        # Puts a title for balance frame to be displayed in Label.
        balanceTitle=self.SelectedCard.accountType+" Account's Balance:"
        # Hides the Service Options Selector.
        self.Selector.pack_forget()
        # Create a Frame to hold controls
        self.CurrentService = balanceFrame = Frame(self,bg=self.Background)
        # Balance Title and Current Balance Labels
        TitleLabel(balanceFrame,text=balanceTitle).pack(anchor=W)
        Label(balanceFrame,text=balanceString,font=("Calibri",28),bg="#0c3b97",fg="#1a96dc").pack(anchor=W)
        # Option buttons to go back to service selector.
        self.SwitchService(balanceFrame).pack(pady=(25,0))
        # Displays the entire Balance Frame and Controls on the screen
        balanceFrame.pack(side=LEFT)

    def TransactionsService(self):
        # Method Description
        """First Service Avaliable is (Checking Balance)"""
        # Gets the transactions from the database
        transactions=DbModule.TransCheck(self.SelectedCard.ID, self.SelectedCard.accountType)
        # Puts a title for transactions frame to be displayed in Label.
        transTitle=self.SelectedCard.accountType+" Account's Transactions:"
        # Hides the Service Options Selector.
        self.Selector.pack_forget()
        # Create a Frame to hold controls
        self.CurrentService = transFrame = Frame(self,bg=self.Background)
        # Transactions Title Label and List of Transcations Labels.
        TitleLabel(transFrame,text=transTitle).pack(padx=(0,10),pady=(5,10),anchor=W)
        for x in transactions:
            transText="On "+str(x[3])+', '+str(x[0]).capitalize()+' '+str(x[1])+' '+str(x[2])
            Label(transFrame,text=transText,font=("Calibri",18),bg="#0c3b97",fg="#1a96dc").pack(anchor=W)
        # Option buttons to go back to service selector.
        self.SwitchService(transFrame).pack(pady=(25,0))
        # Displays the entire Transaction Frame and Controls on the screen
        transFrame.pack(side=LEFT)
    
    def SwitchService(self,parent):
        # Method Description:
        """Create a frame that holds two buttons to select another service or return card."""
        # Create a Frame to hold controls
        switchFrame = Frame(parent, bg=self.Background)
        # Creates SwitchButtons and connect them to other functions.
        SwitchButton(switchFrame,bg="#e5ac00",hbg="#ffbf00",abg="#bf8f00",text="Select Another Service",command=self.BackToSelector).grid(row=0,column=0,padx=(0,10))
        SwitchButton(switchFrame,bg="#cc0058",hbg="#eb0066",abg="#990042",text="Return Card",command=self.Parent.ReturnCard).grid(row=0,column=1,padx=(10,0))
        return switchFrame

    def SuccessFrame(self):
        # Close Current Deposit Service Frame
        self.CurrentService.destroy()
        # Create a Frame to hold controls
        self.CurrentService = successFrame = Frame(self, bg=self.Background)
        # Displays SuccessMessage Image
        Label(successFrame, image=self.SuccessOp, bg=self.Background).pack()
        # Option buttons to go back to service selector.
        self.SwitchService(successFrame).pack(pady=(25,0))
        # Displays the entire Success Frame and Controls on the screen
        successFrame.pack(side=LEFT)


    def BillFrame(self,parent,billValue,billImage):
        # Method Description:
        """Creates a Frame and Bill Image and Bill Amount Adjustment Buttons"""
        # Create a Frame to hold controls
        billFrame = Frame(parent, bg=self.Background)
        # The Bill Image
        Label(billFrame, image=billImage, bg=self.Background).grid(row=0,column=0,columnspan=3)
        # Increment and Decrement Buttons with a TextBox to display the billvalue
        DepositButton(billFrame,text="-",command=lambda: self.EditValue(billValue,False)).grid(row=1,column=0)
        Entry(billFrame,text=billValue,width="6",font=("Calibri",19),borderwidth=0,disabledbackground="#333",disabledforeground="#fafafa",justify=CENTER,state=DISABLED).grid(row=1,column=1,ipady=9)
        DepositButton(billFrame,text="+",command=lambda: self.EditValue(billValue,True)).grid(row=1,column=2)
        return billFrame

    def EditValue(self,billValue,isIncrement):
        # Gets the Total Number of  Bills Selected
        TotalBills=self.DepositBill20.get()+self.DepositBill50.get()+self.DepositBill100.get()+self.DepositBill200.get()
        # If the total is below 40, and an increment command is sent increase billvalue. (Updates Total too)
        if (isIncrement==True and TotalBills<40):
            billValue.set(billValue.get()+1)
            self.DepositTotal.set(self.DepositBill20.get()*20+self.DepositBill50.get()*50+self.DepositBill100.get()*100+self.DepositBill200.get()*200)
        # If the bill value is not 0, and an decrement command is sent decreases billvalue. (Updates Total too)
        elif(isIncrement==False and billValue.get()>0):
            billValue.set(billValue.get()-1)
            self.DepositTotal.set(self.DepositBill20.get()*20+self.DepositBill50.get()*50+self.DepositBill100.get()*100+self.DepositBill200.get()*200)

    def DepositCash(self):
        # Updates the balance value in the database.
        oldBalance, currency = DbModule.BalanceCheck(self.SelectedCard.ID, self.SelectedCard.accountType)
        DbModule.UpdateBalance((oldBalance + self.DepositTotal.get()), self.SelectedCard.ID, self.SelectedCard.accountType)
        # Record the transaction
        DbModule.RecordTrans(self.SelectedCard.ID, self.SelectedCard.accountType, 'deposit', self.DepositTotal.get())
        # Displays Operation Sucesseful Message.
        self.SuccessFrame()

    def BackToSelector(self):
        # Closes The Currently Open Service
        self.CurrentService.destroy()
        # Opens and Displays the Service Selector Frame.
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
        # Binds the hover over events to a set of functions
        self.bind("<Enter>", self.OnEnter)
        self.bind("<Leave>", self.OnLeave)
    # When Mouse is Over
    def OnEnter(self, e):
        self['bg'] = "#ffbf00"
    # When Mouse Leaves
    def OnLeave(self, e):
        self['bg'] = "#e5ac00"

class DepositButton(Button):
     # Class Description
    """Stylized Buttons For Use In ATM Service Selection Controls"""
    def __init__(self, parent, *args, **kwargs):
        # Initalizes A Button, and Hard Codes Few Styles.
        Button.__init__(self, parent, *args, **kwargs)
        self['width'] = 2
        self['border'] = 0
        self['font'] = ("Calibri", 19)
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