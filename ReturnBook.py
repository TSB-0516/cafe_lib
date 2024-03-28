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

#enter the table names issueTable = "books_issued" bookTable = "books" 
allBid = []
 
def Return():
    global submitBtn, quitBtn, LabelFrame, lb1, Canvas1, bookInfo1, w6, status 
    bid = bookInfo1.get()
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
            if check == 'issued':
                status = True
            else:
                status = False 
        else:
            messagebox.showinfo("Error", "Book Id is not Present")
            
    except:
        messagebox.showinfo("Error", "Can't Fetch the book Id") 
        #remove that book from issueTable
        
    issueSql = "delete from books_issued where Book_Id = '"+bid+"'" 
    print(bid in allBid)
    print(status)
    updateStatus = "update LIBRARY set Status = 'available' where Book_Id='"+bid+"'"
    try:
        if bid in allBid and status == True:
            cs.execute(updateStatus)
            mydb.commit()
            messagebox.showinfo('Success', "Book returned successfully") 
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book id")
             
            w6.destroy()
            return

    except:
        messagebox.showinfo("Search Error", "the value you entered is wrong, try again!") 
        allBid.clear()
        w6.destroy() 


def returnBook():
    global w6, mydb, cs, labelFrame, submitBtn, quitBtn, Canvas1, bookInfo1, lb1 

    w6 = Tk()
    w6.title("Library")
    w6.minsize(width=400, height=400)
    w6.geometry("600x500") 

    Canvas1 = Canvas(w6)
    Canvas1.config(bg="#adddf7")
    Canvas1.pack(expand=True, fill=BOTH)
    
    headingFrame1 = Frame(w6, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    
    headingLabel = Label(headingFrame1, text="Return Book", bg="black", fg="white", font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(w6, bg="black")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    
    #book id
    lb1 = Label(labelFrame, text="Book Id", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.5)
     
    bookInfo1 = Entry(labelFrame)
    #bookInfo1.insert(0,'Enter B_ID')
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)
    
    #submit Button
    submitBtn = Button(w6, text="Submit", bg="lightblue", fg="black", command=Return)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
    #quit btn
    quitBtn = Button(w6, text="Quit", bg="lightblue", fg="black", command=w6.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    
    w6.mainloop()

