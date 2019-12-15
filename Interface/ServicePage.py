from tkinter import *
from pathlib import Path
from Modules import CalculationModule, DbModule
from Interface.AppStyles import *
from Interface.PinPage import PinPage

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

        # Bills in the Machine
        self.Bills = {20: 800, 50: 320, 100: 160, 200: 80}

        # Withdraw Values Properties (Entry Textboxes Values)
        self.WithdrawLimit=self.CalculateLimit()
        self.WithdrawAmount=StringVar()
        
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
        self.Error1OP = PhotoImage(file=Path(__file__).parent / "Assets/Message6.png")
        self.Error2OP = PhotoImage(file=Path(__file__).parent / "Assets/Message7.png")

        # Populates the Frame
        self.UserDescriptor().pack(side=LEFT,padx=(0,155),anchor=N)
        # Create a service variable to deal with it in other classes.
        self.Selector=self.ServiceSelector()
        self.Selector.pack(side=LEFT)

    def UserDescriptor(self):
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
        # Quick Cash Button
        WithdrawButton(selectorFrame,mode="menu",text="Quick Cash - 100 L.E.",command=lambda: self.WithdrawCash(100,selectorFrame)).grid(row=3,column=0,columnspan=2,pady=(25,0),sticky=EW)
        return selectorFrame

    def WithdrawService(self):
        """First Service Avaliable is (Checking Balance)"""
        # Puts a title for the withdraw to be displayed as text by UI elements.
        withdrawTitle=self.SelectedCard.accountType+" Account's Withdraw:"
        # Hids the Service Options Selector.
        self.Selector.pack_forget()
        # Create a Frame to hold controls.
        self.CurrentService = withdrawFrame = Frame(self,bg=self.Background)
        # Withdraw Title
        TitleLabel(withdrawFrame,text=withdrawTitle).grid(row=0,column=0,columnspan=6,sticky=W)
        # PreDefined Withdraw Amounts Buttons
        SubtitleLabel(withdrawFrame,text="Quick Withdraw Options:").grid(row=1,column=0,columnspan=6,sticky=W,pady=8)
        WithdrawButton(withdrawFrame,text="100",command=lambda: self.WithdrawCash(100,self.CurrentService)).grid(row=2,column=0)
        WithdrawButton(withdrawFrame,text="200",command=lambda: self.WithdrawCash(200,self.CurrentService)).grid(row=2,column=1)
        WithdrawButton(withdrawFrame,text="300",command=lambda: self.WithdrawCash(300,self.CurrentService)).grid(row=2,column=2)
        WithdrawButton(withdrawFrame,text="500",command=lambda: self.WithdrawCash(500,self.CurrentService)).grid(row=2,column=3)
        WithdrawButton(withdrawFrame,text="1000",command=lambda: self.WithdrawCash(1000,self.CurrentService)).grid(row=2,column=4)
        WithdrawButton(withdrawFrame,text="2000",command=lambda: self.WithdrawCash(2000,self.CurrentService)).grid(row=2,column=5)
        # Custom Amount Withdraw
        SubtitleLabel(withdrawFrame,text="Custom Withdraw Options:").grid(row=3,column=0,columnspan=6,sticky=W,pady=8)
        self.WithdrawPad(withdrawFrame).grid(row=4,column=0,columnspan=6,pady=(0,8),sticky=W)
        # Accept and Cancel Buttons
        SwitchButton(withdrawFrame,bg="#00b300",hbg="#00cc00",abg="#008000",text="Withdraw Custom Amount",command=lambda:self.WithdrawCash(self.WithdrawAmount.get(),self.CurrentService)).grid(row=5,column=0,columnspan=3,padx=(0,10))
        SwitchButton(withdrawFrame,bg="#e5ac00",hbg="#ffbf00",abg="#bf8f00",text="Cancel Service",command=self.BackToSelector).grid(row=5,column=3,columnspan=3,padx=(10,0))
        # Displays the entire Deposit Frame and Controls on the screen
        withdrawFrame.pack(side=LEFT)
    
    def DepositService(self):
        """First Service Avaliable is (Checking Balance)"""
        # Puts a title for the deposit to be displayed as text by UI elements.
        depositTitle=self.SelectedCard.accountType+" Account's Deposit:"
        # Hides the Service Options Selector.
        self.Selector.pack_forget()
        # Create a Frame to hold controls.
        self.CurrentService = depositFrame = Frame(self,bg=self.Background)
        # Deposit Title and Instruction Labels
        TitleLabel(depositFrame,text=depositTitle).grid(row=0,column=0,columnspan=4,sticky=W)
        SubtitleLabel(depositFrame,text="Please enter the amount you want to deposit:").grid(row=1,column=0,columnspan=4,sticky=W,pady=5)
        # Setting Bill Amount Buttons
        self.DepositBillFrame(depositFrame,self.DepositBill20,self.Bill20).grid(row=2,column=0,sticky=W,padx=(0,16))
        self.DepositBillFrame(depositFrame,self.DepositBill50,self.Bill50).grid(row=2,column=1,sticky=W,padx=16)
        self.DepositBillFrame(depositFrame,self.DepositBill100,self.Bill100).grid(row=2,column=2,sticky=W,padx=16)
        self.DepositBillFrame(depositFrame,self.DepositBill200,self.Bill200).grid(row=2,column=3,sticky=W,padx=(16,0))
        # Total Deposit Amount Labels
        SubtitleLabel(depositFrame,text="Total Deposit is:").grid(row=3,column=0,columnspan=4,sticky=W,pady=(10))
        Entry(depositFrame,text=self.DepositTotal,font=("Calibri",19),borderwidth=0,disabledbackground="#0c3b97",disabledforeground="#1a96dc",justify=LEFT,state=DISABLED).grid(row=4,column=0,columnspan=4,sticky=W,pady=(0,10))
        # Accept and Cancel Buttons
        SwitchButton(depositFrame,bg="#00b300",hbg="#00cc00",abg="#008000",text="Deposit Cash",command=self.DepositCash).grid(row=5,column=0,columnspan=2,padx=(0,10))
        SwitchButton(depositFrame,bg="#e5ac00",hbg="#ffbf00",abg="#bf8f00",text="Cancel Service",command=self.BackToSelector).grid(row=5,column=2,columnspan=2,padx=(10,0))
        # Displays the entire Deposit Frame and Controls on the screen
        depositFrame.pack(side=LEFT)

    def BalanceService(self):
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
            DetailsLabel(transFrame,text=transText).pack(anchor=W)
        # Option buttons to go back to service selector.
        self.SwitchService(transFrame).pack(pady=(25,0))
        # Displays the entire Transaction Frame and Controls on the screen
        transFrame.pack(side=LEFT)
    
    def SwitchService(self,parent):
        """Create a frame that holds two buttons to select another service or return card."""
        # Create a Frame to hold controls
        switchFrame = Frame(parent, bg=self.Background)
        # Creates SwitchButtons and connect them to other functions.
        SwitchButton(switchFrame,bg="#e5ac00",hbg="#ffbf00",abg="#bf8f00",text="Select Another Service",command=self.BackToSelector).grid(row=0,column=0,padx=(0,10))
        SwitchButton(switchFrame,bg="#cc0058",hbg="#eb0066",abg="#990042",text="Return Card",command=self.Parent.ReturnCard).grid(row=0,column=1,padx=(10,0))
        return switchFrame

    def WithdrawPad(self,parent):
        """Creates a Frame and NumPad to Enter Custom Withdraw Amounts"""
        # Create a Frame to hold controls
        padFrame = Frame(parent, bg=self.Background)
        # Puts the limit in a string to be displayed as text by UI elements.
        accountLimit = "Limit: "+str(self.WithdrawLimit)+" Max"
        # Subtitle Label Withdraw Amount:
        DetailsLabel(padFrame,text="Please Enter Desired Amount:").grid(row=0,column=0,padx=(0,65),sticky=W)
        # The Textbox holding the custom amount of withdraw cash:
        withdrawEntry=Entry(padFrame,text=self.WithdrawAmount,width="6",font=("Segoe UI", 15, "bold"),borderwidth=0,bg="#333",fg="#fafafa",justify=CENTER,validate="key")
        withdrawEntry['validatecommand'] = (withdrawEntry.register(self.WithdrawKeyChecker),'%P','%d','%s')
        withdrawEntry.grid(row=1,column=0,sticky=NSEW,ipady=5,padx=(0,35))
        # The Limit value for withdraw.
        DetailsLabel(padFrame,text=accountLimit).grid(row=2,column=0,sticky=W)
        # The Input Numpad
        WithdrawPadButton(padFrame,text="1",command=lambda: self.WriteWithdraw("1")).grid(row=0,column=1,padx=2,pady=2)
        WithdrawPadButton(padFrame,text="2",command=lambda: self.WriteWithdraw("2")).grid(row=0,column=2,padx=2,pady=2)
        WithdrawPadButton(padFrame,text="3",command=lambda: self.WriteWithdraw("3")).grid(row=0,column=3,padx=2,pady=2)
        WithdrawPadButton(padFrame,text="4",command=lambda: self.WriteWithdraw("4")).grid(row=1,column=1,padx=2,pady=2)
        WithdrawPadButton(padFrame,text="5",command=lambda: self.WriteWithdraw("5")).grid(row=1,column=2,padx=2,pady=2)
        WithdrawPadButton(padFrame,text="6",command=lambda: self.WriteWithdraw("6")).grid(row=1,column=3,padx=2,pady=2)
        WithdrawPadButton(padFrame,text="7",command=lambda: self.WriteWithdraw("7")).grid(row=2,column=1,padx=2,pady=2)
        WithdrawPadButton(padFrame,text="8",command=lambda: self.WriteWithdraw("8")).grid(row=2,column=2,padx=2,pady=2)
        WithdrawPadButton(padFrame,text="9",command=lambda: self.WriteWithdraw("9")).grid(row=2,column=3,padx=2,pady=2)
        WithdrawPadButton(padFrame,text="0",command=lambda: self.WriteWithdraw("0")).grid(row=3,column=1,columnspan=2,padx=2,pady=2,sticky=EW)
        WithdrawPadButton(padFrame,text="C",command=lambda: self.ClearWithdraw()).grid(row=3,column=3,padx=2,pady=2)
        # Returns the complete frame to another control
        return padFrame

    def WithdrawBillFrame(self,parent,billValue,billImage):
        """Creates a Frame and Bill Image and Bill Amount Adjustment Buttons"""
        # Create a Frame to hold controls
        billFrame = Frame(parent, bg=self.Background)
        # Increment and Decrement Buttons with a TextBox to display the billvalue
        TitleLabel(billFrame,text=str(billValue)+" x").pack()
        # The Bill Image
        Label(billFrame, image=billImage, bg=self.Background).pack()
        return billFrame
    
    def DepositBillFrame(self,parent,billValue,billImage):
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
        """Updates the Deposit Values"""
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

    def WithdrawCash(self,amount,CallerFrame):
        """Withdraws money from the database and updates the GUI"""
        # Sets amount given to an int value
        amount=int(amount)
        # Check if the client has enough amount in balance
        oldBalance, currency = DbModule.BalanceCheck(self.SelectedCard.ID, self.SelectedCard.accountType)
        # Create a Frame to hold controls
        self.CurrentService = statusFrame = Frame(self, bg=self.Background)
        # Close Current Service Frame (if any are opened) and selector menu (if is opened)
        CallerFrame.pack_forget()
        # If the amount > oldBalance enter a loop until a valid amount is entered
        if amount > oldBalance or amount < 0:
            Label(statusFrame, image=self.Error1OP, bg=self.Background).pack(padx=123)
            statusFrame.pack(side=LEFT)
            statusFrame.after(2000,statusFrame.destroy)
            CallerFrame.after(2000,CallerFrame.pack)
            return
        # Updates the machine bills, and gives back the list of bills to be dispensed.        
        self.Bills, amount_bills = CalculationModule.GetBills(self.Bills, amount)
        if not amount_bills:
            Label(statusFrame, image=self.Error2OP, bg=self.Background).pack(padx=104)
            statusFrame.pack(side=LEFT)
            statusFrame.after(2000,statusFrame.destroy)
            CallerFrame.after(2000,CallerFrame.pack)
            return
        # Deduct the amount from the balance in the database
        DbModule.UpdateBalance((oldBalance - amount), self.SelectedCard.ID, self.SelectedCard.accountType)
        # Record the transaction
        DbModule.RecordTrans(self.SelectedCard.ID, self.SelectedCard.accountType, 'withdraw', amount)
        # Resets Withdraw Amount
        self.ClearWithdraw()
        # Sets statusFrame as CurrentService
        self.CurrentService = statusFrame = Frame(self, bg=self.Background)
        # Title Label for cashFrame
        TitleLabel(statusFrame,text="Money Dispensed, Please count your bills!").pack(pady=(0,10))
        # Eject cash as in a cashFrame
        cashFrame = Frame(statusFrame, bg=self.Background)
        # For loop on the output to determine what bills to display
        for bill, billCount in amount_bills.items():
            if bill == 20 and billCount != 0:
                self.WithdrawBillFrame(cashFrame,billCount,self.Bill20).grid(row=1,column=0,sticky=W,padx=16)
            elif bill == 50 and billCount != 0:
                self.WithdrawBillFrame(cashFrame,billCount,self.Bill50).grid(row=1,column=1,sticky=W,padx=16)
            elif bill == 100 and billCount != 0:
                self.WithdrawBillFrame(cashFrame,billCount,self.Bill100).grid(row=1,column=2,sticky=W,padx=16)
            elif bill == 200 and billCount != 0:
                self.WithdrawBillFrame(cashFrame,billCount,self.Bill200).grid(row=1,column=3,sticky=W,padx=16)
        # adds the complete cashFrame into the statusFrame
        cashFrame.pack()
        # Thanks Label for Withdraw
        TitleLabel(statusFrame,text="Thanks for Using PyATM!").pack(pady=10)
        # Option buttons to go back to service selector.
        self.SwitchService(statusFrame).pack(pady=(25,0))
        # Displays the entire statusFrame with the dispensed cash on it.
        statusFrame.pack(side=LEFT)

    def DepositCash(self):
        """Deposits money into the User's Account and updates GUI"""
        if self.self.DepositTotal.get() != 0:
            # Updates the balance value in the database.
            oldBalance, currency = DbModule.BalanceCheck(self.SelectedCard.ID, self.SelectedCard.accountType)
            DbModule.UpdateBalance((oldBalance + self.DepositTotal.get()), self.SelectedCard.ID, self.SelectedCard.accountType)
            # Record the transaction
            DbModule.RecordTrans(self.SelectedCard.ID, self.SelectedCard.accountType, 'deposit', self.DepositTotal.get())
            # Close Current Deposit Service Frame
            self.CurrentService.destroy()
            # Create a Frame to hold controls
            self.CurrentService = messageFrame = Frame(self, bg=self.Background)
            # Adds Success Message Image to the .
            Label(messageFrame, image=self.SuccessOp, bg=self.Background).pack()
            # Option buttons to go back to service selector.
            self.SwitchService(messageFrame).pack(pady=(25,0))
            # Displays the entire Success Frame and Controls on the screen
            messageFrame.pack(side=LEFT)

    def BackToSelector(self):
        """Sends back the Selector frame in GUI"""
        # Closes The Currently Open Service
        self.CurrentService.destroy()
        # Opens and Displays the Service Selector Frame.
        self.Selector.pack(side=LEFT)

    def WriteWithdraw(self, text):
        """Types In the Number of the Button Being Clicked. (Not Exceeding 4 Digits or Withdraw Limit)"""
        CurrentValue = self.WithdrawAmount.get()
        # If the value is less than the limit and smalleer than 4 digits
        if len(CurrentValue) < 4 and int(CurrentValue+text)<=self.WithdrawLimit:
            self.WithdrawAmount.set(CurrentValue+text)
    
    def ClearWithdraw(self):
        """Clears the Withdraw Written in the Textbox"""
        self.WithdrawAmount.set("")

    def WithdrawKeyChecker(self,P,d,s):
        """"Limits the Input From Keyboard into Textbox"""
        #If the Keyboard is trying to insert value
        if d == '1': 
            # If the value enter is a value and the current value is not longer than 4 char.
            if not (P.isdigit() and len(s) < 4 and int(P)<=self.WithdrawLimit):
                return False
        return True

    def CalculateLimit(self):
        """Calculates the Limit Depending on the Card Entered"""
        if self.SelectedCard.BankName != "NBE":
            return 2000
        elif self.SelectedCard.accountType == "Saving":
            return 6000
        else:
            return 8000
