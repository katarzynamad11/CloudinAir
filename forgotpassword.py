from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
class Forgot_password:
    def __init__(self, root):
        self.root = root
        self.root.title("Password recovery")
        self.root.geometry("510x742+0+0")

        # =============== variables ===========================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_ename = StringVar()
        self.var_pname = StringVar()

        #============= tło ====================
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\48882\PycharmProjects\AIRmanagement\images\register.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ============= ramka na dole ======================
        frame = Frame(self.root, bg="lightgrey")
        frame.place(x=0, y=400, width=510, height=300)

        # ==============label and entry =======================

        # =====pass
        fname = Label(frame, text="Enter your CloudinAir's unique password", font=("times new roman", 15))
        fname.place(x=90, y=30)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        fname_entry.place(x=90, y=60, width=335)

        # =====newpass
        ename = Label(frame, text="Enter your new password", font=("times new roman", 15))
        ename.place(x=160, y=100)

        ename_entry = ttk.Entry(frame, textvariable=self.var_ename, font=("times new roman", 15))
        ename_entry.place(x=90, y=130, width=335)



        # register button
        register_btn = Button(frame, text="Safe changes", font=("times new roman", 15, "bold"),
                              bg="green", fg="white")
        register_btn.place(x=170, y=195, width=170)


if __name__ == "__main__":
    root=Tk()
    app=Forgot_password(root)
    root.mainloop()