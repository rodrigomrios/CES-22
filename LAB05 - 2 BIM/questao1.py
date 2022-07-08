import abc
import tkinter as ttk
from tkinter import *

class Bank:

    def __init__(self, amount):

        self.amount = amount
        self.bankextract = []

    def gaincash(self, newamount, gain):

        self.amount = newamount

        self.bankextract.append(f"Deposit value: {gain}, Final Amount: {self.amount}")

        print(f"Deposite Operation Concluded. US {gain} was added to your acount. Your Amount is US {self.amount}.\n")

    def withdrawcash(self, newamount, withdraw):

        self.amount = newamount

        self.bankextract.append(f"Withdraw value: {withdraw}, Final Amount: {self.amount}")

        print(f"Withdraw Operation Concluded. US {withdraw} was subtracted from your acount. Your Amount is US {self.amount}.\n")

    def transfer(self, newamount, transfervalue, recipient):

        self.amount = newamount

        self.bankextract.append(f"Transfer value: {transfervalue} to {recipient}, Final Amount: {self.amount}")

        print(f"Transfer Operation Concluded. US {transfervalue} was subtracted from your acount. Your Amount is US {self.amount}.\n")

    def doextract(self):

        print("Here is your extract including all operations you have already made.\n")

        for element in self.bankextract:

            print(element)
            print("\n")

        print(f"Your Final amount is {self.amount}\n")


class Operation(abc.ABC):

    def __init__(self, bank):

        self.bank = bank
        self.amount = bank.amount

    def execution(self):
        
        pass

class GainOperation(Operation):

    def __init__(self, bank, gain):

        super().__init__(bank)

        self.gain = gain

    def execution(self):

        self.bank.gaincash(self.amount + self.gain, self.gain)

class WithdrawOperation(Operation):

    def __init__(self, bank, withdraw):

        super().__init__(bank)

        self.withdraw = withdraw

    def execution(self):

        self.bank.withdrawcash(self.amount - self.withdraw, self.withdraw)

class TransferOperation(Operation):

    def __init__(self, bank, transfervalue, recipient):

        super().__init__(bank)

        self.transfervalue = transfervalue

        self.recipient = recipient

    def execution(self):

        self.bank.transfer(self.amount - self.transfervalue, self.transfervalue, self.recipient)

class ExtractOperation(Operation):

    def __init__(self, bank):

        super().__init__(bank)


    def execution(self):

        self.bank.doextract()

class Invoker:

    def operation(self, oprt):

        self.oprt = oprt

    def activateop(self):

        self.oprt.execution()


bank = Bank(0)

invoker = Invoker()

class App(ttk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.master = master

        self.interface()

    def interface(self):

        self.windowstyle = ttk.Label(self.master, text="Bank App", font="Raleway", height=2, width=50)
        self.windowstyle.grid(column=0, row=0)

        self.addgain = ttk.Button(self.master, text="Deposit", command=self.addgainop, height=2)
        self.addgain.grid(column=0, row=1)

        self.wdmoney = ttk.Button(self.master, text="Withdraw", command=self.wdmoneyop, height=2)
        self.wdmoney.grid(column=0, row=2)

        self.transfermoney = ttk.Button(self.master, text="Transfer", command=self.transfermoneyop, height=2)
        self.transfermoney.grid(column=0, row=3)

        self.showextract = ttk.Button(self.master, text="Extract", command=self.showextractop, height=2)
        self.showextract.grid(column=0, row=4)

        self.windowstyle = ttk.Label(self.master, text="Value to be operated:", font="Raleway", height=1, width=25)
        self.windowstyle.grid(column=0, row=5)

        self.readuser = ttk.Entry(self.master)
        self.readuser.grid(column=0, row=6)

        self.windowstyle = ttk.Label(self.master, text="Name to transfer to:", font="Raleway", height=1, width=25)
        self.windowstyle.grid(column=0, row=7)

        self.readtransfer = ttk.Entry(self.master)
        self.readtransfer.grid(column=0, row=8)
    
    def addgainop(self):

        valuetop0 = self.readuser.get()

        op0 = GainOperation(bank, int(valuetop0))

        invoker.operation(op0)
        invoker.activateop()

    def wdmoneyop(self):

        valuedown0 = self.readuser.get()

        op1 = WithdrawOperation(bank, int(valuedown0))

        invoker.operation(op1)
        invoker.activateop()

    def transfermoneyop(self):

        valuedown1 = self.readuser.get()
        person0 = self.readtransfer.get()

        op2 = TransferOperation(bank, int(valuedown1), str(person0))

        invoker.operation(op2)
        invoker.activateop()

    def showextractop(self):

        op3 = ExtractOperation(bank)

        invoker.operation(op3)
        invoker.activateop()

root = ttk.Tk()
root.geometry("550x350")
app = App(root)
app.master.title("Bank App")
app.mainloop()