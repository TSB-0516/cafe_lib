from tkinter import *
#from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
import random
import time
from threading import Thread
import os
import subprocess

from AddBook import *
from ViewBook import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *


root = Tk()
root.title('Welcome!')
root.state('zoomed')
root.resizable(False,False)

def cafe1():
    os.system('cafe.py')
def clicked():
    Thread(target=cafe1).start() 


def libwin():
    global w1, w2,w3, w4, w5, w6
    root.destroy()
    w1= Tk()
    w1.title("Library")
    w1.minsize(width=400, height=400)
    w1.geometry("600x500")


    headingFrame1 = Frame(w1, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to \n Library", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(w1, text="Add Book Details", bg="black", fg="cyan", bd=5, command=addBook)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.08)

    btn2 = Button(w1, text="Delete Book", bg="black", fg="cyan", bd=5, command=delete)
    btn2.place(relx=0.28, rely=0.48, relwidth=0.45, relheight=0.08)

    btn3 = Button(w1, text="View book list", bg="black", fg="cyan", bd=5, command=view)
    btn3.place(relx=0.28, rely=0.56, relwidth=0.45, relheight=0.08)

    btn4 = Button(w1, text="Issue Book", bg="black", fg="cyan", bd=5, command=issueBook)
    btn4.place(relx=0.28, rely=0.64, relwidth=0.45, relheight=0.08)

    btn5 = Button(w1, text="Return Book", bg="black", fg="cyan", bd=5, command=returnBook)
    btn5.place(relx=0.28, rely=0.72, relwidth=0.45, relheight=0.08)

    quit_btn = Button(w1, text="Quit", bg="black", fg="cyan", bd=5, command=w1.destroy)
    quit_btn.place(relx=0.28, rely=0.80, relwidth=0.45, relheight=0.08)


#c1--->HOME PAGE

We_label=Label(root,text='Welcome!',font=('Aria','53','bold'), fg='#0000AA')
We_label.pack(pady=20)

#Frame for buttons
fr1=LabelFrame(root,padx=10,pady=10,bd=0)
fr1.place(relx=0.4,rely=0.5)
#os.system("shutdown /s /t 1")

#Cafe
c_btn = Button(fr1,text='CAFÉ', bg='#00AAAA',command=clicked,font=('Courier New','15','bold'), relief=RAISED, width=20, height=1,bd=5)
c_btn.grid(row=0, column=0,columnspan=2)

#LIB
l_btn = Button(fr1, text='LIBRARY', command=libwin, font=('Courier New','15'), bg='#00AAAA', relief=RAISED, width=20, height=1,bd=5)
l_btn.grid(row=1, column=0,columnspan=2)

#QUIT BTN
q_btn = Button(fr1,text='Quit',command=root.destroy,bd=5,font=('Courier New','15'), bg='grey',fg='white', width=20, height=1)
q_btn.grid(row=2,column=0, columnspan=2,pady=12)



root.mainloop()

    
