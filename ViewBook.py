from tkinter import *
import mysql.connector
from tkinter import messagebox

#SQL CONNECTION
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Thamini@2006",
    database="Lib")
#Cursor
cs=mydb.cursor()


def view():
    w3 = Tk()
    w3.title("Library")
    w3.minsize(width=400, height=400)
    w3.geometry("600x500")

    Canvas1 = Canvas(w3)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(w3, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Books", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(w3, bg="black")
    LabelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)





    
    #add a text label to LabeFrame
    textLabel = Label(LabelFrame, text="%10s %40s %30s %20s"%('BID','Title','Author','Status'),bg="black", fg="white")
    textLabel.place(relx=0.07, rely=0.1)

    #addLine
    addline = Label(LabelFrame, text = "----------------------------------------------------------------------------",bg="black", fg="white")
    addline.place(relx=0.05, rely=0.2)
    
    y = 0.25    #declare var to increase the height at y-axis to print details
    #query to retrieve details from books table
    getbooks = "select * from LIBRARY "
    #try:
    cs.execute(getbooks)
    result = cs.fetchall()
    mydb.commit()
    for i in result:
        Label(LabelFrame, text="%10s %40s %20s %20s"%(i[0],i[1],i[2],i[3]), bg="black", fg="white").place(relx=0.07, rely=y)
        y += 0.1
        
    #except:
    #messagebox.showinfo("Error","Failed to Fetch files from database")

    quitBtn = Button(w3, text="QUIT", bg='lightblue', fg="black", command=w3.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
