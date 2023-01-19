from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk      # is used to style the tkinter widgets
import mysql.connector as mc
import tkinter.messagebox as mb

class Staff:
    def __init__(self, CenterFrame):
        self.CenterFrame = CenterFrame
        self.StaffFrame = Frame(self.CenterFrame, pady=10, padx=10)
        self.StaffFrame.grid(row=0, column=2, sticky='senw')
        self.img3 = Image.open("Images/staff.png")  # the  pass of the photo
        self.img3.thumbnail((200, 200))  # To cut the photo
        self.new_img3 = ImageTk.PhotoImage(self.img3)
        self.imgStaff = Label(self.StaffFrame, image=self.new_img3, padx=10, pady=10)
        self.imgStaff.pack()
        self.buttonStaff = Button(self.StaffFrame, command=self.openStaffWindow, text='Staff Management',
                                  font=('Tahoma', 10, 'bold'), bg='#1b9ea4', fg='white', padx=10, pady=10)
        # the name of button And (background, font background)
        self.buttonStaff.pack()
        self.CenterFrame.grid_columnconfigure(0, weight=1)
        self.CenterFrame.grid_columnconfigure(1, weight=1)
        self.CenterFrame.grid_columnconfigure(2, weight=1)

    def openStaffWindow(self):  # A Function Used To open StaffWindow
        STDW = StaffWindow()          # A Object Used To open StaffWindow

class StaffWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Staff Management System')
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
        self.job = Label(self.FrameLeft, text='job', font=('tahoma', 10, 'bold'))
        self.job.place(x=10, y=140)
        self.Phone = Label(self.FrameLeft, text='Phone', font=('tahoma', 10, 'bold'))
        self.Phone.place(x=10, y=170)
        # The options of the Student window
        self.first = StringVar()
        self.last = StringVar()
        self.id = StringVar()
        self.email = StringVar()
        self.job = StringVar()
        self.Phone = StringVar()
        self.FirstName = Entry(self.FrameLeft, text='First Name', textvariable=self.first)
        self.FirstName.place(x=100, y=20)
        self.LastName = Entry(self.FrameLeft, text='Last Name', textvariable=self.last)
        self.LastName.place(x=100, y=50)
        self.ID = Entry(self.FrameLeft, text='ID', textvariable=self.id)
        self.ID.place(x=100, y=80)
        self.Email = Entry(self.FrameLeft, text='Email', textvariable=self.email)
        self.Email.place(x=100, y=110)
        self.job = ttk.Combobox(self.FrameLeft, values=["", "Employee", "professor", "Technician", "Teaching Assistant"], state='readonly',textvariable=self.job)
        # A state used to make job read only.
        self.job.place(x=100, y=140)
        self.Phone = Entry(self.FrameLeft, text='Phone', textvariable=self.Phone)
        self.Phone.place(x=100, y=170)


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
        self.table = ttk.Treeview(self.FrameView, columns=("FirstName", "LastName", "ID", "Email", "job", "Phone"),show='headings')
        self.table.pack(fill=BOTH)
        self.table.heading("FirstName", text='FirstName')
        self.table.heading("LastName", text='LastName')
        self.table.heading("ID", text='ID')
        self.table.heading("Email", text='Email')
        self.table.heading("job", text='job')
        self.table.heading("Phone", text='Phone')

        self.table.column("FirstName", anchor=W, width=30)
        self.table.column("LastName", anchor=W, width=30)                     # (w) to let the be shown at left.
        self.table.column("ID", anchor=W, width=7)
        self.table.column("Email", anchor=W, width=30)
        self.table.column("job", anchor=W, width=30)
        self.table.column("Phone", anchor=W, width=30)
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
        sql = "insert into  staff (FirstName,LastName,Email,ID,job,Phone) values (%s,%s,%s,%s,%s,%s)"
        if (len(self.FirstName.get())==0 or len(self.LastName.get())==0  or len(self.Email.get())==0  or len(self.ID.get())== 0 or len(self.job.get())==0 or len(self.Phone.get())==0):
            mb.showerror("Error", 'All Data Should Be Required', parent=self.master)     # used to tell thw user to insert all data.
        else:
            val = (self.FirstName.get(), self.LastName.get(), self.Email.get(), self.ID.get(), self.job.get(), self.Phone.get() )
            mycursor.execute(sql, val)
            Mydb.commit()
            Mydb.close()
            mb.showinfo('Successfully added ', 'Data Inserted Successfully ', parent=self.master)       # a fun used for tell the user the Successfully inserst.
            # A parent used to show this(Data Inserted Successfully) in student window
            self.Reset()
            self.read()

    def read(self):
        Mydb = mc.connect(  # local variable.
            host='localhost',
            username='root',
            password='',
            database='university'
        )
        mycursor = Mydb.cursor()
        sql = "select * from staff"
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
        self.job.set(val[4])
        self.Phone.set(val[5])



    def Reset(self):
        self.FirstName.delete(0, 'end')
        self.LastName.delete(0, 'end')
        self.ID.delete(0, 'end')
        self.Email.delete(0, 'end')
        self.job.current(0)
        self.Phone.delete(0, 'end')

    def delete(self):
        Mydb = mc.connect(  # local variable.
            host='localhost',
            username='root',
            password='',
            database='university'
        )
        mycursor = Mydb.cursor()
        sql = "delete from staff where id="+self.iid
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
        sql = ("update staff set Id=%s, FirstName=%s, LastName=%s, Email=%s, job=%s, Phone=%s where id=%s")
        VAL = (self.first.get(), self.last.get(), self.id.get(), self.email.get(), self.job.get(), self.Phone.get(), self.iid)
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
        sql = ("select * from staff where id"+self.SearchStudent.get())
        mycursor.execute(sql)
        MyResults = mycursor.fetchone()  # used to print all id's and put all data.
        self.table.delete(*self.table.get_children())
        self.table.insert('', 'end', iid=MyResults[0], values=MyResults)
        Mydb.commit()
        Mydb.close()
