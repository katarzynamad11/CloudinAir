from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk



class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Passenger Management")
        self.root.geometry("1120x550+326+226")

        # =============== variables ===========================
        self.var_lbl_cust_fname = StringVar()
        self.var_lbl_cust_lname = StringVar()
        self.var_lbl_cust_gender = StringVar()
        self.var_lbl_cust_address = StringVar()
        self.var_lbl_cust_contact = StringVar()
        self.var_lbl_cust_email = StringVar()


        lbl_title = Label(self.root, text="Passengers details", font=("times new roman", 15, "bold"), bg="black",
                          fg="white")
        lbl_title.place(x=0, y=0, width=1120, height=50)

        # ======================================================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer details",
                                    font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=350, height=490)


        # Entry fields and labels for customer details
        lbl_cust_fname = Label(labelframeleft, text="First name:", font=("times new roman", 12, "bold"))
        lbl_cust_fname.grid(row=0, column=0, padx=2, pady=5, sticky=W)
        self.entry_cust_fname = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_cust_fname.grid(row=0, column=1, padx=2, pady=5)

        lbl_cust_lname = Label(labelframeleft, text="Last name:", font=("times new roman", 12, "bold"))
        lbl_cust_lname.grid(row=1, column=0, padx=2, pady=5, sticky=W)
        self.entry_cust_lname = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_cust_lname.grid(row=1, column=1, padx=2, pady=5)

        lbl_cust_gender= Label(labelframeleft, text="Gender:", font=("times new roman", 12, "bold"))
        lbl_cust_gender.grid(row=2, column=0, sticky=W)
        self.entry_cust_gender = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_cust_gender.grid(row=2, column=1, padx=2, pady=5)


        lbl_cust_address = Label(labelframeleft, text="Address:", font=("times new roman", 12, "bold"))
        lbl_cust_address.grid(row=3, column=0, padx=2, pady=5, sticky=W)
        self.entry_cust_address = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_cust_address.grid(row=3, column=1, padx=2, pady=5)

        lbl_cust_contact = Label(labelframeleft, text="Contact:", font=("times new roman", 12, "bold"))
        lbl_cust_contact.grid(row=4, column=0, padx=2, pady=5, sticky=W)
        self.entry_cust_contact = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_cust_contact.grid(row=4, column=1, padx=2, pady=5)

        lbl_cust_email = Label(labelframeleft, text="Email:", font=("times new roman", 12, "bold"))
        lbl_cust_email.grid(row=5, column=0, padx=2, pady=5, sticky=W)
        self.entry_cust_email = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_cust_email.grid(row=5, column=1, padx=2, pady=5)

        lbl_cust_id = Label(labelframeleft, text="Id(if update/delete):", font=("times new roman", 12, "bold"))
        lbl_cust_id.grid(row=6, column=0, padx=2, pady=5, sticky=W)
        self.entry_cust_id = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_cust_id.grid(row=6, column=1, padx=2, pady=5)


        # buttons
        img = Image.open("C:/Users/48882/PycharmProjects/AIRmanagement/images/rubbish.png")
        img = img.resize((40, 40), Image.Resampling.LANCZOS)
        self.rubbish_img = ImageTk.PhotoImage(img)

        # Add the image button
        self.image_button = Button(labelframeleft,command=self.unknown, image=self.rubbish_img, bg="black")
        self.image_button.place(x=150, y=260)


        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=430, width=330, height=40)

        btnAdd = Button(btn_frame, text="Add", font=("arial", 11, "bold"), command=self.add_pass,bg="black", fg="white", width=6)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("arial", 11, "bold"),command=self.update, bg="black", fg="white", width=6)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 11, "bold"),command=self.delete, bg="black", fg="white", width=6)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 11, "bold"),command=self.reset, bg="black", fg="white", width=6)
        btnReset.grid(row=0, column=3, padx=1)

        btnleave = Button(btn_frame, text="Leave", font=("arial", 11, "bold"),command=self.leave, bg="black", fg="white", width=6)
        btnleave.grid(row=0, column=4, padx=1)

        # ============================table frame======================================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details",
                                 font=("times new roman", 12, "bold"))
        Table_Frame.place(x=360, y=50, width=750, height=490)

        lblSearchBy=Label(Table_Frame, font=("arial", 11, "bold"), text="Search By:", bg="grey", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)


        self.serch_var=StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.serch_var, font=("times new roman", 12, "bold"), width=27, state="readonly")
        combo_search["value"] = ("Id", "first name", "last name", "gender", "adress", "email")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=6)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search, font=("times new roman", 12, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch=Button(Table_Frame,text="Search", font=("arial", 11, "bold"),command=self.search, bg= "black", fg="white", width=10)
        btnSearch.grid(row=0, column=3, padx=1)
        btnSearch = Button(Table_Frame, text="Show All", font=("arial", 11, "bold"),command=self.fetch_data, bg="black", fg="white", width=10)
        btnSearch.grid(row=0, column=4, padx=1)


        # show data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=740, height=400)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        self.customer_table = ttk.Treeview(details_table, columns=("ID", "name","lname", "gender", "Address","contact","email"), xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)

        self.customer_table.heading("ID", text="ID")
        self.customer_table.heading("name", text="First_Name")
        self.customer_table.heading("lname", text="Last_Name")
        self.customer_table.heading("gender", text="Gender")
        self.customer_table.heading("Address", text="Address")
        self.customer_table.heading("contact", text="Contact")
        self.customer_table.heading("email", text="Email")

        self.customer_table["show"] = "headings"
        self.customer_table.column("ID", width=15)
        self.customer_table.column("name", width=15)
        self.customer_table.column("lname", width=15)
        self.customer_table.column("gender", width=15)
        self.customer_table.column("Address", width=15)
        self.customer_table.column("contact", width=15)
        self.customer_table.column("email", width=15)
        self.customer_table.pack(fill=BOTH, expand=1)


        self.fetch_data()
    def leave(self):
        self.root.destroy()

    def add_pass(self):
        if (self.entry_cust_fname.get() == "" or self.entry_cust_lname.get() == "" or
                self.entry_cust_email.get() == ""):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root",password="new_password", database="plane_management")
                my_cursor = conn.cursor()

                # check if the user already exists in the database
                query = "SELECT * FROM PASSENGERS WHERE email = %s"
                value = (self.entry_cust_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row:
                    messagebox.showerror("Error", "User already exists")
                else:
                    # Add the new user to the database
                    query = "INSERT INTO PASSENGERS (First_name, Last_name, Gender, Address, Contact, email, Last_active) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    values = (self.entry_cust_fname.get(), self.entry_cust_lname.get(), self.entry_cust_gender.get(),
                              self.entry_cust_address.get(), self.entry_cust_contact.get(), self.entry_cust_email.get(),
                              datetime.datetime.now().date())
                    my_cursor.execute(query, values)

                    conn.commit()
                    self.fetch_data()
                    conn.close()

                    messagebox.showinfo("Success", "Passenger added successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"MySQL Error: {str(e)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="new_password",database="plane_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from passengers")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.customer_table.delete(*self.customer_table.get_children())
            for i in rows:
                self.customer_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def update(self):
        if self.entry_cust_id.get() == "":
            messagebox.showerror("Error", "ID field is required for updating")
        elif self.entry_cust_fname.get() == "" or self.entry_cust_lname.get() == "":
            messagebox.showerror("Error", "First name and Last name are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root",password="new_password", database="plane_management")
                my_cursor = conn.cursor()

                # Update the user in the database
                query = "UPDATE PASSENGERS SET First_name = %s, Last_name = %s, Address = %s WHERE id = %s"
                values = (self.entry_cust_fname.get(), self.entry_cust_lname.get(), self.entry_cust_address.get(),
                          self.entry_cust_id.get())
                my_cursor.execute(query, values)

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Passenger updated successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"MySQL Error: {str(e)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

    def delete(self):
        if self.entry_cust_id.get() == "":
            messagebox.showerror("Error", "ID field is required for deleting")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root",password="new_password",database="plane_management")
                my_cursor = conn.cursor()

                # Delete the user from the database
                query = "DELETE FROM PASSENGERS WHERE id = %s"
                values = (self.entry_cust_id.get(),)
                my_cursor.execute(query, values)

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Passenger deleted successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"MySQL Error: {str(e)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")



    def reset(self):
        self.entry_cust_fname.delete(0, 'end')
        self.entry_cust_lname.delete(0, 'end')
        self.entry_cust_gender.delete(0, 'end')
        self.entry_cust_address.delete(0, 'end')
        self.entry_cust_contact.delete(0, 'end')
        self.entry_cust_email.delete(0, 'end')
        self.entry_cust_id.delete(0, 'end')

    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="new_password",database="plane_management")
        my_cursor = conn.cursor()

        try:
            # Properly construct the SQL query using parameterized query to prevent SQL injection
            search_criteria = self.serch_var.get()
            search_value = self.txt_search.get()

            # Adjust the SQL query based on the selected search criteria
            if search_criteria == "Id":
                query = "SELECT * FROM passengers WHERE id = %s"
            elif search_criteria == "first name":
                query = "SELECT * FROM passengers WHERE First_name = %s"
            elif search_criteria == "last name":
                query = "SELECT * FROM passengers WHERE Last_name = %s"
            elif search_criteria == "gender":
                query = "SELECT * FROM passengers WHERE LOWER(Gender) = %s"
                search_value = search_value.lower()
            elif search_criteria == "adress":
                query = "SELECT * FROM passengers WHERE Address = %s"
            elif search_criteria == "email":
                query = "SELECT * FROM passengers WHERE email = %s"
            else:
                messagebox.showerror("Error", "Invalid search criteria")
                return

            my_cursor.execute(query, (search_value,))
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.customer_table.delete(*self.customer_table.get_children())
                for row in rows:
                    self.customer_table.insert("", END, values=row)
                conn.commit()
            else:
                messagebox.showinfo("Info", "No records found")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"MySQL Error: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
        finally:
            conn.close()

    def unknown(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="new_password",database="plane_management")
            my_cursor = conn.cursor()


            my_cursor.execute("SET SQL_SAFE_UPDATES = 0;")
            my_cursor.execute("""
                DELETE FROM PASSENGERS
                WHERE Last_active < DATE_SUB(CURDATE(), INTERVAL 20 YEAR);
            """)

            my_cursor.execute("SET SQL_SAFE_UPDATES = 1;")

            conn.commit()

            messagebox.showinfo("Success", "Inactive passengers have been successfully deleted.")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            if (conn.is_connected()):
                my_cursor.close()
                conn.close()




if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
