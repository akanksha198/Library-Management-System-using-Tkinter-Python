from tkinter import *
import tkinter.messagebox
from tkinter.ttk import *
import mysql.connector 
from mysql.connector import Error

Connection=mysql.connector.connect(host='localhost',database='lms',user='root',password='mysql')
Cur=Connection.cursor()

def C():
    Connection.commit()

def F():
    print(Cur.fetchall())

Cur.execute('Drop database lms')
Cur.execute('create database lms')
Cur.execute('use lms')
Cur.execute('CREATE TABLE student(sap_id bigint primary key,s_name varchar(20),s_course varchar(40),s_branch varchar(30),s_year int);')
Cur.execute('CREATE TABLE book (book_id bigint primary key,book_name varchar(40),author_name varchar(20),price int,pb_name varchar(50),sap_id bigint,foreign key(sap_id) references student(sap_id));')

window=Tk()
window.geometry("1550x1400")
window.title("NMIMS SHIRPUR CAMPUS")
window.config(background='PINK')
ourMessage="LIBRARY MANAGEMENT SYSTEM"
s=("Arial",25)
messageVar=Label(window,text=ourMessage,font=s).place(x=450,y=0)
newMessage="Choose From Below:"
m=("Arial",15)
messageVar=Label(window,text=newMessage,font=m).place(x=600,y=80)


def S1():
    window1=Tk()
    window1.geometry("1550x1400")
    window1.title("NMIMS SHIRPUR CAMPUS")
    window1.config(background='PINK')
    ourMessage="LIBRARY MANAGEMENT SYSTEM"
    newMessage="Student Details"
    s=("Arial",25)
    m=("Arial",15)
    messageVar=Label(window1,text=ourMessage,font=s).place(x=450,y=0)
    messageVar=Label(window1,text=newMessage,font=m).place(x=600,y=80)
    c=StringVar()
    l1=Label(window1,text='Enter Students Name:').place(x=490,y=150)
    e1=Entry(window1)
    e1.place(x=640,y=150)
    l2=Label(window1,text='Enter SAP ID:').place(x=490,y=190)
    e2=Entry(window1)
    e2.place(x=640,y=190)
    l3=Label(window1,text='Enter Course:').place(x=490,y=230)
    e3=Entry(window1)
    e3.place(x=640,y=230)
    l4=Label(window1,text='Enter Branch:').place(x=490,y=270)
    e4=Entry(window1)
    e4.place(x=640,y=270)
    l5=Label(window1,text='Enter Students Year:').place(x=490,y=310)
    e5=Entry(window1)
    e5.place(x=640,y=310)
    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)

    def Submit():
        print(e1.get())
        print(e2.get())
        print(e3.get())
        print(e4.get())
        print(e5.get())
        name=e1.get()
        sap=e2.get()
        course=e3.get()
        branch=e4.get()
        year=e5.get()
        print(name,sap,course,branch,year)
        studentquery='INSERT INTO student(sap_id,s_name,s_course,s_branch,s_year) VALUES(%s,%s,%s,%s,%s);'
        studentdetails=(sap,name,course,branch,year)
        
        try:
            Cur.execute(studentquery,studentdetails)
            C()
            Cur.execute('select* from student;')
            tkinter.messagebox.showinfo('Success',"Student details successfully submitted")
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        F()
        
    B4= Button(window1,text ="Submit", command=Submit).place(x=550,y=360)
    B5= Button(window1,text ="Clear", command=clear).place(x=620,y=360)
    def Cancel():
        tkinter.messagebox.showinfo("Your form canceled")
    B6=Button(window1,text ="Cancel", command=lambda:[Cancel(),window1.destroy()]).place(x=670,y=360)
    window1.mainloop()

B1= Button(window, text ="Add Student Details", command=S1).place(x=530,y=160)
def s2():
    window2=Tk()
    window2.geometry("1600x1500")
    window2.title("NMIMS SHIRPUR CAMPUS")
    window2.config(background='PINK')
    ourMessage="LIBRARY MANAGEMENT SYSTEM"
    newMessage="Book Details"
    s=("Arial",25)
    m=("Arial",15)
    messageVar=Label(window2,text=ourMessage,font=s).place(x=450,y=0)
    messageVar=Label(window2,text=newMessage,font=m).place(x=600,y=80)
    l6=Label(window2,text='Enter Book Id:' ).place(x=490,y=150)
    e6=Entry(window2)
    e6.place(x=640,y=150)
    l7=Label(window2,text='Enter Books Name: ').place(x=490,y=190)
    e7=Entry(window2)
    e7.place(x=640,y=190)
    l8=Label(window2,text='Enter Authors Name: ').place(x=490,y=230)
    e8=Entry(window2)
    e8.place(x=640,y=230)
    l9=Label(window2,text='Enter Publications Name:').place(x=490,y=270)
    e9=Entry(window2)
    e9.place(x=640,y=270)
    l11=Label(window2,text='Enter Price of Book:').place(x=490,y=310)
    e11=Entry(window2)
    e11.place(x=640,y=310)
    def Clear():
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e11.delete(0,END)
    def Submit():
        print(e6.get())
        print(e7.get())
        print(e8.get())
        print(e9.get())
        print(e11.get())
        a=e6.get()#id
        b=e7.get()#name
        c=e8.get()#author_name
        d=e9.get()#publication
        e=e11.get()#price
        print(a,b,c,d,e)
        bookquery='INSERT INTO book(book_id,book_name,author_name,pb_name,price,sap_id) VALUES(%s,%s,%s,%s,%s,NULL);'
        bookval=(a,b,c,d,e)
        try:
            Cur.execute(bookquery,bookval)
            Cur.execute('select* from book;')
            F()
            tkinter.messagebox.showinfo("Success",'Book details successfully submitted')
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        C()
        window2.destroy()
    B1= Button(window2, text ="Submit", command=Submit).place(x=550,y=400)
    B2= Button(window2, text ="Clear", command=Clear).place(x=620,y=400)
    def Cancel():
       tkinter.messagebox.showinfo("Your form canceled")
    B3=Button(window2, text ="Cancel", command=lambda:[Cancel(),window2.destroy()]).place(x=670,y=400)
    window2.mainloop()
B9= Button(window, text ="Add Book Details", command=s2).place(x=530,y=210)


def s3():
    window3=Tk()
    window3.geometry("1600x1500")
    window3.title("NMIMS SHIRPUR CAMPUS")
    window3.config(background='PINK')
    ourMessage="LIBRARY MANAGEMENT SYSTEM"
    newMessage="Students Issuing Book"
    s=("Arial",25)
    m=("Arial",15)
    messageVar=Label(window3,text=ourMessage,font=s).place(x=450,y=0)
    messageVar=Label(window3,text=newMessage,font=m).place(x=600,y=80)
    '''l12=Label(window3,text='Enter Students Name: ').place(x=490,y=150)
    e12=Entry(window3)
    e12.place(x=640,y=150)'''
    l13=Label(window3,text='Enter SAP ID: ').place(x=490,y=190)
    e13=Entry(window3)
    e13.place(x=640,y=190)
    l14=Label(window3,text='Enter Book ID: ').place(x=490,y=230)
    e14=Entry(window3)
    e14.place(x=640,y=230)
    '''l15=Label(window3,text='Enter Books Name: ').place(x=490,y=270)
    e15=Entry(window3)
    e15.place(x=640,y=270)'''
    def Clear():
        #e12.delete(0,END)
        e13.delete(0,END)
        e14.delete(0,END)
        #e15.delete(0,END)

    def Submit():
        #print(e12.get())
        print(e13.get())
        print(e14.get())
        #print(e15.get())
        #a=e12.get()
        sap=e13.get()
        book=e14.get()
        print(sap,book,"lololol")
        #d=e15.get()
        qwery="update book set sap_id = %s where book_id = %s and sap_id IS NULL"
        data=(sap,book)
        try:
            Cur.execute(qwery,data)
            tkinter.messagebox.showinfo("success","book has been issued")
            Cur.execute('select * from book')
            F()
        except mysql.connector.Error as lol:
            print('Error: {}'.format(lol)) 
        C()
    B1= Button(window3, text ="Submit", command=Submit).place(x=490,y=330)

    B2= Button(window3, text ="Clear", command=Clear).place(x=710,y=330)
    def Cancel():
       tkinter.messagebox.showinfo("Your form canceled")
    B3=Button(window3, text ="Cancel", command=lambda:[Cancel(),window3.destroy()]).place(x=600,y=330)
    window3.mainloop()
B8= Button(window, text ="Record for Student Issuing Book", command=s3).place(x=530,y=260)
def s4():
    window4=Tk()
    window4.geometry("1600x1500")
    window4.title("NMIMS SHIRPUR CAMPUS")
    window4.config(background='PINK')
    ourMessage="LIBRARY MANAGEMENT SYSTEM"
    newMessage="Student Returning Book"
    s=("Arial",25)
    m=("Arial",15)
    messageVar=Label(window4,text=ourMessage,font=s).place(x=450,y=0)
    messageVar=Label(window4,text=newMessage,font=m).place(x=600,y=80)
  
    l16=Label(window4,text='Enter Book ID: ').place(x=490,y=150)
    e16=Entry(window4)
    e16.place(x=640,y=150)
    '''l17=Label(window4,text='Enter Books Name: ').place(x=490,y=190)
    e17=Entry(window4)
    e17.place(x=640,y=190)
    l18=Label(window4,text='Enter Students Name:').place(x=490,y=230)
    e18=Entry(window4)
    e18.place(x=640,y=230)'''
    l19=Label(window4,text='Enter SAP ID:').place(x=490,y=270)
    e19=Entry(window4)
    e19.place(x=640,y=270)
    def Clear():
        e16.delete(0,END)
        #e17.delete(0,END)
        #e18.delete(0,END)
        e19.delete(0,END)
    
    def Submit():
        print(e16.get())
        #print(e17.get())
        #print(e18.get())
        print(e19.get())
        book=e16.get()
        sap=e19.get()
        qwery="update book set sap_id = NULL where book_id = %s and sap_id = %s"
        data=(book,sap)
        try:
            Cur.execute(qwery,data)
            tkinter.messagebox.showinfo("success","book has been returned")
            Cur.execute('select * from book')
            F()
        except mysql.connector.Error as lol:
            print('Error: {}'.format(lol)) 
        C()
    B1= Button(window4, text ="Submit", command=Submit).place(x=550,y=350)
    B2= Button(window4, text ="Clear", command=Clear).place(x=620,y=350)
    def Cancel():
       tkinter.messagebox.showinfo("Your form canceled")
    B3=Button(window4, text ="Cancel", command=lambda:[Cancel(),window4.destroy()]).place(x=670,y=350)
    window4.mainloop()
B7= Button(window, text ="Record for Book Returned By Student", command=s4).place(x=530,y=310)
def s5():
    window5=Tk()
    window5.geometry("1600x1500")
    window5.title("NMIMS SHIRPUR CAMPUS")
    window5.config(background='PINK')
    ourMessage="LIBRARY MANAGEMENT SYSTEM"
    newMessage="Deleting Student Detail"
    s=("Arial",25)
    m=("Arial",15)
    messageVar=Label(window5,text=ourMessage,font=s).place(x=450,y=0)
    messageVar=Label(window5,text=newMessage,font=m).place(x=600,y=80)
    l21=Label(window5,text='Enter Students SAP ID: ').place(x=490,y=150)
    e21=Entry(window5)
    e21.place(x=640,y=150)
    def Delete():
        print(e21.get())
        sap=e21.get()
        query='delete from student where sap_id = %s'
        data=(sap)
        try:
            Cur.execute(qwery,data)
            tkinter.messagebox.showinfo("success","Student Data Deleted")
            Cur.execute('select * from student')
            F()
        except mysql.connector.Error as lol:
            print('Error: {}'.format(lol)) 
        C()
    B2= Button(window5, text ="Delete", command=Delete).place(x=590,y=200)
    def Cancel():
       tkinter.messagebox.showinfo("Your form canceled")
    B3=Button(window5, text ="Cancel", command=lambda:[Cancel(),window5.destroy()]).place(x=670,y=200)
    window5.mainloop()
B8= Button(window, text ="Delete Student Detail", command=s5).place(x=530,y=360)

def s6():
    window6=Tk()
    window6.geometry("1600x1500")
    window6.title("NMIMS SHIRPUR CAMPUS")
    window6.config(background='PINK')
    ourMessage="LIBRARY MANAGEMENT SYSTEM"
    newMessage="Deleting Book Detail"
    s=("Arial",25)
    m=("Arial",15)
    messageVar=Label(window6,text=ourMessage,font=s).place(x=450,y=0)
    messageVar=Label(window6,text=newMessage,font=m).place(x=600,y=80)
    l22=Label(window6,text='Enter Book ID: ').place(x=490,y=150)
    e22=Entry(window6)
    e22.place(x=640,y=150)
    def Delete():
        print(e22.get())
        book=e22.get()
        query='delete from student where book_id = %s'
        data=(book)
        try:
            Cur.execute(qwery,data)
            tkinter.messagebox.showinfo("success","Book Data Deleted")
            Cur.execute('select * from book')
            F()
        except mysql.connector.Error as lol:
            print('Error: {}'.format(lol)) 
        C()
        B2= Button(window6, text ="Delete", command=Delete).place(x=590,y=200)
    def Cancel():
       tkinter.messagebox.showinfo("Your form canceled")
    B3=Button(window6, text ="Cancel", command=lambda:[Cancel(),window6.destroy()]).place(x=670,y=200)
    window6.mainloop()
B8= Button(window, text ="Delete Book Detail", command=s6).place(x=530,y=410)
window.mainloop()
