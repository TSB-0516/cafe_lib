from tkinter import *
#from PIL import ImageTk, Image
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


allBid = []  #to store all bokk ids which will issued.

def issue():
    global issuebtn, labelFrame, inf1, inf2, lb1, quitBtn, w5, Canvas1, status

    bid = inf1.get()        #take the book id with get()
    issueto = inf2.get()    #take the name to whom it is issued

    issuebtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    extractBid = "select Book_Id from LIBRARY"

    try:
        cs.execute(extractBid)
        #mydb.commit()

        for i in cs:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select Status from LIBRARY where Book_Id = '"+bid+"'"
            cs.execute(checkAvail)
            #mydb.commit()
            for i in cs:
                check = i[0]

            if check == 'available':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book Id not present")

    except:
        messagebox.showinfo("Error", "Can't fetch the Book Id")

    issueSql = "insert into books_issued values (%s, %s)"
    value = (bid,issueto)
    show = "select * from books_issued"

    updateStatus = "update LIBRARY set Status = 'issued' where Book_Id = '"+bid+"'"

    try:
        if bid in allBid and status == True:
            cs.execute(issueSql,value)
            mydb.commit()
            cs.execute(updateStatus)
            mydb.commit()
            messagebox.showinfo("Success", "Book Issued successfully")
            w5.destroy()
        else:
            allBid.clear()
            messagebox.showinfo("Message", "Book Already Issued")
            w5.destroy()
            return

    except:
        messagebox.showinfo("Search Error", "The value insert is wrong, Try again")

    print(bid)
    print(issueto)
    allBid.clear()

def issueBook():
    global issuebtn, labelFrame, inf1, inf2, lb1, quitBtn, w5, Canvas1, status

    w5=Tk()
    w5.title("Library")
    w5.minsize(width=400, height=400)
    w5.geometry("600x500")

    Canvas1 = Canvas(w5)
    Canvas1.config(bg="#c0bbfa")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(w5, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel1 = Label(headingFrame1, text="Issue Book", bg="black", fg="white", font=('Courier',15))
    headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(w5, bg="black")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    #Book Id
    lb1 = Label(labelFrame, text="Book Id", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    #to whom book is issued, student name
    lb2 = Label(labelFrame, text="Issue To", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    #Issue Button
    issuebtn = Button(w5, text="Issue", bg="#d1ccc0", fg="black", command=issue)
    issuebtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(w5, text="Quit", bg="#aaa69d", fg="black", command=w5.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    w5.mainloop()
