from tkinter import *


class MortgageCalculator:
    
    def __init__(self):
        root = Tk()
        root.title("MortgageCalculator")
        root.geometry("400x200")

        #Input label and Entry boxes
        Label(root,justify=RIGHT,text="Principal").grid(row=1,column=1,sticky=W)
        self.principal = StringVar()
        Entry(root,justify=LEFT, textvariable=self.principal).grid(row=1,column=2,sticky=W)

        Label(root,justify=RIGHT,text="Annual Interest Rate").grid(row=2,column=1,sticky=W)
        self.annualinterestrate = StringVar()
        Entry(root,justify=LEFT,textvariable=self.annualinterestrate).grid(row=2,column=2,sticky=W)

        Label(root,justify=RIGHT,text="Years").grid(row=3,column=1,sticky=W)
        self.years = StringVar()
        Entry(root,justify=LEFT,textvariable=self.years).grid(row=3,column=2,sticky=W)

        #calculate monthly payment
        self.monthly_paymentvar = StringVar()
        Label(root,justify=RIGHT,text="Monthly Payment").grid(row=4,column=1,sticky=W)
        lblmontlypayment = Label(root, textvariable=self.monthly_paymentvar).grid(row=4, column=2,sticky=E)
        
        #create montlypayment button
        Button(root,justify=RIGHT,text="Submit", command = self.monthly_payment).grid(row=4,column=3,sticky=W)

        #calculate total payment
        self.totalpaymentvar = StringVar()
        Label(root,justify=RIGHT,text="Total Payment").grid(row=5,column=1,sticky=W)
        lbltotalpayment = Label(root, textvariable=self.totalpaymentvar).grid(row=5,column=2,sticky=E)
        
        #create totalpayment button
        Button(root,justify=RIGHT, text="Calculate", command = self.total_payment).grid(row=5,column=3,sticky=W)

        root.mainloop()
        
    
    def monthly_payment(self):
        self.p = int(self.principal.get())
        self.i = float(self.annualinterestrate.get()) / 100 / 12
        self.t = int(self.years.get()) * 12
        self.monthly_payment = self.p * ( self.i * (1 + self.i) ** self.t) /((1+ self.i) ** self.t - 1)
        self.monthly_paymentvar.set(format(self.monthly_payment,'10.2f'))
        return self.monthly_payment
    
    def total_payment(self):
        self.total_payment = float(self.monthly_payment) * 12 * 25
        self.totalpaymentvar.set(format(self.total_payment,'10.2f'))
        return self.total_payment
    
    #def __repr__(self):
        #return(f"Principal={self.p}, Interest={self.i}, No of Years = {self.t}, montlypayment = {self.monthly_payment}")

c = MortgageCalculator()
