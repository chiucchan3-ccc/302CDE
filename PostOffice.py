from tkinter import *
from tkinter import filedialog as fd
import json
import os
from decimal import Decimal
import tkinter.messagebox
from datetime import date


def deliveryform():
    df = Toplevel(root)
    Dstatus = ["Not Finished", "Finished Delivery"]
    delivery = ["Pick Up", "Delivery"]
    statuslist = ["Collection", "Arrival inward office", "Departure Office", "Delivery", "Retention", "FinalDelivery"]
    ##Create OptionMenu List
    currenydate = str(date.today())##get curreny date
    renten = BooleanVar()

    Detype = StringVar(df)
    statlist = StringVar(df)
    Dstat = StringVar(df)
    ##Create Set for Option Menu
    Detype.set(delivery[0])
    statlist.set(statuslist[0])
    Dstat.set(Dstatus[0])
    ##Form Design
    df.title("Delivery Detail")
    Label(df, text="Delivery Detail", font= 17).grid(row=0)
    Label(df, text="Delivery Number").grid(row=1)
    dtype = OptionMenu(df, Detype, *delivery)
    dtype.grid(row =1, column=1)
    Label(df, text="Delivery Number").grid(row=2)
    dnum = Entry(df, width=20)
    dnum.grid(row=2, column=1)
    Label(df, text="Status").grid(row=3)
    Dstat = OptionMenu(df,Dstat,*Dstatus)
    Dstat.grid(row=3,column=1)
    Label(df, text="Last Update Date").grid(row=4)
    Date = Entry(df, width=20)
    Date.insert(END,string = currenydate)
    Date.grid(row=4,column=1)
    Label(df,text="Current Status").grid(row=5)
    Stat = OptionMenu(df,statlist,*statuslist)
    Stat.grid(row=5,column=1)
    Label(df,text="Weight").grid(row=6)
    weight = Entry(df,width =20)
    weight.grid(row=6,column=1)
    Label(df,text="Rentiontion").grid(row=7)
    rent = Checkbutton(df,variable = renten , onvalue = True, offvalue = False)
    rent.grid(row=7,column=1)


    def Createjson():
        filename = dnum.get() + ".json"

        obj = {
            "DeliveryType": Detype.get(),
            "DeliveryID" : dnum.get(),
            "LastUpdate" : Date.get(),
            "CurrentStatus": statlist.get(),
            "Weight": weight.get(),
            "Rentention": renten.get(),
        } ##Creat json string
        with open(filename, "w") as out_file:
            json.dump(obj, out_file)        ##Create json file

        def Destroy():##Destroy TopLevel & popup
            popup.destroy()
            df.destroy()

        popup = Tk()
        popup.wm_title("Success")
        Label(popup,text='The File has successfully change to Json').pack()
        Button(popup,text="Ok", command =Destroy).pack()


    Button(df, text="Exhcange to JSON",command=Createjson).grid(row=10, column=2)



def showjson():
    name = fd.askopenfilename(initialdir="E:/PycharmProjects", filetypes={("JSON", "*.json"), ("text file", "*.txt")})
    with open (name,"r") as reader:
        targetfile = json.loads(reader.read())
    sj = Toplevel(root)
    sj.title("Order Detail")
    Label(sj, text="Order Detail", font=20).grid(row=0)
    Label(sj, text="Order Number",font = 15).grid(row=1)
    Label(sj, text=targetfile["OrderNumber"],font = 15).grid(row=1, column=1)
    Label(sj, text="Product Name",font = 15).grid(row=2)
    Label(sj, text=targetfile["ProductName"], font = 15).grid(row=2, column=1)
    Label(sj, text="Quantity",font =15).grid(row=3)
    Label(sj, text=targetfile["Quantity"],font = 15).grid(row=3, column=1)
    Label(sj, text="Customer Name",font = 15).grid(row=4)
    Label(sj, text=targetfile["CustomerName"],font = 15).grid(row=4, column=1)
    Label(sj, text="Stock(Y/N)",font = 15).grid(row=5)
    Label(sj, text=targetfile["Stock"],font = 15).grid(row=5, column=1)
    Label(sj, text="Address",font = 15).grid(row=6)
    Label(sj, text=targetfile["Address"],font = 15).grid(row=6, column=1)
    Label(sj, text="Contact",font = 15).grid(row=7)
    Label(sj, text=targetfile["Contact"],font = 15).grid(row=7, column=1)
    Label(sj, text="Delivery Method",font = 15).grid(row=8)
    Label(sj, text= targetfile["Delivery"],font = 15).grid(row=8, column=1)
    Label(sj, text="Price",font = 15).grid(row=9)
    Label(sj, text= targetfile["Price"],font = 15).grid(row=9, column=1)
    Button(sj,text="Back",command = sj.destroy).grid(row=10, column=2)


def orderstatus():
    os = Toplevel(root)
    os.title("Check Order")
    Label(os,text= 'Choose the Json file by the Order Number',font = 15 ).grid(row=0, column=1)
    Button(os,text='Open the File', command = showjson).grid(row=1, column=1, pady= 15)
    Button(os,text='Back to Menu',command = os.destroy).grid(row =2,column=2)



##Main Menu
def main():
    global root
    root = Tk()
    root.geometry('200x300+600+400')
    root.title("Post Office Amazon IOS")
    title = Label(root, text="Post Office Amazon IOS", font=18)
    title.grid(row=0, pady=15, sticky=S)
    order = Button(root, text="Send Delivery Detail", font=12, pady=15, command=deliveryform)
    order.grid(row=1, pady=15, sticky=S)
    receive = Button(root, text="Get Order Status", font=12, pady=15, command=orderstatus)
    receive.grid(row=2, sticky=S, pady= 15)
    Button(root, text="Exit", font=12, command=root.quit).grid(columnspan=2, sticky=E)

    root.mainloop()
    ##start the GUI

main()
##call the screen function
