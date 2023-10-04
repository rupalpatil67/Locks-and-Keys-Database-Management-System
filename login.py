from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
import mysql.connector
from gtts import gTTS
from playsound import playsound
from time import strftime
import pygame



#####################################################################################################################################################
def logi():


    win = Toplevel()
    win.attributes('-fullscreen', True)
    win.title("MAIN FORM")
    win.config(bg="skyblue")

    path = Image.open("logo.png")
    render = ImageTk.PhotoImage(path)
    img1 = Label(win, image=render,bg="skyblue")
    img1.place(x=530, y=0)
    l1 = Label(win, text="     Admin Login                   ", font=("Berlin sans Fb", 30), height=2,width=82,fg='white',bg='black')
    l1.place(x=0, y=200)

    ########################################################################################################################################################
    def time():
        string = strftime('%H:%M:%S:%p')
        label.config(text=string)
        label.after(1000, time)


    label = Label(win, font=("Imprint MT Shadow", 20), bg="skyblue", fg="black")
    label.place(x=5, y=5)
    ###################################################################################################################################################
    t2 = Label(win, text=datetime.date.today(), fg='Black', bg="skyblue", font=("Imprint MT Shadow", 20))
    t2.place(x=5, y=40)
    b4 = Button(win, text="Back",  bg="skyblue", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=win.destroy)
    b4.place(x=1400, y=5)
    b5 = Button(win, text="Exit",  bg="skyblue", fg='white', font=("arial", 13, "bold"), relief=RIDGE, borderwidth=5,command=quit)
    b5.place(x=1480, y=5)
    ##############################################################################################################################################################

    def login():
        def log():

            s1 = t1.get()
            s2 = t2.get()

            if s1 == "":
                messagebox.showwarning("WARNING..!", "Please enter USERNAME")
                return
            if s1 == "Rupal" and s2 == "123":
                messagebox.showinfo("Message..", "Login Successfully")
                t1.delete(0, END)
                t2.delete(0, END)
                def hello():
                    import Admin
                    Admin.admin()
                hello()

                #mainwin.distroy()
            else:
                messagebox.showinfo("Message..", "Wrong id or pass")

            if s2 == "":
                messagebox.showwarning("WARNING..!", "Please enter PASSWORD")
                return

    ######################################################################################################################################################
        # mytext = 'Welcome to Admin Login!'
        # language = 'en'
        # myobj = gTTS(text=mytext, lang=language, slow=False)
        # myobj.save("welcome.mp3")
        #
        # playsound('welcome.mp3')
        # print('playing sound using playsound')
    ######################################################################################################################################################
        l2 = Label(win, text=" USERNAME ::", font=("arial",29, "bold"),  bg="skyblue")
        l2.place(x=500, y=350)
        l3 = Label(win, text=" PASSWORD ::", font=("arial", 29, "bold"),  bg="skyblue")
        l3.place(x=500, y=430)
        t1 = Entry(win, bd=2, font=("arial", 18))
        t1.place(x=800, y=360)
        t2 = Entry(win, bd=2, font=("arial", 18),show="*")
        t2.place(x=800, y=440)
        b1 = Button(win, text="    LOG    ", font=("arial", 15, "bold"), relief=RIDGE, borderwidth=12, bg="skyblue",command=log)
        b1.place(x=600, y=500)
        b2 = Button(win, text="    Exit    ", font=("arial", 15, "bold"), relief=RIDGE, borderwidth=12, fg='#404040', bg="skyblue", command=win.destroy)
        b2.place(x=750, y=500)
        time()
        mainloop()
    login()
logi()