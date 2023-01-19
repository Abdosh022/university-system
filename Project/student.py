from tkinter import *
from tkinter import ttk      # is used to style the tkinter widgets
from PIL import Image, ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb

class Student:
    def __init__(self, CenterFrame):
        self.CenterFrame = CenterFrame
        self.StudentFrame = Frame(self.CenterFrame, pady=10, padx=10)
        self.StudentFrame.grid(row=0, column=1, sticky='senw')
        self.img2 = Image.open("Images/studenticon.png")  # the  pass of the photo
        self.img2.thumbnail((200, 200))  # To cut the photo
        self.new_img2 = ImageTk.PhotoImage(self.img2)
        self.imgStudent = Label(self.StudentFrame, image=self.new_img2, padx=10, pady=10)
        self.imgStudent.pack()
        self.buttonStudent = Button(self.StudentFrame, command=self.openStudentWindow, text='Student Management',
                                    font=('Tahoma', 10, 'bold'), bg='#1b9ea4', fg='white', padx=10, pady=10)
        # the name of button And (background, font background)
        self.buttonStudent.pack()

    def openStudentWindow(self):  # A Function Used To open University Window
       STDW =StudentWindow()

# انا اتوووب عن حبك انا , انا ليا في بعدك هنا

class StudentWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Student Management System')
        self.master.geometry("1200x600+0+0")
        # # # # # # # # # #  Left Frame Inputs
        self.FrameLeft = Frame(self.master, width=300)
        self.FrameLeft.pack(side=LEFT, fill=Y)
        # # # # # # # # # # # # # ## # # ## # # # # ##
        self.FirstName = Label(self.FrameLeft, text='First Name',  font=('tahoma', 10, 'bold'))
        self.FirstName.place(x=10, y=20)
        self.LastName = Label(self.FrameLeft, text='Last Name', font=('tahoma', 10, 'bold'))
        self.LastName.place(x=10, y=50)
        self.ID = Label(self.FrameLeft, text='ID', font=('tahoma', 10, 'bold'))
        self.ID.place(x=10, y=80)
        self.Email = Label(self.FrameLeft, text='Email', font=('tahoma', 10, 'bold'))
        self.Email.place(x=10, y=110)
        # The options of the Student window
        self.first = StringVar()
        self.last = StringVar()                # to convert the data that the user enter it to string.
        self.id = StringVar()
        self.email = StringVar()
        self.FirstName = Entry(self.FrameLeft, text='First Name', textvariable=self.first)
        self.FirstName.place(x=100, y=20)
        self.LastName = Entry(self.FrameLeft, text='Last Name', textvariable=self.last)
        self.LastName.place(x=100, y=50)
        self.ID = Entry(self.FrameLeft, text='ID', textvariable=self.id)
        self.ID.place(x=100, y=80)
        self.Email = Entry(self.FrameLeft, text='Email', textvariable=self.email)
        self.Email.place(x=100, y=110)

        self.add = Button(self.FrameLeft, text='Add', command=self.add)              # The Add Button
        self.add.place(x=10, y=300)
        self.add = Button(self.FrameLeft, command=self.update, text='Update')           # The Update Button
        self.add.place(x=60, y=300)
        self.add = Button(self.FrameLeft, text='Delete', command=self.delete)           # The Delete Button
        self.add.place(x=120, y=300)
        self.Read = Button(self.FrameLeft, command=self.read, text='Show')  # The Delete Button
        self.Read.place(x=180, y=300)
        self.reset = Button(self.FrameLeft, command=self.Reset, text='Reset')  # The Delete Button
        self.reset.place(x=240, y=300)


        # # # # # # # # # # # #     The beginning of RightFrame   # # # # # # # # # # #

        self.FrameRight = Frame(self.master, width=800)       # the right frame of student Button.
        self.FrameRight.pack(side=LEFT, fill=BOTH)
        # # # # # # # # # # # #     The End of RightFrame   # # # # # # # # # # #
        self.FrameRightTop = Frame(self.FrameRight, height=50, padx=5, pady=5)

        self.SearchStudent = Entry(self.FrameRightTop, fg='#4F4F4F', font=('tahoma', 12, 'bold'), width=80)
        self.SearchStudent.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)  # to get away from the FrameRightTop
        self.buttonSearch = Button(self.FrameRightTop, command=self.Search, text='Search', fg='#4F4F4F', font=('tahoma', 12, 'bold'), width=50)
        self.buttonSearch.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        self.FrameRightTop.grid_columnconfigure(0, weight=1)
        self.FrameRightTop.grid_columnconfigure(1, weight=1)

        self.FrameRightTop.pack()

        # # # # # # # # # # # # # # # #  Frame Tree View # # # # # # # # # # # #
        self.FrameView = Frame(self.FrameRight, bg='blue')
        self.FrameView.pack(fill=BOTH)
        self.table = ttk.Treeview(self.FrameView, columns=("ID", "FirstName", "LastName", "Email"), show='headings')

        self.table.pack(fill=BOTH)
        self.table.heading("ID", text='ID')
        self.table.heading("FirstName", text='FirstName')
        self.table.heading("LastName", text='LastName')
        self.table.heading("Email", text='Email')

        self.table.column("ID", anchor=W, width=10)
        self.table.column("FirstName", anchor=W)                     # (w) to let the be shown at left.
        self.table.column("LastName", anchor=W)
        self.table.column("Email", anchor=W)
        self.read()
        self.table.bind("<ButtonRelease>", self.show)
    def add(self):
        Mydb = mc.connect(                                 # local variable.
            host='localhost',
            username='root',
            password='',
            database='university'
        )
        mycursor = Mydb.cursor()
        sql = "insert into  student (FirstName,LastName,Email,ID) values (%s,%s,%s,%s)"
        if (len(self.FirstName.get())==0 or len(self.LastName.get())==0  or len(self.Email.get())==0  or len(self.ID.get())== 0):
            mb.showerror("Error", 'All Data Should Be Required', parent=self.master)     # used to tell thw user to insert all data.
        else:
            val = (self.FirstName.get(), self.LastName.get(), self.Email.get(), self.ID.get())
            mycursor.execute(sql, val)
            Mydb.commit()
            Mydb.close()
            mb.showinfo('Successfully added ', 'Data Inserted Successfully ', parent=self.master)       # a fun used for tell the user the Successfully inserst.
            # A parent used to show this(Data Inserted Successfully) in student window
            self.FirstName.delete(0, 'end')         # to empty the place after insert the data
            self.LastName.delete(0, 'end')            # to empty the place after insert the data
            self.ID.delete(0, 'end')                   # to empty the place after insert the data
            self.Email.delete(0, 'end')                 # to empty the place after insert the data

            self.read()

    def read(self):
        Mydb = mc.connect(  # local variable.
            host='localhost',
            username='root',
            password='',
            database='university'
        )
        mycursor = Mydb.cursor()
        sql = "select * from student"
        mycursor.execute(sql)
        MyResults = mycursor.fetchall()                 # used to print all id's and put all data.
        self.table.delete(*self.table.get_children())     # to get all data and delete the old data.
        for res in MyResults:
            self.table.insert('', 'end', iid=res[0], values=res)
            Mydb.commit()
        Mydb.close()
    def show(self, ev):
        self.iid = self.table.focus()
        AllData = self.table.item(self.iid)
        val = AllData['values']
        self.first.set(val[0])
        self.last.set(val[1])
        self.id.set(val[2])
        self.email.set(val[3])


    def Reset(self):
        self.FirstName.delete(0, 'end')
        self.LastName.delete(0, 'end')
        self.ID.delete(0, 'end')
        self.Email.delete(0, 'end')
    def delete(self):
        Mydb = mc.connect(  # local variable.
            host='localhost',
            username='root',
            password='',
            database='university'
        )
        mycursor = Mydb.cursor()
        sql = "delete from student where id="+self.iid
        mycursor.execute(sql)
        Mydb.commit()
        mb.showinfo('Delete', 'The Student has been deleted', parent=self.master)
        self.read()           # to update the table after delete the student.
        self.Reset()

    def update(self):
        Mydb = mc.connect(  # local variable.
            host='localhost',
            username='root',
            password='',
            database='university'
        )
        mycursor = Mydb.cursor()
        sql = ("update student set Id=%s, FirstName=%s, LastName=%s, Email=%s where id=%s")
        VAL = (self.first.get(), self.last.get(), self.id.get(), self.email.get(), self.iid)
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
        sql = ("select * from student where id"+self.SearchStudent.get())
        mycursor.execute(sql)
        MyResults = mycursor.fetchone()  # used to print all id's and put all data.
        self.table.delete(*self.table.get_children())
        self.table.insert('', 'end', iid=MyResults[0], values=MyResults)
        Mydb.commit()
        Mydb.close()



