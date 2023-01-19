from tkinter import *
from PIL import Image, ImageTk


class University:
    def __init__(self, CenterFrame):
        self.CenterFrame = CenterFrame
        self.UniversityInfo = Frame(self.CenterFrame, pady=10, padx=10)
        self.UniversityInfo.grid(row=0, column=0, sticky='senw')
        self.img = Image.open("Images/university.png")  # the  pass of the photo
        self.img.thumbnail((200, 200))  # To cut the photo
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgUniversity = Label(self.UniversityInfo, image=self.new_img, padx=10, pady=10)
        self.imgUniversity.pack()
        self.buttonUniversity = Button(self.UniversityInfo, command=self.openUniversityWindow, text='About University',
                                       font=('Tahoma', 10, 'bold'), bg='#1b9ea4', fg='white', padx=10, pady=10)
        # the name of button And (background, font background)
        self.buttonUniversity.pack()

    def openUniversityWindow(self):  # A Function Used To open University Window
        info = UniversityWindow()


class UniversityWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('University Management System')
        self.master.geometry("1200x650+0+0")
        self.TitleLAbel = Label(self.master, text="Higher Technological Institute/CS", bg='#1b9ea4', pady=70, fg='white', font=('Tahoma', 30, 'bold'))
        self.TitleLAbel.pack(fill=X)
        self.txt = StringVar()
        self.message = Message(self.master, textvariable=self.txt, justify=CENTER, font=('Tahoma', 10))
        self.message.pack()
        self.txt.set("   The institute adopts the credit hours system, which gives the student the opportunity to study at his own pace & his/her own abilities. Unlike the usual fixed format teaching being fo11owed by Egyptian universities, the credit-hour system enables the student to select a number of courses from a well - planned academic program.\n"
                     
                     
                     " The program provides a variety of courses some of which are geared to a specific major, some are general and cultural in nature the rest are electives to enhance one's major. The system ensures that the slow learner does net hold back the advanced student. The advanced student is permitted to choose more courses and when he/she fulfills the requirements of the degree, he/she may graduate earlier than other students. Each student is assigned an academic advisor who guides him/her in planning his/her study program, monitor his progress, and help solve any problems he/she may encounter. The system encourages the student to develop independent thinking, gives him/her enough time to widen his scope of interest, and trains him/her to search for information through the use of the library and other learning facilities.\n"
                     " At HTI, a student may study for a diploma or a bachelor's degree depending on the program he selects. To earn an engineering diploma he/she should complete 120-credit hours, which requires at least about three year of study. If he/she wants to fulfill the requirements of a B.Sc in engineering in one of the majors offered, then he/she has to complete an additional 80 credit hours, which require about two more years of academic study. The academic year is divided into three semesters. The first two semesters are academic instruction - 15 weeps each, and the third is devoted to practical training -10 weeks, at one of the factories or project sites at Tenth of Ramadan City, the Sixth of October City, and other locations throughout Egypt or abroad. Practical training is done under the supervision of academic staff. Such a program combines academic class work with technology, a combination that is needed in Egypt and in the Arab World. A student may also select a Technology Management and Information program or Computer Science program. To get a diploma he/she must complete 80 credit units. For a Bachelor's degree he/she has to finish an additional 80 credit hours. Like engineering students a technology management student or computer Science student must complete two academic semesters per year and a third one will be devoted to practical training")


















