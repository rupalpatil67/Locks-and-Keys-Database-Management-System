from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import datetime
import mysql.connector
from PIL import ImageTk, Image

# database connected
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lockandkey"
)


def deleterecord():
    def clearfiled():
        t1.delete(0, END)
        t2.delete(0, END)
        #t3.delete(0, END)
    global img
    #win = Tk()
    win = Toplevel()
    win.attributes('-fullscreen', True)
    # logo
    #path = Image.open("logo.png")
    #render = ImageTk.PhotoImage(path)
    #img = Label(win, image=render,height=120,width=1550)
    #img.place(x=0, y=40)

    # title
    win.title("Lock and Key")
    win.attributes('-fullscreen', True)
    # img = ImageTk.PhotoImage(Image.open("logo.png"))
    # svkmname = Label(win, image=img)
    # svkmname.place(x=560, y=30)

    #logo
    # img = Image.open("logo.png")
    # svkmname = ImageTk.PhotoImage(img)
    # img = Label(win, image=svkmname)
    # img.place(x=560, y=30)

    img = Label(win, text="Delete Record", fg="black", bg="#6dd8fd", font=("book man", 28, "bold"))
    img.place(x=0, y=40)
    img.config(height=3, width=80)

    ##date
    date = datetime.date.today()
    year = date.year
    format = "%d %B " + str(year)
    date = date.strftime(format)
    date = Label(win, text=date, bd=2, font=("arial", 18), fg='black', borderwidth=0, relief="solid")
    date.place(x=1350, y=15)

    def search():

        name=t1.get()
        locker=str(t2.get())
        #print(name,locker)
        #print("search" )
        t3.delete('1.0', END)
        if name == '' and locker == '':
            messagebox.showwarning(title="warn",message="Fill any Field ")
        elif name == '' and locker != '':
            print("first if")
            mycur = mydb.cursor()
            mycur.execute("select * from it where lockerno="+(str(locker)))
            data = mycur.fetchall()
            print(data)
            asslock = []
            for i in data:
                a = i[2]
                asslock.append(a)
            data = data[0]

            da = "\nApplicant's Details"
            da = da + "\n\n Depeartment Name    :" + str(data[0])
            da = da + "\n Faculty Name          :" + str(data[1])
            da = da + "\n Assign Locker         :" + str(asslock)
            t3.insert(END, da)
            locknum = data[2]

            print(locknum)



        elif name != '' and locker == '':
            print("first else if")
            mycur = mydb.cursor()
            mycur.execute("select * from it where name='%s'"%(name))
            data = mycur.fetchall()
            print(data)
            asslock=[]
            for i in data:
                a=i[2]
                asslock.append(a)
            data=data[0]
            da = "\nApplicant's Details"
            da = da + "\n\n Depeartment Name    :" + str(data[0])
            da = da + "\n Faculty Name          :" + str(data[1])
            da = da + "\n Assign Locker         :" + str(asslock)
            t3.insert(END, da)
            #print(names)
            locknum = data[2]
            #deptn=str(data[0])
            #print(locknum,deptn)
        #clearfiled()


        def delete():

            name = t1.get()
            loc = locknum
            #locker = str(t2)
            s4 = datetime.date.today()


            mycur = mydb.cursor()
            mycur.execute("select * from it where lockerno='%s'" % (loc))
            data = mycur.fetchone()
            #print((data))
            dept=data[0]
            print(dept)

            if loc == '' and locker != '':
                #print(("11 loop"))
                mycur=mydb.cursor()
                a = ("INSERT INTO delrec (facname,locnum,date,deptname) values(%s,%s,%s,%s)")
                mycur.execute(a, (name,locker,s4,dept))
                mydb.commit()
            elif loc != '' and locker == '':
                print("loopp")
                mycur = mydb.cursor()
                a = ("INSERT INTO delrec (facname,locnum,date,deptname) values(%s,%s,%s,%s)")
                mycur.execute(a, (name, loc,s4,dept))
                mydb.commit()

            if name == '' and locker != '':
                mycur = mydb.cursor()
                mycur.execute("delete from it where it.lockerno='%s'" %(locker))
                mydb.commit()
                messagebox.showinfo("Record Save", "Record deleted succesfully ...")

                # names = mycur.fetchall()
            elif name != '' and locker == '':
                mycur = mydb.cursor()
                mycur.execute("delete from it where it.name='%s'" %(name))
                mydb.commit()
                messagebox.showinfo("Record Save", "Record deleted succesfully ...")
            t3.delete('1.0', END)
            clearfiled()


                # names = mycur.fetchall()

        delbutn = Button(win, text="Delete", font=("arial", 15), fg='black', borderwidth=0.5, relief="groove", command=delete, bg="#6dd8fd")
        delbutn.place(x=500,y=610)



    ##
    b1 = Button(win, text="back", command=win.destroy,font=("arial", 10))
    b1.place(x=5, y=5)


    # l1 = Label(win, text=" Locks And Key DataBase ManageMent System  ",font=("arial", 25), fg='black',relief="solid")
    # l1.place(x=430, y=180)
    # l2 = Label(win, text=" Delete Records  ", font=("arial", 25), fg='black',relief="solid")
    # l2.place(x=655, y=260)
    l3 = Label(win, text="Enter Faculty Name : ", bd=2, font=("arial", 20), fg='black', borderwidth=0, relief="solid")
    l3.place(x=60, y=350)
    l4 = Label(win, text="Delete By Locker Number : ", bd=2, font=("arial", 20), fg='black', borderwidth=0, relief="solid")
    l4.place(x=60, y=450)
    b2 = Button(win, text="  Search  ", font=("arial", 15), fg='black',relief="groove", command=search,bg="#6dd8fd",borderwidth=0.5)
    b2.place(x=200, y=610)
    b1 = Button(win, text="  Exit  ", font=("arial", 15), fg='black', relief="groove", command=quit, bg="#6dd8fd",borderwidth=0.5)
    b1.place(x=360, y=610)

    #b3 = Button(win, text="  Exit  ", font=("arial", 10), fg='black', borderwidth=0.5, relief="solid", command=quit)
    #b3.place(x=1400, y=200)

    t1 = Entry(win,bd=2, font=("arial", 20))
    t1.place(x=400, y=365)

    t2 = Entry(win,bd=2, font=("arial", 20))
    t2.place(x=400, y=450)

    t3 = Text(win, width=60)
    t3.place(x=750, y=280)


    win.mainloop()

deleterecord()