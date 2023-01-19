import mysql.connector as mc
import tkinter.messagebox as mb
from tkinter import *                                # For every thing in tiknter library.
from PIL import Image, ImageTk                       # To bring the pictures
import University as uni                                  # for A Student Class
import Student as s                                  # for A Student Class
import Library as lib
import Staff as st
import Exam as ex


class UniversityManagement:
    def __init__(self, mast):
        self.master = mast                 # instance of class
        self.master.title("Student Management System ")   # To write the title.
        self.width = self.master.winfo_screenwidth()      # To let program enter my width
        self.height = self.master.winfo_screenheight()     # To let program enter my height
        self.master.geometry("{w}x{h}+0+0".format(w=self.width, h=self.height))          # To calculate the dimensions.
        self.master.resizable(True, True)                                  # To control max and min in length and width
        # # # # # # # # # # # #     The beginning of FrameTop     # # # # # # # # # # # #
        self.FrameTop = Frame(self.master, bg='#1b9ea4', height=150 )    # to create background of the frame
        self.FrameTop.pack(fill=X)            # To let the FrameTop be shown
        self.UMS = Label(self.FrameTop, text='University Management System', bg='#1b9ea4', fg='White', font=('Tahoma', 30), pady=50)
        # To create (text,background,font background,font)
        self.UMS.pack()                          # TO let the label be shown
        self.buttonLogout = Button(self.FrameTop, text='Exit', command=self.logout)
        self.buttonLogout.pack()

        # # # # # # # # # # # #     The beginning of CenterFrame   # # # # # # # # # # #
        self.CenterFrame = Frame(self.master, height=200)
        self.CenterFrame.pack(fill=X)           # # To let the CenterFrame be shown

        # # # # Frame University info     # # # # # # # # # # # #
        un = uni.University(self.CenterFrame)           # A Object Used To open University Window

        # # # # # # # # # # # #     Frame Student info     # # # # # # # # # # # #
        std = s.Student(self.CenterFrame)             # A Object Used To open Student Window

        # # # # # # # # # #   Staff info     # # # # # # # # # # # #
        stf = st.Staff(self.CenterFrame)                  # A Object Used To open Staff Window

        # # # # # # # # # # # #     The beginning of Bottom Frame     # # # # # # # # # # # #
        self.BottomFrame = Frame(self.master, height=200)
        self.BottomFrame.pack(fill=X)  # # To let the BottomFrame be shown

        # # # # # # # # # # # #     Frame Library info     # # # # # # # # # # #
        libra = lib.Library(self.BottomFrame)           # A Object Used To open Library Window

        # # # # # # # # # # # #     Frame Exam info     # # # # # # # # # # #
        exam = ex.Exam(self.BottomFrame)             # A Object Used To open Exam Window

    def logout(self):
        self.master.destroy()

class Login:
    def __init__(self, Window):
        self.master =window                  # instance of class
        self.master.title("Login System ")   # To write the title.
        self.master.geometry("500x500+150+150")         # To calculate the dimensions.
        self.img = Image.open('images/loginImage.png')
        self.img.thumbnail((200, 200))  # To cut the photo
        self.new_img2 = ImageTk.PhotoImage(self.img)
        self.imgStudent = Label(self.master, image=self.new_img2, padx=10, pady=10)
        self.imgStudent.pack()
        self.FrameLogin = Frame(self.master)
        self.FrameLogin.pack()
        self.LabelUser = Label(self.FrameLogin, text='User Name', pady=10, padx=10, font=('Tahoma',10,'bold'))
        self.LabelUser.grid(row=0, column=0)
        self.LabelPass = Label(self.FrameLogin, text='Password', pady=10, padx=10, font=('Tahoma',10,'bold'))
        self.LabelPass.grid(row=1, column=0)
        self.username = Entry(self.FrameLogin, font=('Tahoma', 10, 'bold'))
        self.username.grid(row=0, column=1, pady=10, padx=10)
        self.password = Entry(self.FrameLogin, font=('Tahoma', 10, 'bold'), show="*")
        self.password.grid(row=1, column=1, pady=10, padx=10)
        self.LoginButton = Button(self.FrameLogin, command=self.login, text='Login', font=('Tahoma', 10, 'bold'), bg='#1b9ea4', fg='white')
        self.LoginButton.grid(row=2, column=0, columnspan=2, sticky='snew', pady=10, padx=10)



    def login(self):
        try:
           Mydb = mc.connect(  # local variable.
           host='localhost',
           username='root',
           password='',
           database='university'
           )

           mycursor = Mydb.cursor()
           sql = "select * from loginadmin where Username='"+self.username.get()+"' and Password= '"+self.password.get()+"'"
           mycursor.execute(sql)
           res = mycursor.fetchone()
           if(res == None):
              mb.showerror('Failed Login', 'Invalid Username or Password ! please Try again')
           else:
              win = Toplevel()
              Window = UniversityManagement(win)
        except:
           mb.showerror('Failed connection', "Please Open Your SQL Server")




if (__name__=='__main__'):
    window = Tk()                    # (window is the name of program )
    Std = Login(window)            # Std is a object
    mainloop()

