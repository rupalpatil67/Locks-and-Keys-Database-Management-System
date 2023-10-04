from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import datetime

import mysql.connector
from PIL import ImageTk, Image
#import addrec,delrec

def main1():
    global img
    win = Toplevel()
    #win = Toplevel()
    win.attributes('-fullscreen', True)
    win.title("Lock and Key")

    # logo
    # img = Image.open("logo.png")
    # svkmname = ImageTk.PhotoImage(img)
    # img = Label(win, image=svkmname)
    # img.place(x=550, y=30)

    img = Label(win, text="Search Record", fg="black", bg="#6dd8fd", font=("book man", 28, "bold"))
    img.place(x=0, y=40)
    img.config(height=3, width=80)

    # l1 = Label(win, text="Locks And Key Database Management System", font=("arial", 25), fg='black', relief="solid")
    # l1.place(x=450, y=180)
    # img = ImageTk.PhotoImage(Image.open("logo.png"))
    # svkmname =  Label(win, image=img,height=120,width=1550)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lockandkey"
    )

    # show department names
    def dep(self):
        def accno(self):
            fac = str(c2.get())
            # c2 for combobox 2
            # print(fac)
            mycur = mydb.cursor()
            mycur.execute("select lockerno from it where name='%s'" % (fac))
            accnum = mycur.fetchall()
            # print(accnum)
            arr = []
            for i in accnum:
                a = str(i[0])
                arr.append(a)
            l6 = Label(win, text=arr, bd=2, font=("arial", 16), fg='black', borderwidth=0, relief="solid")
            l6.place(x=390, y=530)

        depnam = c1.get()
        falculty = ("None")
        if depnam == "Information Technology Department":
            mycur = mydb.cursor()
            mycur.execute("select name from it;")
            falculty = mycur.fetchall()
            arr=[]
            for i in falculty:
                if i[0] not in arr:
                    arr.append((i[0]))
        l4 = Label(win, text="Select Faculty : ", bd=2, font=("arial", 17), fg='black', borderwidth=0, relief="solid")
        l4.place(x=100, y=430)
        c2 = Combobox(win, values=arr, state="readonly", font=("arial", 15))
        c2.place(x=390, y=430)
        c2.bind("<<ComboboxSelected>>", accno)
        l5 = Label(win, text="Alloted Lockers : ", bd=2, font=("arial", 17), fg='black', borderwidth=0, relief="solid")
        l5.place(x=100, y=530)

    def search():
        pass

        # SHORT WIN
        def ser():

            accno = t1.get()
            print(accno)
            if accno == "":
                messagebox.showwarning("WARNING..!", "Please Enter Locker Number..")
            else:
                mycur = mydb.cursor()
                mycur.execute("select name from it where lockerno=" + accno)
                falcultynam = mycur.fetchone()
                #
                mycur = mydb.cursor()
                mycur.execute("select keyhold from it where lockerno=" + accno)
                keyhold = mycur.fetchone()

                mycur = mydb.cursor()
                mycur.execute("SELECT date FROM transtb where asslock = " + accno)
                date1 = mycur.fetchone()
                print(date1)
                #
                def clear():
                    l6.config(text="")
                    #l7.config(text="")
                # print(falcultynam)
                if falcultynam == None:
                    messagebox.showinfo("WARNING..!", "Loker Number Not Found..")
                else:
                    l11.config(text=keyhold)
                    l6.config(text=falcultynam)
                    l7.config( text=date1)
                    l8 = Label(newWindow, text="Faculty Name :", bd=2, font=("arial", 16), fg='black', borderwidth=0,
                               relief="solid")
                    l8.place(x=50, y=180)


                    l9 = Label(newWindow, text=" Assign Date :", bd=2, font=("arial", 16), fg='black', borderwidth=0,
                               relief="solid")
                    l9.place(x=50, y=270)
                    ##
                    l10 = Label(newWindow, text="Key holder's name :", bd=2, font=("arial", 16), fg='black', borderwidth=0,
                               relief="solid")
                    l10.place(x=50, y=370)


                    ##

        newWindow = Toplevel(win)
        newWindow.title("Search By Locker Number :")
        newWindow.geometry("400x500")
        l4 = Label(newWindow, text="Enter Locker Number", bd=2, font=("arial", 16), fg='black', borderwidth=0,
                   relief="solid")
        l4.place(x=45, y=70)
        t1 = Entry(newWindow)
        t1.place(x=250, y=70)
        b3 = Button(newWindow, text="  Search  ", font=("arial", 13), fg='black', borderwidth=0.5, relief="solid",
                    command=ser)
        b3.place(x=150, y=120)
        l6 = Label(newWindow, bd=2, font=("arial", 16), fg='black', borderwidth=0,
                   relief="solid")
        l6.place(x=250, y=180)
        l7 = Label(newWindow, bd=2, font=("arial", 16), fg='black', borderwidth=0,
                   relief="solid")
        l7.place(x=230, y=270)
        l11 = Label(newWindow, bd=2, font=("arial", 16), fg='black', borderwidth=0,
                    relief="solid")
        l11.place(x=250, y=370)
    b1 = Button(win, text="back", command=win.destroy,font=("arial", 10))
    b1.place(x=5, y=5)

    b1 = Button(win, text="  Exit  ", font=("arial", 13), fg='black', borderwidth=0.5, relief="solid", command=quit)
    b1.place(x=1400, y=200)

    # Button 2 of Search
    b2 = Button(win, text=" Search By Locker Number ", font=("arial", 15), fg='black', borderwidth=0.5,relief="groove",command=search,
                bg="#6dd8fd")
    b2.place(x=900, y=430)

    # lab = Label(win, text="  Search Record  ", font=("arial", 25), fg='black', relief="solid")
    # lab.place(x=655, y=260)

    # lab=Label(win, text="Search Record", bd=2, font=("arial", 20), fg='black', borderwidth=0,relief="solid")
    # lab.place(x=200,y=200)

    date = datetime.date.today()
    year = date.year
    format = "%d %B " + str(year)
    date = date.strftime(format)
    date = Label(win, text=date, bd=2, font=("arial", 14), fg='black', borderwidth=0, relief="solid")
    date.place(x=1130, y=200)

    l3 = Label(win, text="Select Department Name : ", bd=2, font=("arial", 17), fg='black', borderwidth=0, relief="solid")
    l3.place(x=100, y=330)

    dept = ("Information Technology Department", "Computer Department")
    c1 = Combobox(win, values=dept, state="readonly", font=("arial", 16))
    c1.place(x=390, y=330)
    c1.bind("<<ComboboxSelected>>", dep)

    # def addrec():
    #     import addrec
    #     addrec.addrecord()
    # def deleterec():
    #     import delrec
    #     delrec.deleterecord()
    #
    # #b3 = Button(win, text="  Add Details  ", font=("arial", 14), fg='black', borderwidth=0.5, relief="solid",command=addrec)
    # #b3.place(x=1200, y=400)
    #
    # #b4 = Button(win, text="  Delete Records ", font=("arial", 14), fg='black', borderwidth=0.5,relief="solid",command=deleterec)
    # #b4.place(x=1200, y=500)

    win.mainloop()
main1()