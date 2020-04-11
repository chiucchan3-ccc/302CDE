from tkinter import *
from tkinter import filedialog as fd
import json
import os
from decimal import Decimal
import tkinter.messagebox
from datetime import date


def orderform():
    stock = ["Y","N"]
    delivery = ["Pick Up","Delivery"]
    scn1 = Toplevel(root)
    variable = StringVar(scn1)
    variable2 = StringVar(scn1)
    variable.set(stock[0])
    variable2.set(delivery[0])
    scn1.title("Order Detail")
    Label(scn1, text="Order Detail", font= 17).grid(row=0)
    Label(scn1, text="Order Number").grid(row=1)
    Onum = Entry(scn1,width=50)
    Onum.grid(row =1,column = 1)
    Label(scn1,text="Product Name").grid(row=2)
    Pname = Entry(scn1,width=50)
    Pname.grid(row=2,column=1)
    Label(scn1,text="Quantity").grid(row=3)
    Quan = Entry(scn1,width=50)
    Quan.grid(row=3,column=1)
    Label(scn1,text="Customer Name").grid(row=4)
    Cname = Entry(scn1,width=50)
    Cname.grid(row=4,column=1)
    Label(scn1,text="Stock(Y/N)").grid(row=5)
    Stock = OptionMenu(scn1,variable,*stock)
    Stock.grid(row=5,column=1)
    Label(scn1,text="Address").grid(row=6)
    Address = Entry(scn1,width=50)
    Address.grid(row=6,column=1)
    Label(scn1,text="Contact").grid(row=7)
    Contact = Entry(scn1,width=50)
    Contact.grid(row=7,column=1)
    Label(scn1,text="Delivery Method").grid(row=8)
    Delivery = OptionMenu(scn1,variable2,*delivery)
    Delivery.grid(row=8,column=1)
    Label(scn1,text="Price").grid(row=9)
    Price = Entry(scn1,width=50)
    Price.grid(row=9,column=1)


    def Createjson():
        filename = Onum.get() + ".json"
        obj = {
            "OrderNumber": Onum.get(),
            "ProductName" : Pname.get(),
            "Quantity" : Quan.get(),
            "CustomerName": Cname.get(),
            "Stock": variable.get(),
            "Address": Address.get(),
            "Contact": Contact.get(),
            "Delivery": variable2.get(),
            "Price": Price.get()
        }
        with open(filename, "w") as out_file:
            json.dump(obj, out_file)

        def Destroy():
            popup.destroy()
            scn1.destroy()

        popup = Tk()
        popup.wm_title("Success")
        Label(popup,text='The File has successfully change to Json').pack()
        Button(popup,text="Ok", command =Destroy).pack()




    Button(scn1, text="Exhcange to JSON",command=Createjson).grid(row=10, column=2)


def showjson():
    name = fd.askopenfilename(initialdir="E:/PycharmProjects", filetypes={("JSON", "*.json"), ("text file", "*.txt")})
    with open (name,"r") as reader:
        targetfile = json.loads(reader.read())
    sj = Toplevel(root)
    sj.title("Delivery Status")
    Label(sj, text="Delivery Status", font=20).grid(row=0)
    Label(sj, text="Delivery Type",font = 15).grid(row=1)
    Label(sj, text=targetfile["DeliveryType"],font = 15).grid(row=1, column=1)
    Label(sj, text="Delivery ID",font = 15).grid(row=2)
    Label(sj, text=targetfile["DeliveryID"], font = 15).grid(row=2, column=1)
    Label(sj, text="Last Update Date",font =15).grid(row=3)
    Label(sj, text=targetfile["LastUpdate"],font = 15).grid(row=3, column=1)
    Label(sj, text="Current Status",font = 15).grid(row=4)
    Label(sj, text=targetfile["CurrentStatus"],font = 15).grid(row=4, column=1)
    Label(sj, text="Weight",font = 15).grid(row=5)
    Label(sj, text=targetfile["Weight"],font = 15).grid(row=5, column=1)
    Label(sj, text="Rentention",font = 15).grid(row=6)
    Label(sj, text=targetfile["Rentention"],font = 15).grid(row=6, column=1)

    Button(sj,text="Back",command = sj.destroy).grid(row=7, column=2)


def deliverystatus():
    ds = Toplevel(root)
    ds.title("Check Delivery Status")
    Label(ds, text='Choose the Json file by the Delivery ID', font=15).grid(row=0, column=1)
    Button(ds, text='Open the File', command=showjson).grid(row=1, column=1, pady=15)
    Button(ds, text='Back to Menu', command=ds.destroy).grid(row=2, column=2)


def main():
    global root
    root = Tk()
    root.geometry('200x300+600+400')
    root.title("Amazon Post Office IOS")
    title = Label(root, text="Amazon Post Office IOS", font=18)
    title.grid(row=0, pady=15, sticky=S)
    order = Button(root, text="Send Order Detail", font=12, pady=15, command=orderform)
    order.grid(row=1, pady=15, sticky=S)
    receive = Button(root, text="Order Status", font=12, pady=15, command=deliverystatus)
    receive.grid(row=2, sticky=S, pady= 15)
    Button(root, text="Exit", font=12, command=root.quit).grid(columnspan=2, sticky=E)

    root.mainloop()
    ##start the GUI

main()
##call the screen function
