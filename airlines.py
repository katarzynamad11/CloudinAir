from tkinter import*
from tkinter import ttk
import tkinter as tk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

from PIL import Image, ImageTk


class Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Partnership Airlines")
        self.root.geometry("1120x550+326+226")

        lbl_title = Label(self.root, text="Airlines", font=("times new roman", 15, "bold"), bg="black",
                          fg="white")
        lbl_title.place(x=0, y=0, width=1120, height=50)

        # ======================================================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Manage",
                                    font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=350, height=180)


        # Entry fields and labels for customer details
        lbl_cust_aname = Label(labelframeleft, text="Airline Name:", font=("times new roman", 12, "bold"))
        lbl_cust_aname.grid(row=0, column=0, padx=2, pady=5, sticky=W)
        self.entry_cust_aname = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_cust_aname.grid(row=0, column=1, padx=2, pady=5)

        lbl_cust_seats = Label(labelframeleft, text="Total seats:", font=("times new roman", 12, "bold"))
        lbl_cust_seats.grid(row=1, column=0, padx=2, pady=5, sticky=W)
        self.entry_cust_seats = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_cust_seats.grid(row=1, column=1, padx=2, pady=5)

        lbl_cust_number= Label(labelframeleft, text="Number of planes:", font=("times new roman", 12, "bold"))
        lbl_cust_number.grid(row=2, column=0, sticky=W)
        self.entry_cust_number = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_cust_number.grid(row=2, column=1, padx=2, pady=5)


        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=83, y=110, width=330, height=30)

        btnAdd = Button(btn_frame, text="Add", font=("arial", 11, "bold"),command=self.add_pass, bg="black", fg="white", width=6)
        btnAdd.grid(row=0, column=0, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 11, "bold"),command=self.delete, bg="black", fg="white", width=6)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 11, "bold"),command=self.reset, bg="black", fg="white", width=6)
        btnReset.grid(row=0, column=3, padx=1)

        btnleave = Button(btn_frame, text="Leave", font=("arial", 11, "bold"), command=self.leave, bg="black", fg="white", width=6)
        btnleave.grid(row=0, column=4, padx=1)

        # ============================table frame======================================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details",
                                 font=("times new roman", 12, "bold"))
        Table_Frame.place(x=360, y=50, width=750, height=490)


        # show data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=10, width=740, height=150)


        self.customer_table = ttk.Treeview(details_table, columns=("ID", "airline_name","total_seats", "number_of_planes"))



        self.customer_table.heading("ID", text="ID")
        self.customer_table.heading("airline_name", text="Airline_name")
        self.customer_table.heading("total_seats", text="Total seats")
        self.customer_table.heading("number_of_planes", text="Number_of_planes")


        self.customer_table["show"] = "headings"
        self.customer_table.column("ID", width=15)
        self.customer_table.column("airline_name", width=15)
        self.customer_table.column("total_seats", width=15)
        self.customer_table.column("number_of_planes", width=15)

        self.customer_table.pack(fill=BOTH, expand=1)


        self.fetch_data()


        # frame1 - na proceudure
        report_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Procedure",
                                  font=("times new roman", 12, "bold"))
        report_frame.place(x=5, y=230, width=350, height=310)

        # Dodajemy elementy graficzne do ramki report_frame
        lbl_report_title = Label(report_frame, text="Number of available flights",
                                 font=("times new roman", 12, "bold"))
        lbl_report_title.pack(pady=5)

        # Tutaj wykonujemy zapytanie do procedury i wyświetlamy wynik
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
            my_cursor = conn.cursor()

            my_cursor.callproc('GetAirlineFlightSummary')  # Tutaj nazwa procedury

            for result in my_cursor.stored_results():
                rows = result.fetchall()
                for row in rows:
                    # Wyświetlamy wynik na etykiecie
                    lbl_result = Label(report_frame, text=row, font=("times new roman", 10))
                    lbl_result.pack(pady=2)

            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"MySQL Error: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")


        # frame2 - na widok
        report_frame1 = LabelFrame(self.root, bd=2, relief=RIDGE, text="View",
                                   font=("times new roman", 12, "bold"))
        report_frame1.place(x=362, y=230, width=740, height=310)

        # Dodajemy tabelę do wyświetlenia danych z widoku
        details_table = ttk.Treeview(report_frame1, columns=(
            "Airline Name", "Flight Number", "Available Seats", ),
                                     show="headings", height=10)

        details_table.heading("Flight Number", text="Flight Number")
        details_table.heading("Available Seats", text="Available Seats")
        details_table.heading("Airline Name", text="Airline Name")

        # Tutaj pobieramy dane z widoku i wyświetlamy je w tabeli
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT * FROM AirlineFlightDetails1")

            rows = my_cursor.fetchall()
            for row in rows:
                details_table.insert("", tk.END, values=row)

            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"MySQL Error: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

        details_table.pack(fill="both", expand=True)


    def leave(self):
        self.root.destroy()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from airlines")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.customer_table.delete(*self.customer_table.get_children())
            for i in rows:
                self.customer_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    def leave(self):
        self.root.destroy()

    def add_pass(self):
        if (self.entry_cust_aname.get() == "" or self.entry_cust_seats.get() == "" or
                self.entry_cust_number.get() == ""):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
                my_cursor = conn.cursor()

                # check if the user already exists in the database
                query = "SELECT * FROM AIRLINES WHERE airline_name = %s"
                value = (self.entry_cust_aname.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row:
                    messagebox.showerror("Error", "User already exists")
                else:
                    # Add the new user to the database
                    query = "INSERT INTO AIRLINES (airline_name, total_seats, number_of_planes) VALUES (%s, %s, %s)"
                    values = (self.entry_cust_aname.get(), self.entry_cust_seats.get(), self.entry_cust_number.get())
                    my_cursor.execute(query, values)

                    conn.commit()
                    self.fetch_data()
                    conn.close()

                    messagebox.showinfo("Success", "Airline added successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"MySQL Error: {str(e)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")


    def delete(self):
        if self.entry_cust_aname.get() == "":
            messagebox.showerror("Error", "Name field is required for deleting")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="new_password",database="plane_management")
                my_cursor = conn.cursor()

                # Delete the user from the database
                query = "DELETE FROM airlines WHERE airline_name = %s"
                values = (self.entry_cust_aname.get(),)
                my_cursor.execute(query, values)

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Airline deleted successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"MySQL Error: {str(e)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")



    def reset(self):
        self.entry_cust_aname.delete(0, 'end')
        self.entry_cust_seats.delete(0, 'end')
        self.entry_cust_number.delete(0, 'end')





if __name__ == "__main__":
    root = Tk()
    obj = Win(root)
    root.mainloop()