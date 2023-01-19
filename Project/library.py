from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk  # is used to style the tkinter widgets
import mysql.connector as mc
import tkinter.messagebox as mb
from tkcalendar import Calendar

class Library:
    def __init__(self, BottomFrame):
        self.BottomFrame = BottomFrame
        self.LibraryFrame = Frame(self.BottomFrame, pady=10, padx=50)
        self.LibraryFrame.grid(row=1, column=0, sticky='senw')
        self.img4 = Image.open("Images/open-book.png ")  # the  pass of the photo
        self.img4.thumbnail((200, 200))  # To cut the photo
        self.new_img4 = ImageTk.PhotoImage(self.img4)
        self.imgLibrary = Label(self.LibraryFrame, image=self.new_img4, padx=10, pady=10)
        self.imgLibrary.pack()
        self.buttonLibrary = Button(self.LibraryFrame, command=self.openLibraryWindow, font=('Tahoma', 10, 'bold'),
                                    text='Library Management', bg='#1b9ea4', fg='white', padx=10, pady=10)
        # the name of button And (background, font background)
        self.buttonLibrary.pack()

    def openLibraryWindow(self):  # A Function Used To open Library Window
        STDW = LibraryWindow()


# بتحبني ولا الهواء عمره ما زارك .

class LibraryWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Library Management System')
        self.master.geometry("1200x800+0+0")
        # # # # # # # # # #  Left Frame Inputs
        self.FrameLeft = Frame(self.master, width=400)
        self.FrameLeft.pack(side=LEFT, fill=Y)
        # # # # # # # # # # # # # ## # # ## # # # # ##
        self.NameLabel = Label(self.FrameLeft, text='Student Name', font=('tahoma', 12, 'bold'))
        self.NameLabel.place(x=15, y=20, width=120, height=40)
        self.PhoneLabel = Label(self.FrameLeft, text='Phone', font=('tahoma', 12, 'bold'))
        self.PhoneLabel.place(x=10, y=80, width=120, height=40)
        self.BookLabel = Label(self.FrameLeft, text='Book Name', font=('tahoma', 12, 'bold'))
        self.BookLabel.place(x=10, y=140, width=120, height=40)
        self.DateStudent = Label(self.FrameLeft, text='Delivery Data', font=('tahoma', 12, 'bold'))
        self.DateStudent.place(x=15, y=200, width=120, height=40)
        self.ReturnLabel = Label(self.FrameLeft, text='Return Data', font=('tahoma', 12, 'bold'))
        self.ReturnLabel.place(x=15, y=450, width=120, height=40)

        # The options of the Student window
        self.first = StringVar()
        self.Phone = StringVar()
        self.Book = StringVar()

        self.NameStudent = Entry(self.FrameLeft, text='Name', font=('tahoma', 12, 'bold'), textvariable=self.first)
        self.NameStudent.place(x=170, y=20, width=200, height=40)
        self.PhoneStudent = Entry(self.FrameLeft, text='Phone', font=('tahoma', 12, 'bold'), textvariable=self.Phone)
        self.PhoneStudent.place(x=170, y=80, width=200, height=40)
        self.BookStudent = Entry(self.FrameLeft, text='Book Name', font=('tahoma', 12, 'bold'), textvariable=self.Book)
        self.BookStudent.place(x=170, y=140, width=200, height=40)
        self.DeliveryDate = Calendar(self.FrameLeft, text='Delivery Data')
        self.DeliveryDate.place(x=170, y=200, width=200, height=200)
        self.ReturnDate = Calendar(self.FrameLeft, text='Return Data')
        self.ReturnDate.place(x=170, y=450, width=200, height=200)

        self.add = Button(self.FrameLeft, text='Add', command=self.add)  # The Add Button
        self.add.place(x=20, y=700, width=60, height=60)
        self.add = Button(self.FrameLeft, command=self.update, text='Update')  # The Update Button
        self.add.place(x=100, y=700, width=60, height=60)
        self.add = Button(self.FrameLeft, text='Delete', command=self.delete)  # The Delete Button
        self.add.place(x=180, y=700, width=60, height=60)
        self.Read = Button(self.FrameLeft, command=self.read, text='Show')  # The Delete Button
        self.Read.place(x=260, y=700, width=60, height=60)
        self.reset = Button(self.FrameLeft, command=self.Reset, text='Reset')  # The Delete Button
        self.reset.place(x=340, y=700, width=60, height=60)

        # # # # # # # # # # # #     The beginning of RightFrame   # # # # # # # # # # #

        self.FrameRight = Frame(self.master, width=800)  # the right frame of student Button.
        self.FrameRight.pack(side=LEFT, fill=BOTH)
        # # # # # # # # # # # #     The End of RightFrame   # # # # # # # # # # #
        self.FrameRightTop = Frame(self.FrameRight, height=50, padx=5, pady=5)

        self.SearchStudent = Entry(self.FrameRightTop, fg='#4F4F4F', font=('tahoma', 12, 'bold'), width=80)
        self.SearchStudent.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)  # to get away from the FrameRightTop
        self.buttonSearch = Button(self.FrameRightTop, command=self.Search, text='Search', fg='#4F4F4F',
                                   font=('tahoma', 12, 'bold'), width=50)
        self.buttonSearch.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        self.FrameRightTop.grid_columnconfigure(0, weight=1)
        self.FrameRightTop.grid_columnconfigure(1, weight=1)

        self.FrameRightTop.pack()

        # # # # # # # # # # # # # # # #  Frame Tree View # # # # # # # # # # # #
        self.FrameView = Frame(self.FrameRight, bg='blue')
        self.FrameView.pack(fill=BOTH)
        self.table = ttk.Treeview(self.FrameView,
                                  columns=("id", "Name", "Phone", "Book Name", "Delivery data", "Return data"),
                                  show='headings')

        self.table.pack(fill=BOTH)
        self.table.heading("id", text='id')
        self.table.heading("Name", text='Name')
        self.table.heading("Phone", text='Phone')
        self.table.heading("Book Name", text='Book Name')
        self.table.heading("Delivery data", text='Delivery data')
        self.table.heading("Return data", text="Return data")

        self.table.column("Name", anchor=W, width=10)
        self.table.column("Phone", anchor=W)  # (w) to let the be shown at left.
        self.table.column("Book Name", anchor=W)
        self.table.column("Delivery data", anchor=W)
        self.table.column("Return data", anchor=W)
        self.read()
        self.table.bind("<ButtonRelease>", self.show)


    def add(self):
        Mydb = mc.connect(  # local variable.
            host='localhost',
            username='root',
            password='',
            database='university'
        )
        n = 10000000
        for i in range(0, n):
            self.id_n=i

            Mycursor = Mydb.cursor()
            MYSQL = "insert into  library2(id,StudentName,Phone,Book,DeliveryDate,ReturnDate) values (%s,%s,%s,%s,%s,%s)"
            if (len(self.NameStudent.get()) == 0 or len(self.PhoneStudent.get()) == 0 or len(
                 self.BookStudent.get()) == 0 or len(self.DeliveryDate.get_date()) == 0 or len(
                 self.ReturnDate.get_date()) == 0):
                mb.showerror("Error", 'All Data Should Be Required',
                         parent=self.master)  # used to tell thw user to insert all data.
            else:
                value = (self.id_n, self.NameStudent.get(), self.PhoneStudent.get(), self.BookStudent.get(),
                        self.DeliveryDate.get_date(), self.ReturnDate.get_date())
                Mycursor.execute(MYSQL, value)

                Mydb.commit()
                Mydb.close()
                mb.showinfo('Successfully added ', 'Data Inserted Successfully ',
                           parent=self.master)  # a fun used for tell the user the Successfully inserst.
                # A parent used to show this(Data Inserted Successfully) in student window
                self.NameStudent.delete(0, 'end')  # to empty the place after insert the data
                self.PhoneStudent.delete(0, 'end')  # to empty the place after insert the data
                self.BookStudent.delete(0, 'end')  # to empty the place after insert the data
                # self.DeliveryStudent.delete(0, 'end')
                # to empty the place after insert the data

                # self.ReturnStudent.delete(0, 'end')
                Mydb.close()

                self.read()
                i+=1



    def read(self):
        Mydb = mc.connect(  # local variable.
            host='localhost',
            username='root',
            password='',
            database='university'
        )
        mycursor = Mydb.cursor()
        sql = "select * from library2"
        mycursor.execute(sql)
        MyResults = mycursor.fetchall()  # used to print all id's and put all data.
        self.table.delete(*self.table.get_children())  # to get all data and delete the old data.
        for res in MyResults:
            self.table.insert('', 'end', iid=res[0], values=res)
            Mydb.commit()
        Mydb.close()

    def show(self, ev):
        self.iid = self.table.focus()
        AllData = self.table.item(self.iid)
        val = AllData['values']
        self.first.set(val[1])
        self.Phone.set(val[2])
        self.Book.set(val[3])

    def Reset(self):
        self.NameStudent.delete(0, 'end')
        self.PhoneStudent.delete(0, 'end')
        self.BookStudent.delete(0, 'end')


    def delete(self):
        Mydb = mc.connect(  # local variable.
            host='localhost',
            username='root',
            password='',
            database='university'
        )
        mycursor = Mydb.cursor()
        sql = "delete from library2 where id=" + self.iid
        mycursor.execute(sql)
        Mydb.commit()
        mb.showinfo('Delete', 'The Student has been deleted', parent=self.master)
        self.read()  # to update the table after delete the student.
        self.Reset()

    def update(self):
        Mydb = mc.connect(  # local variable.
            host='localhost',
            username='root',
            password='',
            database='university'
        )
        mycursor = Mydb.cursor()
        sql = ("update library2 set StudentName=%s, Phone=%s, Book=%s, DeliveryDate=%s where ReturnDate=%s")
        VAL = (self.first.get(), self.Phone.get(), self.Book.get(), self.iid)
        mycursor.execute(sql, VAL)
        Mydb.commit()
        mb.showinfo('Update', 'The Student has been Updated', parent=self.master)
        self.read()  # to update the table after Update the student.
        self.Reset()

    def Search(self):
        Mydb = mc.connect(  # local variable.
            host='localhost',
            username='root',
            password='',
            database='university'
        )
        mycursor = Mydb.cursor()
        sql = ("select * from student where id" + self.SearchStudent.get())
        mycursor.execute(sql)
        MyResults = mycursor.fetchone()  # used to print all id's and put all data.
        self.table.delete(*self.table.get_children())
        self.table.insert('', 'end', iid=MyResults[0], values=MyResults)
        Mydb.commit()
        Mydb.close()
