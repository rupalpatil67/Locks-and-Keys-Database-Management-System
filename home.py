from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import datetime
import mysql.connector
from time import strftime
from PIL import Image,ImageTk
win=Tk()
win.attributes('-fullscreen',True)
path = Image.open("logo.png")
render = ImageTk.PhotoImage(path)
img = Label(win, image=render,height=120,width=1350)
win.config(bg="#9bddff")
img.place(x=0, y=50)
def login():
    import login
    login.logi()
def faculty():
    import search
    search.main1()
def time():
    string = strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000, time)


label = Label(win, font=("Imprint MT Shadow", 20), bg="#9bddff", fg="black")
label.place(x=5, y=5)
b1=Button(win, text="      Admin Login     ", font=("arial", 30), fg='black', borderwidth=3, relief="solid", bg="white",command=login)
b1.place(x=450,y=300)
b2=Button(win, text="         Search          ", font=("arial", 30), fg='black', borderwidth=3, relief="solid", bg="white",command=faculty)
b2.place(x=450,y=400)
b3=Button(win, text="Exit", font=("arial", 10), fg='white', borderwidth=3, relief="groove", bg="black",command=win.destroy)
b3.place(x=1220,y=0)
time()
win.mainloop()