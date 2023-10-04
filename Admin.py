from tkinter import *
from PIL import Image,ImageTk

def admin():
    win = Toplevel()
    # win = Toplevel()
    win.attributes('-fullscreen', True)
    path = Image.open("logo.png")
    render = ImageTk.PhotoImage(path)

    img = Label(win, image=render,height=120,width=1350)
    # win.config(bg="#B0C4DE")
    win.config(bg="#9bddff")

    img.place(x=0, y=40)


    def addrec():
        import addrec
        addrec.addrecord()
    def delrec():
        import delrec
        delrec.deleterecord()
    def show():
        import showrec
        showrec.showrec()
    def SearchRec():
        import search
        search.main1()

    l1 = Label(win, text="  Locks And Key Database Management System  ", font=("arial", 20), fg='black', borderwidth=3,relief="groove",bd=3)
    l1.place(x=370, y=200)

    b1 = Button(win, text="Back", command=win.destroy)
    b1.place(x=5, y=5)

    b1 = Button(win, text="Exit", command=quit)
    b1.place(x=50, y=5)

    b3 = Button(win, text="Add Record",width = 15, font=("arial", 22), fg='black', borderwidth=3, relief="groove", bg="white",command=addrec)
    b3.place(x=370, y=400)

    b3 = Button(win, text="Delete Record",width = 15, font=("arial", 22), fg='black', borderwidth=3, relief="groove", bg="white",command=delrec)
    b3.place(x=370, y=500)

    b3 = Button(win, text="Search Record", width = 15,font=("arial", 22), fg='black', borderwidth=3, relief="groove", bg="white",command=SearchRec)
    b3.place(x=690, y=400)


    b3 = Button(win, text="Generate PDF",width = 15, font=("arial", 22), fg='black', borderwidth=3, relief="groove", bg="white",command=show)
    b3.place(x=690, y=500)

    win.mainloop()
admin()