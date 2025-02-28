from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from customer import Cust_Win
from airlines import Win
from reservations import Win2
from flights import Win3

def main():
    win = Tk()
    app = Login(win)
    win.mainloop()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("510x742+500+20")

        # =============== variables ===========================
        self.var_ename = StringVar()
        self.var_pname = StringVar()

        #============= tło ====================
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\48882\PycharmProjects\AIRmanagement\images\register.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        #============= ramka na dole ======================
        frame = Frame(self.root, bg="lightgrey")
        frame.place(x=0, y=400, width=510, height=300)

        #============== label and entry =======================
        # email
        ename1 = Label(frame, text="E-mail", font=("times new roman", 15))
        ename1.place(x=50, y=80)

        ename1_entry = ttk.Entry(frame, textvariable=self.var_ename, font=("times new roman", 15))
        ename1_entry.place(x=50, y=110, width=170)

        # password
        pname1 = Label(frame, text="Password", font=("times new roman", 15))
        pname1.place(x=280, y=80)

        pname1_entry = ttk.Entry(frame, textvariable=self.var_pname, font=("times new roman", 15), show='*')
        pname1_entry.place(x=280, y=110, width=170)

        # login button
        login_btn1 = Button(frame, text="Login now", command=self.login, font=("times new roman", 15, "bold"),
                            bg="blue", fg="white")
        login_btn1.place(x=165, y=180, width=170)

        # register button
        login_btn2 = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 8, "bold"), bg="lightgrey", fg="black")
        login_btn2.place(x=165, y=230, width=170)

        # forgot password button
        forgot_pass_btn = Button(frame, text="Forgot Password?", command=self.forgot_password, font=("times new roman", 8, "bold"), bg="lightgrey", fg="black")
        forgot_pass_btn.place(x=165, y=260, width=170)




    def register_window(self):
        self.new_window = Toplevel(self.root)
        Register(self.new_window)

    def login(self):
        if self.var_ename.get() == "" or self.var_pname.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register where ename=%s and passwd=%s", (
                    self.var_ename.get(),
                    self.var_pname.get()
                ))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username & Password")
                else:
                    self.new_window = Toplevel(self.root)
                    self.app = Airplane(self.new_window)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}")

    def forgot_password(self):
        if self.var_ename.get() == "":
            messagebox.showerror("Error", "Please enter the E-mail address to reset password")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
                my_cursor = conn.cursor()
                query = ("select * from register where ename=%s")
                value = (self.var_ename.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "E-mail address not found")
                else:
                    self.new_window = Toplevel(self.root)
                    self.app = ForgotPassword(self.new_window, self.var_ename.get())
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}")

class ForgotPassword:
    def __init__(self, root, email):
        self.root = root
        self.root.title("Password recovery")
        self.root.geometry("510x742+500+20")
        self.email = email

        # =============== variables ===========================
        self.var_special_pass = StringVar()
        self.var_new_pass = StringVar()

        #============= tło ====================
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\48882\PycharmProjects\AIRmanagement\images\register.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ============= ramka na dole ======================
        frame = Frame(self.root, bg="lightgrey")
        frame.place(x=0, y=400, width=510, height=300)

        # ==============label and entry =======================
        # special pass
        special_pass_label = Label(frame, text="Enter CloudinAir's unique password", font=("times new roman", 15))
        special_pass_label.place(x=112, y=30)

        special_pass_entry = ttk.Entry(frame, textvariable=self.var_special_pass, font=("times new roman", 15))
        special_pass_entry.place(x=90, y=60, width=335)

        # new password
        new_pass_label = Label(frame, text="Enter your new password", font=("times new roman", 15))
        new_pass_label.place(x=160, y=100)

        new_pass_entry = ttk.Entry(frame, textvariable=self.var_new_pass, font=("times new roman", 15))
        new_pass_entry.place(x=90, y=130, width=335)

        # save changes button
        save_changes_btn = Button(frame, text="Save changes", command=self.reset_password, font=("times new roman", 15, "bold"),
                                  bg="green", fg="white")
        save_changes_btn.place(x=170, y=195, width=170)

    def reset_password(self):
        special_password = "AdminCloudinAir"
        if self.var_special_pass.get() == special_password:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
                my_cursor = conn.cursor()
                query = "update register set passwd=%s where ename=%s"
                value = (self.var_new_pass.get(), self.email)
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Password has been reset successfully")
                self.root.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}")
        else:
            messagebox.showerror("Error", "Invalid CloudinAir's unique password")

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("510x742+500+20")

        # =============== variables ===========================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_ename = StringVar()
        self.var_pname = StringVar()

        #============= tło ====================
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\48882\PycharmProjects\AIRmanagement\images\register.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        #============= ramka na dole ======================
        frame = Frame(self.root, bg="lightgrey")
        frame.place(x=0, y=400, width=510, height=300)

        #============== label and entry =======================
        # firstname
        fname = Label(frame, text="First Name", font=("times new roman", 15))
        fname.place(x=50, y=30)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        fname_entry.place(x=50, y=60, width=170)

        # lastname
        lname = Label(frame, text="Last Name", font=("times new roman", 15))
        lname.place(x=280, y=30)

        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        lname_entry.place(x=280, y=60, width=170)

        # email
        ename = Label(frame, text="E-mail", font=("times new roman", 15))
        ename.place(x=50, y=100)

        ename_entry = ttk.Entry(frame, textvariable=self.var_ename, font=("times new roman", 15))
        ename_entry.place(x=50, y=130, width=170)

        # password
        pname = Label(frame, text="Password", font=("times new roman", 15))
        pname.place(x=280, y=100)

        pname_entry = ttk.Entry(frame, textvariable=self.var_pname, font=("times new roman", 15))
        pname_entry.place(x=280, y=130, width=170)

        # register button
        register_btn = Button(frame, text="Register", command=self.register_data, font=("times new roman", 15, "bold"), bg="green", fg="white")
        register_btn.place(x=50, y=200, width=170)

        # login button
        login_btn = Button(frame, text="Login now", command=self.return_login, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        login_btn.place(x=280, y=200, width=170)

    # ================================= function ==============================================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_ename.get() == "" or self.var_lname.get() == "" or self.var_pname.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root",password="new_password", database="plane_management")
                my_cursor = conn.cursor()
                query = ("select * from register where ename = %s")
                value = (self.var_ename.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists")
                else:
                    my_cursor.execute("insert into register (fname, lname, ename, passwd) values (%s, %s, %s, %s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_ename.get(),
                        self.var_pname.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registered Successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}")

    def return_login(self):
        self.root.destroy()


class Airplane:
    def __init__(self,root):
        self.root=root
        self.root.title("AIR Management System")
        self.root.geometry("1350x780+95+0")
        # ============= tło ====================
        img1=Image.open(r"C:\Users\48882\PycharmProjects\AIRmanagement\images\stronaglowna.jpg")
        img1=img1.resize((1550,140), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root, image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0, width=1350, height=140)

        # logo

        img2 = Image.open(r"C:\Users\48882\PycharmProjects\AIRmanagement\images\firma.png")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)



        lbltitle=Label(self.root, bd=1,relief=RIDGE, text="CloudinAir Management System", fg="black", bg="white", font= ("times new roman", 27, "bold"))
        lbltitle.place(x=0,y=140, width=1350, height=60)

        #main frame
        main_frame=Frame(self.root,bd=4, relief=RIDGE, bg="lightgrey")
        main_frame.place(x=0,y=190, width=1350, height=640)

        #menu
        lblmenu = Label(self.root, bd=4, relief=RIDGE, text="Menu", fg="black", bg="white",
                        font=("times new roman", 30, "bold"))
        lblmenu.place(x=0, y=195, width=230)

        #btn frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=58, width=225, height=640)

        cust_btn=Button(btn_frame,text="PASSENGERS", command=self.cust_det, font=("times new roman", 14, "bold"), fg= "black", bd=3)
        cust_btn.place(x=0, y= 0, width=220, height = 70)

        cust_btn1 = Button(btn_frame, text="RESERVATIONS",command=self.cust_det2, font=("times new roman", 14, "bold"), fg="black", bd=3)
        cust_btn1.place(x=0, y=70, width=220, height = 70)

        cust_btn2 = Button(btn_frame, text="AVAILABLE FLIGHTS",command=self.cust_det3 ,font=("times new roman", 14, "bold"), fg="black", bd=3)
        cust_btn2.place(x=0, y=140, width=220, height=70)

        cust_btn3 = Button(btn_frame, text="AIRLINES", command=self.cust_det1,font=("times new roman", 14, "bold"), fg="black", bd=3)
        cust_btn3.place(x=0, y=210, width=220, height=70)

        cust_btn4 = Button(btn_frame, text="LOGOUT", command=self.log, font=("times new roman", 14, "bold"), fg="black", bd=3)
        cust_btn4.place(x=0, y=280, width=220, height=70)

        #right side
        img13 = Image.open(r"C:\Users\48882\PycharmProjects\AIRmanagement\images\ziemia.png")
        img13 = img13.resize((950, 650), Image.Resampling.LANCZOS)
        self.photoimg13 = ImageTk.PhotoImage(img13)

        # Create a Label widget and place it in the root window
        lblimg1 = Label(self.root, image=self.photoimg13, bd=4, relief=RIDGE, bg="white")
        lblimg1.place(x=230, y=190, width=1310, height=590)

#================ logout ============
    def log(self):
        self.root.destroy()

# ================passengers
    def cust_det(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
 # ================airlines
    def cust_det1(self):
        self.new_window1 = Toplevel(self.root)
        self.app1 = Win(self.new_window1)

    def cust_det2(self):
        self.new_window2 = Toplevel(self.root)
        self.app2 = Win2(self.new_window2)

    def cust_det3(self):
        self.new_window3 = Toplevel(self.root)
        self.app3 = Win3(self.new_window3)


    #===============logout=====================
    def log(self):
        self.root.destroy()


if __name__ == "__main__":
    main()