from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("510x742+0+0")

        # =============== variables ===========================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_ename = StringVar()
        self.var_pname = StringVar()

        #=============tlo====================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\48882\PycharmProjects\AIRmanagement\images\register.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        #============= ramka na dole ======================
        frame = Frame(self.root, bg="lightgrey")
        frame.place(x=0, y=400, width=510, height=300)

        #==============label and entry =======================

        #=====firstname
        fname = Label(frame, text="First Name", font=("times new roman", 15))
        fname.place(x=50, y=30)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        fname_entry.place(x=50, y=60, width=170)

        #=====lastname
        lname = Label(frame, text="Last Name", font=("times new roman", 15))
        lname.place(x=280, y=30)

        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        lname_entry.place(x=280, y=60, width=170)

        #=====email
        ename = Label(frame, text="E-mail", font=("times new roman", 15))
        ename.place(x=50, y=100)

        ename_entry = ttk.Entry(frame, textvariable=self.var_ename, font=("times new roman", 15))
        ename_entry.place(x=50, y=130, width=170)

        #password
        pname = Label(frame, text="Password", font=("times new roman", 15))
        pname.place(x=280, y=100)

        pname_entry = ttk.Entry(frame, textvariable=self.var_pname, font=("times new roman", 15))
        pname_entry.place(x=280, y=130, width=170)

        #register button
        register_btn = Button(frame, text="Register", command=self.register_data, font=("times new roman", 15, "bold"), bg="green", fg="white")
        register_btn.place(x=50, y=200, width=170)

        # login button
        login_btn = Button(frame, text="Login now", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        login_btn.place(x=280, y=200, width=170)

    #================================function==================================================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_ename.get()=="" or self.var_lname.get()=="" or self.var_pname.get()=="":
            messagebox.showerror("Error", "All fields are required")

        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="Katarzyna090",database="plane_management")
            my_cursor=conn.cursor()
            query=("select * from register where ename = %s")
            value=(self.var_ename.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("ERROR","User exists")
            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_ename.get(),
                                                                                            self.var_pname.get()
                                                                                            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully")

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()