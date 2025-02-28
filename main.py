from tkinter import*
from tkinter import ttk
import tkinter as tk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

from PIL import Image, ImageTk
from customer import Cust_Win
from airlines import Win
from reservations import Win2
from flights import Win3

# ==================================================================================================================================
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


                # ========================================================Dataframe======================================================================



if __name__=="__main__":
    root=Tk()
    ob=Airplane(root)
    root.mainloop()