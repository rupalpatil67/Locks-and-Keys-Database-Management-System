from tkinter import *
# from reportlab.pdfgen import canvas
import datetime
from fpdf import FPDF
import mysql.connector

from PIL import ImageTk, Image
def showrec():
    # win=Tk()
    win = Toplevel()
    win.attributes('-fullscreen', True)
    # win.attributes('-fullscreen', True)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="lockandkey"
    )

    # l1 = Label(win, text="Locks And Key Database Management System", font=("arial", 25), fg='black', relief="solid")
    # l1.place(x=430, y=180)
    def rup():
        import filehandling

    def showrecord():
        # logo
        # img = Image.open("logo.png")
        # svkmname = ImageTk.PhotoImage(img)
        # img=Label(win,image=svkmname)
        # img.place(x=550, y=30)

        img = Label(win, text="Show Details", fg="black", bg="#6dd8fd", font=("book man", 28, "bold"))
        img.place(x=0, y=40)
        img.config(height=3, width=80)

        def gen():
            mycur = mydb.cursor()
            mycur.execute("select * from it ")
            data = mycur.fetchall()
            print((data))
            aa = "\n\t\t\tDetails\n\n\n"
            t1.insert(END, aa)
            t1.insert(END, "Depeartment Name \t Faculty Name \t Number \t keyholder \t\t type\n\n")
            for i in data:
                t1.insert(END, i[0])
                t1.insert(END, "\t\t")
                t1.insert(END, i[1])
                t1.insert(END, "\t\t\t")
                t1.insert(END, i[2])
                t1.insert(END, "\t")
                t1.insert(END, i[3])
                t1.insert(END, "\t")
                t1.insert(END, i[4])
                # t1.insert(END, "\t")
                # t1.insert(END, i[5])
                t1.insert(END, "\n")

            # length = len(data) + 1
            # for i in range(length):
            #
            #     for j in range(0, 3):
            #         print(j)
            #         da = "\n\n Depeartment Name : \t" + str(data[i][j])
            #         t1.insert(END, da)
            #         print(data[i][j])
            #         da = "\nApplicant's Details"
            #         daa = "\n\nFaculty Name   :" + str(data[i][j + 1])
            #         t1.insert(END, daa)
            #         if j==2:
            #             da =  "\n Assign locker    :" + str(data[i][j+2])
            #         else:
            #             da = "\n Assign locker    :" + str(data[i][j + 1])
            #         t1.insert(END,da)
            #
            #     print("lop chya  banher")
            ######################################################
            # text = "\n"
            # fp = open('recrd.txt', 'w')
            # mycur = mydb.cursor()
            # mycur.execute("select * from it ")
            # data = mycur.fetchall()
            # print(data)
            # t1.insert(END,"Depeartment Name\t\t\t\t\t\t Name \t\t\t Assgin Lockers \n\n")
            # for i in data:
            #     for j in i:
            #         # print(j)
            #         line = ""
            #         line = str(j) + "\t\t"
            #         t1.insert(END," | ")
            #         t1.insert(END,line)
            #     t1.insert(END,"\n")

        b1 = Button(win, text="back", command=win.destroy, font=("arial", 10))
        b1.place(x=5, y=5)

        b1 = Button(win, text="  Generate Record  ", font=("arial", 18), bg="#82ddf6", fg='black', borderwidth=0.5,
                    relief="groove", command=gen)
        b1.place(x=250, y=400)

        b1 = Button(win, text="  Generate PDF  ", font=("arial", 18), bg="#82ddf6", fg='black', borderwidth=0.5,
                    relief="groove", command=rup)
        b1.place(x=260, y=500)

        b2 = Button(win, text=" Exit ", font=("arial", 10), fg='black', command=quit)
        b2.place(x=50, y=5)

        t1 = Text(win, width=70)
        t1.place(x=550, y=270)
        win.mainloop()
    showrecord()
