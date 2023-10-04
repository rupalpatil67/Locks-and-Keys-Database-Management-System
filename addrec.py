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
def addrecord():
    global img
    win = Tk()
    #win = Toplevel()
    win.attributes('-fullscreen', True)



    def save():
        s1=t1.get()
        s2=c1.get()
        s3=t2.get()
        s5=t5.get()
        s4 = datetime.date.today()
        s6=c2.get()
        #arrr = s3.split(",")
        #print(arrr)
        if s1 == "":
            messagebox.showwarning("WARNING..!", "Please enter Faculty's name..")
            return
        if s2 == "":
            messagebox.showwarning("WARNING..!", "Please Choose Dept Name..")
            return
        if s3 == "":
            messagebox.showwarning("WARNING..!", "Please enter loker number..")
            return
        if s5 == "":
            messagebox.showwarning("WARNING..!", "Please enter locker holder's name..")
            return
        if s6 == "":
            messagebox.showwarning("WARNING..!", "Please enter locker holder's name..")
            return
        #print(s1,s2,s3)
        #arrr=[]
        arrr=s3.split(",")
        for i in arrr:
            mycur = mydb.cursor()

            a = ("INSERT INTO it (name,lockerno,deptname,keyhold,type) values(%s,%s,%s,%s,%s)")
            mycur.execute(a, (s1, i, s2, s5, s6))
            a = ("INSERT INTO transtb (name,asslock,deptname,date) values(%s,%s,%s,%s)")
            mycur.execute(a, (s1, i, s2, s4))

            mydb.commit()
        messagebox.showinfo("Record Save", "Record Saved ...")
        t1.delete(0, END)
        c1.delete(0, END)
        t2.delete(0, END)
        t5.delete(0, END)

    # logo
    # path = Image.open("logo.png")
    # render = ImageTk.PhotoImage(path)
    img = Label(win, text="Assign Lockers",fg="black",bg="#6dd8fd",font=("book man",28,"bold"))
    img.place(x=0, y=40)
    img.config(height=3,width=80)

    # img.pack(side="top")



    # img = Image.open("logo.png")
    # svkmname = ImageTk.PhotoImage(img)
    # img = Label(win, image=svkmname)
    # img.place(x=550, y=40)

    # title
    win.title("Lock and Key")
    win.attributes('-fullscreen', True)

    # background image
    # img = ImageTk.PhotoImage(Image.open("logo.png"))
    # svkmname = Label(win, image=img)
    # svkmname.place(x=540, y=30)

    # l1 = Label(win, text=" Locks And Key DataBase ManageMent System ",font=("arial", 20), fg='black',relief="solid")
    # l1.place(x=490, y=180)

    # l2 = Label(win, text=" Assign Lockers  ",font=("arial", 20), fg='black',relief="solid")
    # l2.place(x=700, y=250)



    #create UI for add Entries to database

    #name entry
    b1 = Button(win, text="back", command=win.destroy,font=("arial", 10))
    b1.place(x=5, y=5)

    l3 = Label(win, text="Enter Faculty Name : ", bd=2, font=("arial", 22), fg='black', borderwidth=0, relief="solid")
    l3.place(x=300, y=240)
    t1 = Entry(win,bd=2,font=("arial", 22))
    t1.place(x=620, y=240)

    #Dept Name
    l4 = Label(win, text="Select Dept. Name : ", bd=2, font=("arial", 22), fg='black', borderwidth=0, relief="solid")
    l4.place(x=300, y=320)

    mycur = mydb.cursor()
    mycur.execute("select deptname from it ")
    accnum = mycur.fetchall()
    arr=[]
    for i in accnum:
        i=i[0]
        if i in arr:
            pass
        else:
            arr.append(i)

    c1=Combobox(win,values=arr,state="readonly", font=("arial", 22),width=19)
    c1.place(x=620,y=320)

    #assign Locker
    l5 = Label(win, text="Assign Lockers :", bd=2, font=("arial", 22), fg='black', borderwidth=0, relief="solid")
    l5.place(x=300, y=400)
    t2 = Entry(win, font=("arial", 22),bd=2)
    t2.place(x=620, y=400)

    ##
    l6 = Label(win, text="Key Holder Name : ", bd=2, font=("arial", 22), fg='black', borderwidth=0, relief="solid")
    l6.place(x=300, y=480)
    t5 = Entry(win, bd=2, font=("arial", 22))
    t5.place(x=620, y=480)
    ##
    l6 = Label(win, text="Type  : ", bd=2, font=("arial", 22), fg='black', borderwidth=0, relief="solid")
    l6.place(x=300, y=560)
    arr=["doors","lockers","cupboard"]
    c2 = Combobox(win, values=arr, state="readonly", font=("arial", 22), width=19)
    c2.place(x=620, y=560)

    #date
    date = datetime.date.today()
    year=date.year
    format = "%d %B "+str(year)
    date = date.strftime(format)
    date = Label(win, text=date, bd=2, font=("arial", 20), fg='black', borderwidth=0, relief="groove")
    date.place(x=1350, y=20)

    ###
    b4 = Button(win, text="  Save Record ", font=("arial", 15), fg='black', borderwidth=0.5, relief="groove",command=save,bg="#6dd8fd")
    b4.place(x=500, y=650)
    b1 = Button(win, text="  Exit  ", font=("arial", 15), fg='black', borderwidth=0.5, relief="groove", command=quit,bg="#6dd8fd")
    b1.place(x=750, y=650)


    win.mainloop()

#addrecord()
