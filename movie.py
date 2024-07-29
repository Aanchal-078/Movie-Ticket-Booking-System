from tkinter import *
from tkinter import font, PhotoImage
import tkinter.messagebox as tm
import mysql.connector as c
conn = c.connect(user='root', password="", database='movie')
from PIL import Image, ImageTk
class TicketBooking:
    def __init__(self, parent):
        self.parent = parent
        self.main()
    
    def main(self):
        # Displaying the main page where user can choose to login or signup
        self.parent.title("Online movie ticket ")
        self.parent.geometry("600x400")
        # Setting background to the screen
        self.image_path = Image.open("D:/brilliko/python/Tkinter/movie1.jpg")
        self.bg_image = ImageTk.PhotoImage(self.image_path)
        bg_label = Label(self.parent, image=self.bg_image)
        bg_label.place(relheight=1, relwidth=1)
        self.heading_font = font.Font(family='Palatino', size=40, weight="bold")
        self.custom_font = font.Font(family='Times New Roman', size=16)
        #Displaying the labels and buttons on the screen
        Label(self.parent, text="PVR CINEMAS", font=self.heading_font, bg='Black',fg='Red').place(x=130, y=150)
        Button(self.parent, text='Sign Up', bg='Black',fg='White', font=self.custom_font, command=self.signup).place(x=390, y=10)
        Button(self.parent, text='Login ', bg='Black', fg='White', font=self.custom_font, command=self.login).place(x=500, y=10)
    
    def signup(self):
        # Destroying previous screen and creating new screen
        self.parent.destroy()
        self.parent = Tk()
        self.parent.title("SIGN UP FORM")
        self.parent.geometry("520x550")
        self.parent.configure(bg='Black')
        self.custom1 = font.Font(family='Times New Roman', size=12)
        self.image_path2 = Image.open("D:/brilliko/python/Tkinter/movie2.jpg")
        self.bg_image2 = ImageTk.PhotoImage(self.image_path2)
        bg_label2 = Label(self.parent, image=self.bg_image2)
        bg_label2.place(relheight=0.5, relwidth=1)
        self.custom = font.Font(family='Gregorian', size=18, weight='bold')
        Button(self.parent, text='<- Back', bg='Black', font=self.custom1, fg='White', command=self.main).place(x=10, y=10)
        Label(self.parent, text='Mobile No: ', bg='Black', fg='White', font=self.custom).place(x=20, y=300)
        # Taking user input using Entry widget
        self.txts1 = Entry(self.parent, font=self.custom_font, width=30)
        self.txts1.place(x=200, y=305)
        Label(self.parent, text='Full Name: ' , bg='Black', fg='White', font=self.custom ).place(x=20, y=350)
        self.txts2 = Entry(self.parent, font=self.custom_font, width=30)
        self.txts2.place(x=200, y=355)
        Label(self.parent, text='Username: ', bg='Black', fg='White', font=self.custom ).place(x=20, y=400)
        self.txts3 = Entry(self.parent, font=self.custom_font, width=30)
        self.txts3.place(x=200, y=405)
        Label(self.parent, text='Password: ' , bg='Black', fg='White', font=self.custom ).place(x=20, y=450)
        self.txts4 = Entry(self.parent, font=self.custom_font, width=30, show='*')
        self.txts4.place(x=200, y=455)
        self.show_password_var = BooleanVar()
        self.show_password_check = Checkbutton(self.parent, text='Show Password', bg='Black', fg='White', font=self.custom_font, variable=self.show_password_var, command=self.toggle_password)
        self.show_password_check.place(x=30, y=500)
        
        Button(self.parent, text='Sign In', bg='Black', fg='White', font=self.custom_font, command=self.add_data).place(x=420, y=500)
    
    # Displaying error messagebox where some error occur
    def error_signup(self):
        tm.showinfo("Error", "Username already exist!!!")
    
    def error_login(self):
        tm.showinfo("Error", "Invalid Credentials!!!")
    
    def error_login1(self):
        tm.showinfo("Error", "Username doesn't exist!!!")

    def toggle_password(self):
        if self.show_password_var.get():
            self.txts4.config(show='')
        else:
            self.txts4.config(show='*')

    def add_data(self):
        mobile = self.txts1.get()
        fullname = self.txts2.get()
        name = self.txts3.get()
        password = self.txts4.get()
        # Inserting data into database after user sign in. So that there data must be saved
        sql = 'select name from signup where name = %s'
        data=(name,)
        myc = conn.cursor()
        myc.execute(sql,data)
        res = myc.fetchall()
        result = ', '.join(str(i[0]) for i in res)
        if name in result:
            # If user already exist it will show an error
            self.error_signup()
        else:
            # If user doesn't exist it will insert data into database
            sql = 'insert into signup values(%s,%s,%s,%s)'
            data=(mobile, fullname, name, password)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
            self.login()

    def login(self):
        # Displaying the login window and taking user input to login into the system
        self.parent.destroy()
        self.parent = Tk()
        self.parent.title("LOGIN FORM")
        self.parent.configure(bg='Black')
        self.parent.geometry("800x400")
        self.heading_font = font.Font(family='Palatino', size=40, weight="bold")
        self.custom = font.Font(family='Gregorian', size=18)
        self.custom1 = font.Font(family='Times New Roman', size=12)
        self.image_path3 = Image.open("D:/brilliko/python/Tkinter/login2.jpg")
        self.bg_image3 = ImageTk.PhotoImage(self.image_path3)
        bg_label3 = Label(self.parent, image=self.bg_image3)
        bg_label3.place(relheight=1, relwidth=0.5)
        Label(self.parent, text='USER LOGIN', fg='#5885FF', bg='Black', font=self.heading_font).place(x=430, y=40)
        Label(self.parent, text='Username: ', bg='Black', font=self.custom, fg='White' ).place(x=420, y=140)
        self.txtl1 = Entry(self.parent, font=self.custom_font, width=25)
        self.txtl1.place(x=550, y=145)
        Label(self.parent, text='Password: ', font=self.custom, bg='Black', fg='White').place(x=420, y=190)
        self.txtl2 = Entry(self.parent, font=self.custom_font, width=25, show='*')
        self.txtl2.place(x=550, y=195)
        Button(self.parent, text='<- Back', bg='Black', font=self.custom1, fg='White', command=self.main).place(x=10, y=10)
        Button(self.parent, text='Login', bg='#5885FF', fg='White', width=25, font=self.custom, command=self.chk_data).place(x=430, y=260)

    def chk_data(self):
        name = self.txtl1.get()
        password = self.txtl2.get()
        # Fetching user details from database
        sql = 'select name, password, fullname from signup where name = %s'
        data=(name,)
        myc = conn.cursor()
        myc.execute(sql,data)
        res = myc.fetchall()
        n = ', '.join(str(i[0]) for i in res)
        p = ', '.join(str(i[1]) for i in res)
        f = ', '.join(str(i[2]) for i in res)
        # If user data exist it will successfully login otherwise it will show the error message boxes
        if(n==name and p!=password or n!=name and p==password):
            self.error_login()
        elif(name=="" and password==""):
            self.error_login1()
        else:
            self.name = name
            self.fullname = f
            self.movie_slc()
    
    # In this function user will be able to select city and movie
    def movie_slc(self):
        self.parent.destroy()
        self.parent = Tk()
        self.parent.title("MOVIE TICKET BOOKING")
        self.parent.geometry("920x560")
        self.heading_font = font.Font(family='Palatino', size=40, weight="bold")
        self.custom = font.Font(family='Gregorian', size=18)
        self.custom1 = font.Font(family='Times New Roman', size=14)
        self.city_var = StringVar()
        self.city_var.set("Select City")
        self.city_dropdown = OptionMenu(self.parent, self.city_var, "Ambala", "Ludhiana", "Chandigarh", "Haridwar", "Patiala", "Kharar", "Mohali", "Amritsar","Jalandhar")
        self.city_dropdown.config( font=font.Font(family='Times New Roman', size=16))
        self.city_dropdown.place(x=760, y=10)
        self.image_path4 = Image.open("D:/brilliko/python/Tkinter/mv1.jpg")
        self.bg_image4 = ImageTk.PhotoImage(self.image_path4)
        self.image_path5 = Image.open("D:/brilliko/python/Tkinter/mv2.jpg")
        self.bg_image5 = ImageTk.PhotoImage(self.image_path5)
        self.image_path6 = Image.open("D:/brilliko/python/Tkinter/mv3.jpg")
        self.bg_image6 = ImageTk.PhotoImage(self.image_path6)
        Label(self.parent, text='BOOKING TICKET', font=self.heading_font).place(x=200, y=0)
        Button(self.parent, text='Logout', font=self.custom1, command=self.main).place(x=10, y=10)
        Button(self.parent, height=30, width=40, image=self.bg_image4, command=self.movie1).place( x=10, y=80, relheight=0.8, relwidth=0.3)
        Button(self.parent, height=30, width=40, image=self.bg_image5, command=self.movie2).place( x=300, y=80, relheight=0.8, relwidth=0.3)
        Button(self.parent, height=30, width=40, image=self.bg_image6, command=self.movie3).place(x=600, y=80, relheight=0.8, relwidth=0.3)
    
    def movie1(self):
        global movie
        movie = 1
        self.movie()

    def movie2(self):
        global movie
        movie = 2
        self.movie()

    def movie3(self):
        global movie
        movie = 3    
        self.movie()
    
    # This will show the seats and after selecting seats user can book the tickets
    def movie(self):
        self.parent.destroy()
        self.parent = Tk()
        self.parent.title("SEATS SELECTION")
        self.parent.geometry('770x450')
        self.parent.configure(bg='Black')
        self.custom2 = font.Font(family='Times New Roman', size=12)
        self.custom = font.Font(family='Gregorian', size=14, weight='bold')
        self.custom1 = font.Font(family='Palatino', size=20, weight='bold')
        Label(self.parent, text='SELECT YOUR SEATS', font=self.custom1 , bg='Black', fg='White').place(x=250, y=0)
        Button(self.parent, text='Book Ticket', width=25, font=self.custom, command=self.bookseat).place(x=430, y=380)
        Button(self.parent, text='<- Back', bg='Black', font=self.custom2, fg='White', command=self.movie_slc).place(x=10, y=0)
        Label(self.parent, text="", bg='Black').grid(row=0, column=0)
        Label(self.parent, text="", bg='Black').grid(row=1, column=0)
        Label(self.parent, text=" ", bg='Black').grid(row=1, column=2)
        Label(self.parent, text='A', font=self.custom, fg='White', bg='Black').grid(row=3,column=1)
        Label(self.parent, text='B', font=self.custom, fg='White', bg='Black').grid(row=4,column=1)
        Label(self.parent, text='C', font=self.custom, fg='White', bg='Black').grid(row=5,column=1)
        Label(self.parent, text='D', font=self.custom, fg='White', bg='Black').grid(row=6,column=1)
        Label(self.parent, text='E', font=self.custom, fg='White', bg='Black').grid(row=7,column=1)
        Label(self.parent, text='F', font=self.custom, fg='White', bg='Black').grid(row=8,column=1)
        Label(self.parent, text='G', font=self.custom, fg='White', bg='Black').grid(row=9,column=1)
        Label(self.parent, text='H', font=self.custom, fg='White', bg='Black').grid(row=10,column=1)
        Label(self.parent, text='I', font=self.custom, fg='White', bg='Black').grid(row=11,column=1)
        Label(self.parent, text='J', font=self.custom, fg='White', bg='Black').grid(row=12,column=1)
        Label(self.parent, text='1', font=self.custom, fg='White', bg='Black').grid(row=2,column=3)
        Label(self.parent, text='2', font=self.custom, fg='White', bg='Black').grid(row=2,column=4)
        Label(self.parent, text='3', font=self.custom, fg='White', bg='Black').grid(row=2,column=5)
        Label(self.parent, text='4', font=self.custom, fg='White', bg='Black').grid(row=2,column=6)
        Label(self.parent, text='5', font=self.custom, fg='White', bg='Black').grid(row=2,column=7)
        Label(self.parent, text='6', font=self.custom, fg='White', bg='Black').grid(row=2,column=8)
        Label(self.parent, text='7', font=self.custom, fg='White', bg='Black').grid(row=2,column=9)
        Label(self.parent, text='8', font=self.custom, fg='White', bg='Black').grid(row=2,column=10)
        Label(self.parent, text='9', font=self.custom, fg='White', bg='Black').grid(row=2,column=11)
        Label(self.parent, text='10', font=self.custom, fg='White', bg='Black').grid(row=2,column=12)
        Label(self.parent, text='11', font=self.custom, fg='White', bg='Black').grid(row=2,column=13)
        Label(self.parent, text='   Stairs   ', font=self.custom, fg='White', bg='Black').grid(row=2,column=14)
        Label(self.parent, text='12', font=self.custom, fg='White', bg='Black').grid(row=2,column=15)
        Label(self.parent, text='13', font=self.custom, fg='White', bg='Black').grid(row=2,column=16)
        Label(self.parent, text='14', font=self.custom, fg='White', bg='Black').grid(row=2,column=17)
        Label(self.parent, text='15', font=self.custom, fg='White', bg='Black').grid(row=2,column=18)
        Label(self.parent, text='16', font=self.custom, fg='White', bg='Black').grid(row=2,column=19)
        Label(self.parent, text='17', font=self.custom, fg='White', bg='Black').grid(row=2,column=20)
        Label(self.parent, text='18', font=self.custom, fg='White', bg='Black').grid(row=2,column=21)
        Label(self.parent, text='19', font=self.custom, fg='White', bg='Black').grid(row=2,column=22)
        Label(self.parent, text='20', font=self.custom, fg='White', bg='Black').grid(row=2,column=23)
        Label(self.parent, text='21', font=self.custom, fg='White', bg='Black').grid(row=2,column=24)
        Label(self.parent, text='22', font=self.custom, fg='White', bg='Black').grid(row=2,column=25)
        global a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22
        global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22
        global c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22
        global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22
        global e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22
        global f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22
        global g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22
        global h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22
        global i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22
        global j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20, j21, j22
        
        # Declaring variable which store whether the seat is selected or not
        a1 = IntVar()
        a2 = IntVar()
        a3 = IntVar()
        a4 = IntVar()
        a5 = IntVar()
        a6 = IntVar()
        a7 = IntVar()
        a8 = IntVar()
        a9 = IntVar()
        a10 = IntVar()
        a11 = IntVar()
        a12 = IntVar()
        a13 = IntVar()
        a14 = IntVar()
        a15 = IntVar()
        a16 = IntVar()
        a17 = IntVar()
        a18 = IntVar()
        a19 = IntVar()
        a20 = IntVar()
        a21 = IntVar()
        a22 = IntVar()

        b1 = IntVar()
        b2 = IntVar()
        b3 = IntVar()
        b4 = IntVar()
        b5 = IntVar()
        b6 = IntVar()
        b7 = IntVar()
        b8 = IntVar()
        b9 = IntVar()
        b10 = IntVar()
        b11 = IntVar()
        b12 = IntVar()
        b13 = IntVar()
        b14 = IntVar()
        b15 = IntVar()
        b16 = IntVar()
        b17 = IntVar()
        b18 = IntVar()
        b19 = IntVar()
        b20 = IntVar()
        b21 = IntVar()
        b22 = IntVar()

        c1 = IntVar()
        c2 = IntVar()
        c3 = IntVar()
        c4 = IntVar()
        c5 = IntVar()
        c6 = IntVar()
        c7 = IntVar()
        c8 = IntVar()
        c9 = IntVar()
        c10 = IntVar()
        c11 = IntVar()
        c12 = IntVar()
        c13 = IntVar()
        c14 = IntVar()
        c15 = IntVar()
        c16 = IntVar()
        c17 = IntVar()
        c18 = IntVar()
        c19 = IntVar()
        c20 = IntVar()
        c21 = IntVar()
        c22 = IntVar()

        d1 = IntVar()
        d2 = IntVar()
        d3 = IntVar()
        d4 = IntVar()
        d5 = IntVar()
        d6 = IntVar()
        d7 = IntVar()
        d8 = IntVar()
        d9 = IntVar()
        d10 = IntVar()
        d11 = IntVar()
        d12 = IntVar()
        d13 = IntVar()
        d14 = IntVar()
        d15 = IntVar()
        d16 = IntVar()
        d17 = IntVar()
        d18 = IntVar()
        d19 = IntVar()
        d20 = IntVar()
        d21 = IntVar()
        d22 = IntVar()

        e1 = IntVar()
        e2 = IntVar()
        e3 = IntVar()
        e4 = IntVar()
        e5 = IntVar()
        e6 = IntVar()
        e7 = IntVar()
        e8 = IntVar()
        e9 = IntVar()
        e10 = IntVar()
        e11 = IntVar()
        e12 = IntVar()
        e13 = IntVar()
        e14 = IntVar()
        e15 = IntVar()
        e16 = IntVar()
        e17 = IntVar()
        e18 = IntVar()
        e19 = IntVar()
        e20 = IntVar()
        e21 = IntVar()
        e22 = IntVar()

        f1 = IntVar()
        f2 = IntVar()
        f3 = IntVar()
        f4 = IntVar()
        f5 = IntVar()
        f6 = IntVar()
        f7 = IntVar()
        f8 = IntVar()
        f9 = IntVar()
        f10 = IntVar()
        f11 = IntVar()
        f12 = IntVar()
        f13 = IntVar()
        f14 = IntVar()
        f15 = IntVar()
        f16 = IntVar()
        f17 = IntVar()
        f18 = IntVar()
        f19 = IntVar()
        f20 = IntVar()
        f21 = IntVar()
        f22 = IntVar()

        g1 = IntVar()
        g2 = IntVar()
        g3 = IntVar()
        g4 = IntVar()
        g5 = IntVar()
        g6 = IntVar()
        g7 = IntVar()
        g8 = IntVar()
        g9 = IntVar()
        g10 = IntVar()
        g11 = IntVar()
        g12 = IntVar()
        g13 = IntVar()
        g14 = IntVar()
        g15 = IntVar()
        g16 = IntVar()
        g17 = IntVar()
        g18 = IntVar()
        g19 = IntVar()
        g20 = IntVar()
        g21 = IntVar()
        g22 = IntVar()

        h1 = IntVar()
        h2 = IntVar()
        h3 = IntVar()
        h4 = IntVar()
        h5 = IntVar()
        h6 = IntVar()
        h7 = IntVar()
        h8 = IntVar()
        h9 = IntVar()
        h10 = IntVar()
        h11 = IntVar()
        h12 = IntVar()
        h13 = IntVar()
        h14 = IntVar()
        h15 = IntVar()
        h16 = IntVar()
        h17 = IntVar()
        h18 = IntVar()
        h19 = IntVar()
        h20 = IntVar()
        h21 = IntVar()
        h22 = IntVar()

        i1 = IntVar()
        i2 = IntVar()
        i3 = IntVar()
        i4 = IntVar()
        i5 = IntVar()
        i6 = IntVar()
        i7 = IntVar()
        i8 = IntVar()
        i9 = IntVar()
        i10 = IntVar()
        i11 = IntVar()
        i12 = IntVar()
        i13 = IntVar()
        i14 = IntVar()
        i15 = IntVar()
        i16 = IntVar()
        i17 = IntVar()
        i18 = IntVar()
        i19 = IntVar()
        i20 = IntVar()
        i21 = IntVar()
        i22 = IntVar()

        j1 = IntVar()
        j2 = IntVar()
        j3 = IntVar()
        j4 = IntVar()
        j5 = IntVar()
        j6 = IntVar()
        j7 = IntVar()
        j8 = IntVar()
        j9 = IntVar()
        j10 = IntVar()
        j11 = IntVar()
        j12 = IntVar()
        j13 = IntVar()
        j14 = IntVar()
        j15 = IntVar()
        j16 = IntVar()
        j17 = IntVar()
        j18 = IntVar()
        j19 = IntVar()
        j20 = IntVar()
        j21 = IntVar()
        j22 = IntVar()

        # Creating checkbuttons which will be displayed as seats 
        Checkbutton(self.parent, variable=a1).grid(row=3, column=3)
        Checkbutton(self.parent, variable=a2).grid(row=3, column=4)
        Checkbutton(self.parent, variable=a3).grid(row=3, column=5)
        Checkbutton(self.parent, variable=a4).grid(row=3, column=6)
        Checkbutton(self.parent, variable=a5).grid(row=3, column=7)
        Checkbutton(self.parent, variable=a6).grid(row=3, column=8)
        Checkbutton(self.parent, variable=a7).grid(row=3, column=9)
        Checkbutton(self.parent, variable=a8).grid(row=3, column=10)
        Checkbutton(self.parent, variable=a9).grid(row=3, column=11)
        Checkbutton(self.parent, variable=a10).grid(row=3, column=12)
        Checkbutton(self.parent, variable=a11).grid(row=3, column=13)
        Checkbutton(self.parent, variable=a12).grid(row=3, column=15)
        Checkbutton(self.parent, variable=a13).grid(row=3, column=16)
        Checkbutton(self.parent, variable=a14).grid(row=3, column=17)
        Checkbutton(self.parent, variable=a15).grid(row=3, column=18)
        Checkbutton(self.parent, variable=a16).grid(row=3, column=19)
        Checkbutton(self.parent, variable=a17).grid(row=3, column=20)
        Checkbutton(self.parent, variable=a18).grid(row=3, column=21)
        Checkbutton(self.parent, variable=a19).grid(row=3, column=22)
        Checkbutton(self.parent, variable=a20).grid(row=3, column=23)
        Checkbutton(self.parent, variable=a21).grid(row=3, column=24)
        Checkbutton(self.parent, variable=a22).grid(row=3, column=25)

        Checkbutton(self.parent, variable=b1).grid(row=4, column=3)
        Checkbutton(self.parent, variable=b2).grid(row=4, column=4)
        Checkbutton(self.parent, variable=b3).grid(row=4, column=5)
        Checkbutton(self.parent, variable=b4).grid(row=4, column=6)
        Checkbutton(self.parent, variable=b5).grid(row=4, column=7)
        Checkbutton(self.parent, variable=b6).grid(row=4, column=8)
        Checkbutton(self.parent, variable=b7).grid(row=4, column=9)
        Checkbutton(self.parent, variable=b8).grid(row=4, column=10)
        Checkbutton(self.parent, variable=b9).grid(row=4, column=11)
        Checkbutton(self.parent, variable=b10).grid(row=4, column=12)
        Checkbutton(self.parent, variable=b11).grid(row=4, column=13)
        Checkbutton(self.parent, variable=b12).grid(row=4, column=15)
        Checkbutton(self.parent, variable=b13).grid(row=4, column=16)
        Checkbutton(self.parent, variable=b14).grid(row=4, column=17)
        Checkbutton(self.parent, variable=b15).grid(row=4, column=18)
        Checkbutton(self.parent, variable=b16).grid(row=4, column=19)
        Checkbutton(self.parent, variable=b17).grid(row=4, column=20)
        Checkbutton(self.parent, variable=b18).grid(row=4, column=21)
        Checkbutton(self.parent, variable=b19).grid(row=4, column=22)
        Checkbutton(self.parent, variable=b20).grid(row=4, column=23)
        Checkbutton(self.parent, variable=b21).grid(row=4, column=24)
        Checkbutton(self.parent, variable=b22).grid(row=4, column=25)

        Checkbutton(self.parent, variable=c1).grid(row=5, column=3)
        Checkbutton(self.parent, variable=c2).grid(row=5, column=4)
        Checkbutton(self.parent, variable=c3).grid(row=5, column=5)
        Checkbutton(self.parent, variable=c4).grid(row=5, column=6)
        Checkbutton(self.parent, variable=c5).grid(row=5, column=7)
        Checkbutton(self.parent, variable=c6).grid(row=5, column=8)
        Checkbutton(self.parent, variable=c7).grid(row=5, column=9)
        Checkbutton(self.parent, variable=c8).grid(row=5, column=10)
        Checkbutton(self.parent, variable=c9).grid(row=5, column=11)
        Checkbutton(self.parent, variable=c10).grid(row=5, column=12)
        Checkbutton(self.parent, variable=c11).grid(row=5, column=13)
        Checkbutton(self.parent, variable=c12).grid(row=5, column=15)
        Checkbutton(self.parent, variable=c13).grid(row=5, column=16)
        Checkbutton(self.parent, variable=c14).grid(row=5, column=17)
        Checkbutton(self.parent, variable=c15).grid(row=5, column=18)
        Checkbutton(self.parent, variable=c16).grid(row=5, column=19)
        Checkbutton(self.parent, variable=c17).grid(row=5, column=20)
        Checkbutton(self.parent, variable=c18).grid(row=5, column=21)
        Checkbutton(self.parent, variable=c19).grid(row=5, column=22)
        Checkbutton(self.parent, variable=c20).grid(row=5, column=23)
        Checkbutton(self.parent, variable=c21).grid(row=5, column=24)
        Checkbutton(self.parent, variable=c22).grid(row=5, column=25)

        Checkbutton(self.parent, variable=d1).grid(row=6, column=3)
        Checkbutton(self.parent, variable=d2).grid(row=6, column=4)
        Checkbutton(self.parent, variable=d3).grid(row=6, column=5)
        Checkbutton(self.parent, variable=d4).grid(row=6, column=6)
        Checkbutton(self.parent, variable=d5).grid(row=6, column=7)
        Checkbutton(self.parent, variable=d6).grid(row=6, column=8)
        Checkbutton(self.parent, variable=d7).grid(row=6, column=9)
        Checkbutton(self.parent, variable=d8).grid(row=6, column=10)
        Checkbutton(self.parent, variable=d9).grid(row=6, column=11)
        Checkbutton(self.parent, variable=d10).grid(row=6, column=12)
        Checkbutton(self.parent, variable=d11).grid(row=6, column=13)
        Checkbutton(self.parent, variable=d12).grid(row=6, column=15)
        Checkbutton(self.parent, variable=d13).grid(row=6, column=16)
        Checkbutton(self.parent, variable=d14).grid(row=6, column=17)
        Checkbutton(self.parent, variable=d15).grid(row=6, column=18)
        Checkbutton(self.parent, variable=d16).grid(row=6, column=19)
        Checkbutton(self.parent, variable=d17).grid(row=6, column=20)
        Checkbutton(self.parent, variable=d18).grid(row=6, column=21)
        Checkbutton(self.parent, variable=d19).grid(row=6, column=22)
        Checkbutton(self.parent, variable=d20).grid(row=6, column=23)
        Checkbutton(self.parent, variable=d21).grid(row=6, column=24)
        Checkbutton(self.parent, variable=d22).grid(row=6, column=25)

        Checkbutton(self.parent, variable=e1).grid(row=7, column=3)
        Checkbutton(self.parent, variable=e2).grid(row=7, column=4)
        Checkbutton(self.parent, variable=e3).grid(row=7, column=5)
        Checkbutton(self.parent, variable=e4).grid(row=7, column=6)
        Checkbutton(self.parent, variable=e5).grid(row=7, column=7)
        Checkbutton(self.parent, variable=e6).grid(row=7, column=8)
        Checkbutton(self.parent, variable=e7).grid(row=7, column=9)
        Checkbutton(self.parent, variable=e8).grid(row=7, column=10)
        Checkbutton(self.parent, variable=e9).grid(row=7, column=11)
        Checkbutton(self.parent, variable=e10).grid(row=7, column=12)
        Checkbutton(self.parent, variable=e11).grid(row=7, column=13)
        Checkbutton(self.parent, variable=e12).grid(row=7, column=15)
        Checkbutton(self.parent, variable=e13).grid(row=7, column=16)
        Checkbutton(self.parent, variable=e14).grid(row=7, column=17)
        Checkbutton(self.parent, variable=e15).grid(row=7, column=18)
        Checkbutton(self.parent, variable=e16).grid(row=7, column=19)
        Checkbutton(self.parent, variable=e17).grid(row=7, column=20)
        Checkbutton(self.parent, variable=e18).grid(row=7, column=21)
        Checkbutton(self.parent, variable=e19).grid(row=7, column=22)
        Checkbutton(self.parent, variable=e20).grid(row=7, column=23)
        Checkbutton(self.parent, variable=e21).grid(row=7, column=24)
        Checkbutton(self.parent, variable=e22).grid(row=7, column=25)

        Checkbutton(self.parent, variable=f1).grid(row=8, column=3)
        Checkbutton(self.parent, variable=f2).grid(row=8, column=4)
        Checkbutton(self.parent, variable=f3).grid(row=8, column=5)
        Checkbutton(self.parent, variable=f4).grid(row=8, column=6)
        Checkbutton(self.parent, variable=f5).grid(row=8, column=7)
        Checkbutton(self.parent, variable=f6).grid(row=8, column=8)
        Checkbutton(self.parent, variable=f7).grid(row=8, column=9)
        Checkbutton(self.parent, variable=f8).grid(row=8, column=10)
        Checkbutton(self.parent, variable=f9).grid(row=8, column=11)
        Checkbutton(self.parent, variable=f10).grid(row=8, column=12)
        Checkbutton(self.parent, variable=f11).grid(row=8, column=13)
        Checkbutton(self.parent, variable=f12).grid(row=8, column=15)
        Checkbutton(self.parent, variable=f13).grid(row=8, column=16)
        Checkbutton(self.parent, variable=f14).grid(row=8, column=17)
        Checkbutton(self.parent, variable=f15).grid(row=8, column=18)
        Checkbutton(self.parent, variable=f16).grid(row=8, column=19)
        Checkbutton(self.parent, variable=f17).grid(row=8, column=20)
        Checkbutton(self.parent, variable=f18).grid(row=8, column=21)
        Checkbutton(self.parent, variable=f19).grid(row=8, column=22)
        Checkbutton(self.parent, variable=f20).grid(row=8, column=23)
        Checkbutton(self.parent, variable=f21).grid(row=8, column=24)
        Checkbutton(self.parent, variable=f22).grid(row=8, column=25)

        Checkbutton(self.parent, variable=g1).grid(row=9, column=3)
        Checkbutton(self.parent, variable=g2).grid(row=9, column=4)
        Checkbutton(self.parent, variable=g3).grid(row=9, column=5)
        Checkbutton(self.parent, variable=g4).grid(row=9, column=6)
        Checkbutton(self.parent, variable=g5).grid(row=9, column=7)
        Checkbutton(self.parent, variable=g6).grid(row=9, column=8)
        Checkbutton(self.parent, variable=g7).grid(row=9, column=9)
        Checkbutton(self.parent, variable=g8).grid(row=9, column=10)
        Checkbutton(self.parent, variable=g9).grid(row=9, column=11)
        Checkbutton(self.parent, variable=g10).grid(row=9, column=12)
        Checkbutton(self.parent, variable=g11).grid(row=9, column=13)
        Checkbutton(self.parent, variable=g12).grid(row=9, column=15)
        Checkbutton(self.parent, variable=g13).grid(row=9, column=16)
        Checkbutton(self.parent, variable=g14).grid(row=9, column=17)
        Checkbutton(self.parent, variable=g15).grid(row=9, column=18)
        Checkbutton(self.parent, variable=g16).grid(row=9, column=19)
        Checkbutton(self.parent, variable=g17).grid(row=9, column=20)
        Checkbutton(self.parent, variable=g18).grid(row=9, column=21)
        Checkbutton(self.parent, variable=g19).grid(row=9, column=22)
        Checkbutton(self.parent, variable=g20).grid(row=9, column=23)
        Checkbutton(self.parent, variable=g21).grid(row=9, column=24)
        Checkbutton(self.parent, variable=g22).grid(row=9, column=25)

        Checkbutton(self.parent, variable=h1).grid(row=10, column=3)
        Checkbutton(self.parent, variable=h2).grid(row=10, column=4)
        Checkbutton(self.parent, variable=h3).grid(row=10, column=5)
        Checkbutton(self.parent, variable=h4).grid(row=10, column=6)
        Checkbutton(self.parent, variable=h5).grid(row=10, column=7)
        Checkbutton(self.parent, variable=h6).grid(row=10, column=8)
        Checkbutton(self.parent, variable=h7).grid(row=10, column=9)
        Checkbutton(self.parent, variable=h8).grid(row=10, column=10)
        Checkbutton(self.parent, variable=h9).grid(row=10, column=11)
        Checkbutton(self.parent, variable=h10).grid(row=10, column=12)
        Checkbutton(self.parent, variable=h11).grid(row=10, column=13)
        Checkbutton(self.parent, variable=h12).grid(row=10, column=15)
        Checkbutton(self.parent, variable=h13).grid(row=10, column=16)
        Checkbutton(self.parent, variable=h14).grid(row=10, column=17)
        Checkbutton(self.parent, variable=h15).grid(row=10, column=18)
        Checkbutton(self.parent, variable=h16).grid(row=10, column=19)
        Checkbutton(self.parent, variable=h17).grid(row=10, column=20)
        Checkbutton(self.parent, variable=h18).grid(row=10, column=21)
        Checkbutton(self.parent, variable=h19).grid(row=10, column=22)
        Checkbutton(self.parent, variable=h20).grid(row=10, column=23)
        Checkbutton(self.parent, variable=h21).grid(row=10, column=24)
        Checkbutton(self.parent, variable=h22).grid(row=10, column=25)

        Checkbutton(self.parent, variable=i1).grid(row=11, column=3)
        Checkbutton(self.parent, variable=i2).grid(row=11, column=4)
        Checkbutton(self.parent, variable=i3).grid(row=11, column=5)
        Checkbutton(self.parent, variable=i4).grid(row=11, column=6)
        Checkbutton(self.parent, variable=i5).grid(row=11, column=7)
        Checkbutton(self.parent, variable=i6).grid(row=11, column=8)
        Checkbutton(self.parent, variable=i7).grid(row=11, column=9)
        Checkbutton(self.parent, variable=i8).grid(row=11, column=10)
        Checkbutton(self.parent, variable=i9).grid(row=11, column=11)
        Checkbutton(self.parent, variable=i10).grid(row=11, column=12)
        Checkbutton(self.parent, variable=i11).grid(row=11, column=13)
        Checkbutton(self.parent, variable=i12).grid(row=11, column=15)
        Checkbutton(self.parent, variable=i13).grid(row=11, column=16)
        Checkbutton(self.parent, variable=i14).grid(row=11, column=17)
        Checkbutton(self.parent, variable=i15).grid(row=11, column=18)
        Checkbutton(self.parent, variable=i16).grid(row=11, column=19)
        Checkbutton(self.parent, variable=i17).grid(row=11, column=20)
        Checkbutton(self.parent, variable=i18).grid(row=11, column=21)
        Checkbutton(self.parent, variable=i19).grid(row=11, column=22)
        Checkbutton(self.parent, variable=i20).grid(row=11, column=23)
        Checkbutton(self.parent, variable=i21).grid(row=11, column=24)
        Checkbutton(self.parent, variable=i22).grid(row=11, column=25)

        Checkbutton(self.parent, variable=j1).grid(row=12, column=3)
        Checkbutton(self.parent, variable=j2).grid(row=12, column=4)
        Checkbutton(self.parent, variable=j3).grid(row=12, column=5)
        Checkbutton(self.parent, variable=j4).grid(row=12, column=6)
        Checkbutton(self.parent, variable=j5).grid(row=12, column=7)
        Checkbutton(self.parent, variable=j6).grid(row=12, column=8)
        Checkbutton(self.parent, variable=j7).grid(row=12, column=9)
        Checkbutton(self.parent, variable=j8).grid(row=12, column=10)
        Checkbutton(self.parent, variable=j9).grid(row=12, column=11)
        Checkbutton(self.parent, variable=j10).grid(row=12, column=12)
        Checkbutton(self.parent, variable=j11).grid(row=12, column=13)
        Checkbutton(self.parent, variable=j12).grid(row=12, column=15)
        Checkbutton(self.parent, variable=j13).grid(row=12, column=16)
        Checkbutton(self.parent, variable=j14).grid(row=12, column=17)
        Checkbutton(self.parent, variable=j15).grid(row=12, column=18)
        Checkbutton(self.parent, variable=j16).grid(row=12, column=19)
        Checkbutton(self.parent, variable=j17).grid(row=12, column=20)
        Checkbutton(self.parent, variable=j18).grid(row=12, column=21)
        Checkbutton(self.parent, variable=j19).grid(row=12, column=22)
        Checkbutton(self.parent, variable=j20).grid(row=12, column=23)
        Checkbutton(self.parent, variable=j21).grid(row=12, column=24)
        Checkbutton(self.parent, variable=j22).grid(row=12, column=25)
    
    # Displaying the confirmation video of booked seats and amount
    def bookseat(self):
        self.parent.destroy()
        self.parent = Tk()
        self.parent.title("BOOKING CONFIRMED")
        self.parent.geometry('550x350')
        self.parent.configure(bg='Black')
        global seat, amt
        seat = ""
        amt = 0
        count=0
        if(a1.get()==1):
            # Validating if seat is booked or not
            seat += 'A1,'
            amt += 190
            count+=1
        if(a2.get()==1):
            seat += 'A2,'
            amt+=190
            count+=1
        if(a3.get()==1):
            seat += 'A3,'
            amt+=190
            count+=1
        if(a4.get()==1):
            seat += 'A4,'
            amt += 190
            count+=1
        if(a5.get()==1):
            seat += 'A5,'
            amt += 190
            count+=1
        if(a6.get()==1):
            seat += 'A6,'
            amt += 190
            count+=1
        if(a7.get()==1):
            seat += 'A7,'
            amt += 190
            count+=1
        if(a8.get()==1):
            seat += 'A8,'
            amt += 190
            count+=1
        if(a9.get()==1):
            seat += 'A9,'
            amt += 190
            count+=1
        if(a10.get()==1):
            seat += 'A10,'
            amt += 190
            count+=1
        if(a11.get()==1):
            seat += 'A11,'
            amt += 190
            count+=1
        if(a12.get()==1):
            seat += 'A12,'
            amt += 190
            count+=1
        if(a13.get()==1):
            seat += 'A13,'
            amt += 190
            count+=1
        if(a14.get()==1):
            seat += 'A14,'
            amt += 190
            count+=1
        if(a15.get()==1):
            seat += 'A15,'
            amt += 190
            count+=1
        if(a16.get()==1):
            seat += 'A16,'
            amt += 190
            count+=1
        if(a17.get()==1):
            seat += 'A17,'
            amt += 190
            count+=1
        if(a18.get()==1):
            seat += 'A18,'
            amt += 190
            count+=1
        if(a19.get()==1):
            seat += 'A19,'
            amt += 190
            count+=1
        if(a20.get()==1):
            seat += 'A20,'
            amt += 190
            count+=1
        if(a21.get()==1):
            seat += 'A21,'
            amt += 190
            count+=1
        if(a22.get()==1):
            seat += 'A22,'
            amt += 190
            count+=1
        if(b1.get()==1):
            seat += 'B1,'
            amt += 190
            count+=1
        if(b2.get()==1):
            seat += 'B2,'
            amt+=190
            count+=1
        if(b3.get()==1):
            seat += 'B3,'
            amt+=190
            count+=1
        if(b4.get()==1):
            seat += 'B4,'
            amt += 190
            count+=1
        if(b5.get()==1):
            seat += 'B5,'
            amt += 190
            count+=1
        if(b6.get()==1):
            seat += 'B6,'
            amt += 190
            count+=1
        if(b7.get()==1):
            seat += 'B7,'
            amt += 190
            count+=1
        if(b8.get()==1):
            seat += 'B8,'
            amt += 190
            count+=1
        if(b9.get()==1):
            seat += 'B9,'
            amt += 190
            count+=1
        if(b10.get()==1):
            seat += 'B10,'
            amt += 190
            count+=1
        if(b11.get()==1):
            seat += 'B11,'
            amt += 190
            count+=1
        if(b12.get()==1):
            seat += 'B12,'
            amt += 190
            count+=1
        if(b13.get()==1):
            seat += 'B13,'
            amt += 190
            count+=1
        if(b14.get()==1):
            seat += 'B14,'
            amt += 190
            count+=1
        if(b15.get()==1):
            seat += 'B15,'
            amt += 190
            count+=1
        if(b16.get()==1):
            seat += 'B16,'
            amt += 190
            count+=1
        if(b17.get()==1):
            seat += 'B17,'
            amt += 190
            count+=1
        if(b18.get()==1):
            seat += 'B18,'
            amt += 190
            count+=1
        if(b19.get()==1):
            seat += 'B19,'
            amt += 190
            count+=1
        if(b20.get()==1):
            seat += 'B20,'
            amt += 190
            count+=1
        if(b21.get()==1):
            seat += 'B21,'
            amt += 190
            count+=1
        if(b22.get()==1):
            seat += 'B22,'
            amt += 190
            count+=1
        if(c1.get()==1):
            seat += 'C1,'
            amt += 190
            count+=1
        if(c2.get()==1):
            seat += 'C2,'
            amt+=190
            count+=1
        if(c3.get()==1):
            seat += 'C3,'
            amt+=190
            count+=1
        if(c4.get()==1):
            seat += 'C4,'
            amt += 190
            count+=1
        if(c5.get()==1):
            seat += 'C5,'
            amt += 190
            count+=1
        if(c6.get()==1):
            seat += 'C6,'
            amt += 190
            count+=1
        if(c7.get()==1):
            seat += 'C7,'
            amt += 190
            count+=1
        if(c8.get()==1):
            seat += 'C8,'
            amt += 190
            count+=1
        if(c9.get()==1):
            seat += 'C9,'
            amt += 190
            count+=1
        if(c10.get()==1):
            seat += 'C10,'
            amt += 190
            count+=1
        if(c11.get()==1):
            seat += 'C11,'
            amt += 190
            count+=1
        if(c12.get()==1):
            seat += 'C12,'
            amt += 190
            count+=1
        if(c13.get()==1):
            seat += 'C13,'
            amt += 190
            count+=1
        if(c14.get()==1):
            seat += 'C14,'
            amt += 190
            count+=1
        if(c15.get()==1):
            seat += 'C15,'
            amt += 190
            count+=1
        if(c16.get()==1):
            seat += 'C16,'
            amt += 190
            count+=1
        if(c17.get()==1):
            seat += 'C17,'
            amt += 190
            count+=1
        if(c18.get()==1):
            seat += 'C18,'
            amt += 190
            count+=1
        if(c19.get()==1):
            seat += 'C19,'
            amt += 190
            count+=1
        if(c20.get()==1):
            seat += 'C20,'
            amt += 190
            count+=1
        if(c21.get()==1):
            seat += 'C21,'
            amt += 190
            count+=1
        if(c22.get()==1):
            seat += 'C22,'
            amt += 190
            count+=1
        if(d1.get()==1):
            seat += 'D1,'
            amt += 180
            count+=1
        if(d2.get()==1):
            seat += 'D2,'
            amt+=180
            count+=1
        if(d3.get()==1):
            seat += 'D3,'
            amt+=180
            count+=1
        if(d4.get()==1):
            seat += 'D4,'
            amt += 180
            count+=1
        if(d5.get()==1):
            seat += 'D5,'
            amt += 180
            count+=1
        if(d6.get()==1):
            seat += 'D6,'
            amt += 180
            count+=1
        if(d7.get()==1):
            seat += 'D7,'
            amt += 180
            count+=1
        if(d8.get()==1):
            seat += 'D8,'
            amt += 180
            count+=1
        if(d9.get()==1):
            seat += 'D9,'
            amt += 180
            count+=1
        if(d10.get()==1):
            seat += 'D10,'
            amt += 180
            count+=1
        if(d11.get()==1):
            seat += 'D11,'
            amt += 180
            count+=1
        if(d12.get()==1):
            seat += 'D12,'
            amt += 180
            count+=1
        if(d13.get()==1):
            seat += 'D13,'
            amt += 180
            count+=1
        if(d14.get()==1):
            seat += 'D14,'
            amt += 180
            count+=1
        if(d15.get()==1):
            seat += 'D15,'
            amt += 180
            count+=1
        if(d16.get()==1):
            seat += 'D16,'
            amt += 180
            count+=1
        if(d17.get()==1):
            seat += 'D17,'
            amt += 180
            count+=1
        if(d18.get()==1):
            seat += 'D18,'
            amt += 180
            count+=1
        if(d19.get()==1):
            seat += 'D19,'
            amt += 180
            count+=1
        if(d20.get()==1):
            seat += 'D20,'
            amt += 180
            count+=1
        if(d21.get()==1):
            seat += 'D21,'
            amt += 180
            count+=1
        if(d22.get()==1):
            seat += 'D22,'
            amt += 180
            count+=1
        if(e1.get()==1):
            seat += 'E1,'
            amt += 180
            count+=1
        if(e2.get()==1):
            seat += 'E2,'
            amt+=180
            count+=1
        if(e3.get()==1):
            seat += 'E3,'
            amt+=180
            count+=1
        if(e4.get()==1):
            seat += 'E4,'
            amt += 180
            count+=1
        if(e5.get()==1):
            seat += 'E5,'
            amt += 180
            count+=1
        if(e6.get()==1):
            seat += 'E6,'
            amt += 180
            count+=1
        if(e7.get()==1):
            seat += 'E7,'
            amt += 180
            count+=1
        if(e8.get()==1):
            seat += 'E8,'
            amt += 180
            count+=1
        if(e9.get()==1):
            seat += 'E9,'
            amt += 180
            count+=1
        if(e10.get()==1):
            seat += 'E10,'
            amt += 180
            count+=1
        if(e11.get()==1):
            seat += 'E11,'
            amt += 180
            count+=1
        if(e12.get()==1):
            seat += 'E12,'
            amt += 180
            count+=1
        if(e13.get()==1):
            seat += 'E13,'
            amt += 180
            count+=1
        if(e14.get()==1):
            seat += 'E14,'
            amt += 180
            count+=1
        if(e15.get()==1):
            seat += 'E15,'
            amt += 180
            count+=1
        if(e16.get()==1):
            seat += 'E16,'
            amt += 180
            count+=1
        if(e17.get()==1):
            seat += 'E17,'
            amt += 180
            count+=1
        if(e18.get()==1):
            seat += 'E18,'
            amt += 180
            count+=1
        if(e19.get()==1):
            seat += 'E19,'
            amt += 180
            count+=1
        if(e20.get()==1):
            seat += 'E20,'
            amt += 180
            count+=1
        if(e21.get()==1):
            seat += 'E21,'
            amt += 180
            count+=1
        if(e22.get()==1):
            seat += 'E22,'
            amt += 180
            count+=1
        if(f1.get()==1):
            seat += 'F1,'
            amt += 180
            count+=1
        if(f2.get()==1):
            seat += 'F2,'
            amt+=180
            count+=1
        if(f3.get()==1):
            seat += 'F3,'
            amt+=180
            count+=1
        if(f4.get()==1):
            seat += 'F4,'
            amt += 180
            count+=1
        if(f5.get()==1):
            seat += 'F5,'
            amt += 180
            count+=1
        if(f6.get()==1):
            seat += 'F6,'
            amt += 180
            count+=1
        if(f7.get()==1):
            seat += 'F7,'
            amt += 180
            count+=1
        if(f8.get()==1):
            seat += 'F8,'
            amt += 180
            count+=1
        if(f9.get()==1):
            seat += 'F9,'
            amt += 180
            count+=1
        if(f10.get()==1):
            seat += 'F10,'
            amt += 180
            count+=1
        if(f11.get()==1):
            seat += 'F11,'
            amt += 180
            count+=1
        if(f12.get()==1):
            seat += 'F12,'
            amt += 180
            count+=1
        if(f13.get()==1):
            seat += 'F13,'
            amt += 180
            count+=1
        if(f14.get()==1):
            seat += 'F14,'
            amt += 180
            count+=1
        if(f15.get()==1):
            seat += 'F15,'
            amt += 180
            count+=1
        if(f16.get()==1):
            seat += 'F16,'
            amt += 180
            count+=1
        if(f17.get()==1):
            seat += 'F17,'
            amt += 180
            count+=1
        if(f18.get()==1):
            seat += 'F18,'
            amt += 180
            count+=1
        if(f19.get()==1):
            seat += 'F19,'
            amt += 180
            count+=1
        if(f20.get()==1):
            seat += 'F20,'
            amt += 180
            count+=1
        if(f21.get()==1):
            seat += 'F21,'
            amt += 180
            count+=1
        if(f22.get()==1):
            seat += 'F22,'
            amt += 180
            count+=1
        if(g1.get()==1):
            seat += 'G1,'
            amt += 170
            count+=1
        if(g2.get()==1):
            seat += 'G2,'
            amt+=170
            count+=1
        if(g3.get()==1):
            seat += 'G3,'
            amt+=170
            count+=1
        if(g4.get()==1):
            seat += 'G4,'
            amt += 170
            count+=1
        if(g5.get()==1):
            seat += 'G5,'
            amt += 170
            count+=1
        if(g6.get()==1):
            seat += 'G6,'
            amt += 170
            count+=1
        if(g7.get()==1):
            seat += 'G7,'
            amt += 170
            count+=1
        if(g8.get()==1):
            seat += 'G8,'
            amt += 170
            count+=1
        if(g9.get()==1):
            seat += 'G9,'
            amt += 170
            count+=1
        if(g10.get()==1):
            seat += 'G10,'
            amt += 170
            count+=1
        if(g11.get()==1):
            seat += 'G11,'
            amt += 170
            count+=1
        if(g12.get()==1):
            seat += 'G12,'
            amt += 170
            count+=1
        if(g13.get()==1):
            seat += 'G13,'
            amt += 170
            count+=1
        if(g14.get()==1):
            seat += 'G14,'
            amt += 170
            count+=1
        if(g15.get()==1):
            seat += 'G15,'
            amt += 170
            count+=1
        if(g16.get()==1):
            seat += 'G16,'
            amt += 170
            count+=1
        if(g17.get()==1):
            seat += 'G17,'
            amt += 170
            count+=1
        if(g18.get()==1):
            seat += 'G18,'
            amt += 170
            count+=1
        if(g19.get()==1):
            seat += 'G19,'
            amt += 170
            count+=1
        if(g20.get()==1):
            seat += 'G20,'
            amt += 170
            count+=1
        if(g21.get()==1):
            seat += 'G21,'
            amt += 170
            count+=1
        if(g22.get()==1):
            seat += 'G22,'
            amt += 170
            count+=1
        if(h1.get()==1):
            seat += 'H1,'
            amt += 170
            count+=1
        if(h2.get()==1):
            seat += 'H2,'
            amt+=170
            count+=1
        if(h3.get()==1):
            seat += 'H3,'
            amt+=170
            count+=1
        if(h4.get()==1):
            seat += 'H4,'
            amt += 170
            count+=1
        if(h5.get()==1):
            seat += 'H5,'
            amt += 170
            count+=1
        if(h6.get()==1):
            seat += 'H6,'
            amt += 170
            count+=1
        if(h7.get()==1):
            seat += 'H7,'
            amt += 170
            count+=1
        if(h8.get()==1):
            seat += 'H8,'
            amt += 170
            count+=1
        if(h9.get()==1):
            seat += 'H9,'
            amt += 170
            count+=1
        if(h10.get()==1):
            seat += 'H10,'
            amt += 170
            count+=1
        if(h11.get()==1):
            seat += 'H11,'
            amt += 170
            count+=1
        if(h12.get()==1):
            seat += 'H12,'
            amt += 170
            count+=1
        if(h13.get()==1):
            seat += 'H13,'
            amt += 170
            count+=1
        if(h14.get()==1):
            seat += 'H14,'
            amt += 170
            count+=1
        if(h15.get()==1):
            seat += 'H15,'
            amt += 170
            count+=1
        if(h16.get()==1):
            seat += 'H16,'
            amt += 170
            count+=1
        if(h17.get()==1):
            seat += 'H17,'
            amt += 170
            count+=1
        if(h18.get()==1):
            seat += 'H18,'
            amt += 170
            count+=1
        if(h19.get()==1):
            seat += 'H19,'
            amt += 170
            count+=1
        if(h20.get()==1):
            seat += 'H20,'
            amt += 170
            count+=1
        if(h21.get()==1):
            seat += 'H21,'
            amt += 170
            count+=1
        if(h22.get()==1):
            seat += 'H22,'
            amt += 170
            count+=1
        if(i1.get()==1):
            seat += 'I1,'
            amt += 170
            count+=1
        if(i2.get()==1):
            seat += 'I2,'
            amt+=170
            count+=1
        if(i3.get()==1):
            seat += 'I3,'
            amt+=170
            count+=1
        if(i4.get()==1):
            seat += 'I4,'
            amt += 170
            count+=1
        if(i5.get()==1):
            seat += 'I5,'
            amt += 170
            count+=1
        if(i6.get()==1):
            seat += 'I6,'
            amt += 170
            count+=1
        if(i7.get()==1):
            seat += 'I7,'
            amt += 170
            count+=1
        if(i8.get()==1):
            seat += 'I8,'
            amt += 170
            count+=1
        if(i9.get()==1):
            seat += 'I9,'
            amt += 170
            count+=1
        if(i10.get()==1):
            seat += 'I10,'
            amt += 170
            count+=1
        if(i11.get()==1):
            seat += 'I11,'
            amt += 170
            count+=1
        if(i12.get()==1):
            seat += 'I12,'
            amt += 170
            count+=1
        if(i13.get()==1):
            seat += 'I13,'
            amt += 170
            count+=1
        if(i14.get()==1):
            seat += 'I14,'
            amt += 170
            count+=1
        if(i15.get()==1):
            seat += 'I15,'
            amt += 170
            count+=1
        if(i16.get()==1):
            seat += 'I16,'
            amt += 170
            count+=1
        if(i17.get()==1):
            seat += 'I17,'
            amt += 170
            count+=1
        if(i18.get()==1):
            seat += 'I18,'
            amt += 170
            count+=1
        if(i19.get()==1):
            seat += 'I19,'
            amt += 170
            count+=1
        if(i20.get()==1):
            seat += 'I20,'
            amt += 170
            count+=1
        if(i21.get()==1):
            seat += 'I21,'
            amt += 170
            count+=1
        if(i22.get()==1):
            seat += 'I22,'
            amt += 170
            count+=1
        if(j1.get()==1):
            seat += 'J1,'
            amt += 170
            count+=1
        if(j2.get()==1):
            seat += 'J2,'
            amt+=170
            count+=1
        if(j3.get()==1):
            seat += 'J3,'
            amt+=170
            count+=1
        if(j4.get()==1):
            seat += 'J4,'
            amt += 170
            count+=1
        if(j5.get()==1):
            seat += 'J5,'
            amt += 170
            count+=1
        if(j6.get()==1):
            seat += 'J6,'
            amt += 170
            count+=1
        if(j7.get()==1):
            seat += 'J7,'
            amt += 170
            count+=1
        if(j8.get()==1):
            seat += 'J8,'
            amt += 170
            count+=1
        if(j9.get()==1):
            seat += 'J9,'
            amt += 170
            count+=1
        if(j10.get()==1):
            seat += 'J10,'
            amt += 170
            count+=1
        if(j11.get()==1):
            seat += 'J11,'
            amt += 170
            count+=1
        if(j12.get()==1):
            seat += 'J12,'
            amt += 170
            count+=1
        if(j13.get()==1):
            seat += 'J13,'
            amt += 170
            count+=1
        if(j14.get()==1):
            seat += 'J14,'
            amt += 170
            count+=1
        if(j15.get()==1):
            seat += 'J15,'
            amt += 170
            count+=1
        if(j16.get()==1):
            seat += 'J16,'
            amt += 170
            count+=1
        if(j17.get()==1):
            seat += 'J17,'
            amt += 170
            count+=1
        if(j18.get()==1):
            seat += 'J18,'
            amt += 170
            count+=1
        if(j19.get()==1):
            seat += 'J19,'
            amt += 170
            count+=1
        if(j20.get()==1):
            seat += 'J20,'
            amt += 170
            count+=1
        if(j21.get()==1):
            seat += 'J21,'
            amt += 170
            count+=1
        if(j22.get()==1):
            seat += 'J22,'
            amt += 170
            count+=1
        self.custom2 = font.Font(family='Times New Roman', size=12)
        self.custom = font.Font(family='Gregorian', size=20, weight='bold')
        self.custom1 = font.Font(family='Palatino', size=30, weight='bold')
        text1 = "Your seat no. is : " + seat
        text2 = "Total amount : " + str(amt)
        username = self.name
        self.image_path7 = Image.open("D:/brilliko/python/Tkinter/ticket.jpg")
        self.bg_image7 = ImageTk.PhotoImage(self.image_path7)
        bg_label7 = Label(self.parent, image=self.bg_image7)
        bg_label7.place(relheight=0.7, relwidth=1)
        Label(self.parent, text=text1, fg='White', bg='Black', font=self.custom).place(x=40, y=250)
        Label(self.parent, text=text2, fg='White', bg='Black', font=self.custom).place(x=40, y=300)

        # Creating buttons for if user want to get back to previous window or want to log out
        Button(self.parent, text='<- Back', bg='Black', font=self.custom2, fg='White', command=self.movie).place(x=10, y=10)
        Button(self.parent, text='Logout', bg='Black', font=self.custom2, fg='White', command=self.main).place(x=480, y=10)
        sql = 'select uname from booking where uname = %s'
        data=(username,)
        myc = conn.cursor()
        myc.execute(sql,data)
        res = myc.fetchall()
        result = ', '.join(str(i[0]) for i in res)
        if username in result:
            # If user has already booked the seats it will update it with new seat
            sql= 'update booking set seat = %s, amount = %s where uname = %s'
            data= (seat, amt, username)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
        else:
            # If user is booking seats for first time it will insert the data of new seats booked
            sql = 'insert into booking values(%s,%s,%s, %s,%s)'
            data= (username, seat, amt, movie, count)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()


if __name__ == "__main__":
    parent = Tk()
    app = TicketBooking(parent)
    parent.mainloop()