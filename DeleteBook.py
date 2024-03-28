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


def deleteBook():
    bid = bookInfo1.get()

    deleteSql = "delete from LIBRARY where Book_Id = "+bid+""
    deleteIssue = "delete from books_issued where Book_Id ="+bid+""

    try:
        cs.execute(deleteSql)
        mydb.commit()
        cs.execute(deleteIssue)
        mydb.commit()
        messagebox.showinfo("Success", "Book Deleted Successfully")

    except:
        messagebox.showinfo("Error", "Please check Book Id")

    #print(bid)

    bookInfo1.delete(0, END)
    w4.destroy()

def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, cs, mydb, w4

    w4 = Tk()
    w4.title("Library")
    w4.minsize(width=400, height=400)
    w4.geometry("600x500")

    Canvas1 = Canvas(w4)
    Canvas1.config(bg="#6ec2b1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(w4, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    #add a leabel to heading Frame
    headingLabel = Label(headingFrame1, text="Delete Book", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #add a label frame to canvas to give a lebl insite it to delete book
    LabelFrame = Frame(w4, bg="black")
    LabelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    #take a book ID to delete
    lb2 = Label(LabelFrame, text="Book Id: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(LabelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    #submit button    
    submitBtn = Button(w4, text="Submit", bg="lightblue", fg="black", command=deleteBook)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(w4, text="Quit", bg="lightblue", fg="black", command=w4.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    w4.mainloop()
