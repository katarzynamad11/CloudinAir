from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from datetime import datetime


class Win2:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservations")
        self.root.geometry("1120x550+326+226")

        lbl_title = Label(self.root, text="Reservations", font=("times new roman", 15, "bold"), bg="black", fg="white")
        lbl_title.place(x=0, y=0, width=1120, height=50)

        # Input Fields
        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_gender = StringVar()
        self.var_address = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_flight_date = StringVar()
        self.var_departure_location = StringVar()
        self.var_destination_location = StringVar()



        lbl_first_name = Label(self.root, text="First Name", font=("arial", 12, "bold"))
        lbl_first_name.place(x=50, y=80)
        entry_first_name = Entry(self.root, textvariable=self.var_first_name, font=("arial", 12, "bold"))
        entry_first_name.place(x=250, y=80)

        lbl_last_name = Label(self.root, text="Last Name", font=("arial", 12, "bold"))
        lbl_last_name.place(x=50, y=120)
        entry_last_name = Entry(self.root, textvariable=self.var_last_name, font=("arial", 12, "bold"))
        entry_last_name.place(x=250, y=120)

        lbl_flight_date = Label(self.root, text="Flight Date (YYYY-MM-DD)", font=("arial", 12, "bold"))
        lbl_flight_date.place(x=50, y=160)
        entry_flight_date = Entry(self.root, textvariable=self.var_flight_date, font=("arial", 12, "bold"))
        entry_flight_date.place(x=250, y=160)

        lbl_departure_location = Label(self.root, text="Departure Location", font=("arial", 12, "bold"))
        lbl_departure_location.place(x=50, y=200)
        entry_departure_location = Entry(self.root, textvariable=self.var_departure_location,
                                         font=("arial", 12, "bold"))
        entry_departure_location.place(x=250, y=200)

        lbl_destination_location = Label(self.root, text="Destination Location", font=("arial", 12, "bold"))
        lbl_destination_location.place(x=50, y=240)
        entry_destination_location = Entry(self.root, textvariable=self.var_destination_location,
                                           font=("arial", 12, "bold"))
        entry_destination_location.place(x=250, y=240)

        btn_check_user = Button(self.root, text="Check User", command=self.check_user, font=("arial", 12, "bold"),
                                bg="black", fg="white")
        btn_check_user.place(x=50, y=280, width=150, height=30)

        self.additional_info_frame = Frame(self.root)
        self.additional_info_frame.place(x=50, y=200, width=80, height=0)

        self.btn_reserve = Button(self.root, text="Reserve", command=self.make_reservation, font=("arial", 12, "bold"),
                                  bg="black", fg="white")
        self.btn_reserve.place(x=50, y=510, width=150, height=30)


        self.btn_reserve2 = Button(self.root, text="Refresh Data", command=self.fetch_data, font=("arial", 12, "bold"),
                                  bg="black", fg="white")
        self.btn_reserve2.place(x=250, y=510, width=150, height=30)

        self.btn_reserve1 = Button(self.root, text="X", command=self.leave, font=("arial", 12, "bold"),
                                  bg="black", fg="white")
        self.btn_reserve1.place(x=430, y=510, width=15, height=30)

#============================================================

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details",
                                 font=("times new roman", 12, "bold"))
        Table_Frame.place(x=450, y=50, width=650, height=490)



        # show data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=15, width=650, height=450)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        self.customer_table = ttk.Treeview(details_table,
                                           columns=("ID", "name", "lname", "gender", "Address1","Address"),
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)

        self.customer_table.heading("ID", text="Departure Location")
        self.customer_table.heading("name", text="Destination Location")
        self.customer_table.heading("lname", text="Flight date")
        self.customer_table.heading("gender", text="Available Seats")
        self.customer_table.heading("Address1", text="Total Seats")
        self.customer_table.heading("Address", text="Airline Name")


        self.customer_table["show"] = "headings"
        self.customer_table.column("ID", width=10)
        self.customer_table.column("name", width=10)
        self.customer_table.column("lname", width=10)
        self.customer_table.column("gender", width=10)
        self.customer_table.column("Address1", width=10)
        self.customer_table.column("Address", width=10)

        self.customer_table.pack(fill=BOTH, expand=1)

        self.fetch_data()


        #============================

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
        my_cursor = conn.cursor()
        query = """
        SELECT AF.departure_location, AF.destination_location, AF.flight_date, AF.available_seats, A.total_seats, A.airline_name
        FROM AVAILABLE_FLIGHTS AF
        INNER JOIN AIRLINES A ON AF.airline_id = A.id
        """
        my_cursor.execute(query)
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.customer_table.delete(*self.customer_table.get_children())
            for row in rows:
                self.customer_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def check_user(self):
        first_name = self.var_first_name.get()
        last_name = self.var_last_name.get()

        conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
        my_cursor = conn.cursor()
        query = "SELECT id FROM PASSENGERS WHERE First_name=%s AND Last_name=%s"
        my_cursor.execute(query, (first_name, last_name))
        row = my_cursor.fetchone()

        if row:
            self.passenger_id = row[0]
            messagebox.showinfo("Info", "User found in database. Proceeding with reservation.")
            self.btn_reserve["state"] = "normal"
        else:
            messagebox.showerror("Error", "User not found. Please provide additional details.")
            self.btn_reserve["state"] = "disabled"
            self.show_additional_info_form()

        conn.close()

    def show_additional_info_form(self):
        self.additional_info_frame.destroy()
        self.additional_info_frame = Frame(self.root)
        self.additional_info_frame.place(x=50, y=320, width=400, height=150)

        lbl_gender = Label(self.additional_info_frame, text="Gender (M/F)", font=("arial", 12, "bold"))
        lbl_gender.place(x=0, y=0)
        entry_gender = Entry(self.additional_info_frame, textvariable=self.var_gender, font=("arial", 12, "bold"))
        entry_gender.place(x=200, y=0)

        lbl_address = Label(self.additional_info_frame, text="Address", font=("arial", 12, "bold"))
        lbl_address.place(x=0, y=40)
        entry_address = Entry(self.additional_info_frame, textvariable=self.var_address, font=("arial", 12, "bold"))
        entry_address.place(x=200, y=40)

        lbl_contact = Label(self.additional_info_frame, text="Contact", font=("arial", 12, "bold"))
        lbl_contact.place(x=0, y=80)
        entry_contact = Entry(self.additional_info_frame, textvariable=self.var_contact, font=("arial", 12, "bold"))
        entry_contact.place(x=200, y=80)

        lbl_email = Label(self.additional_info_frame, text="Email", font=("arial", 12, "bold"))
        lbl_email.place(x=0, y=120)
        entry_email = Entry(self.additional_info_frame, textvariable=self.var_email, font=("arial", 12, "bold"))
        entry_email.place(x=200, y=120)

        self.btn_reserve["state"] = "normal"

    def make_reservation(self):
        first_name = self.var_first_name.get()
        last_name = self.var_last_name.get()
        gender = self.var_gender.get()
        address = self.var_address.get()
        contact = self.var_contact.get()
        email = self.var_email.get()
        flight_date = self.var_flight_date.get()
        departure_location = self.var_departure_location.get()
        destination_location = self.var_destination_location.get()
        current_date = datetime.now().date()

        conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
        my_cursor = conn.cursor()

        # Find passenger ID or insert new passenger
        query = "SELECT id FROM PASSENGERS WHERE First_name=%s AND Last_name=%s"
        my_cursor.execute(query, (first_name, last_name))
        row = my_cursor.fetchone()

        if row:
            passenger_id = row[0]
        else:
            query = "INSERT INTO PASSENGERS (First_name, Last_name, Gender, Address, Contact, email, Last_active) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            my_cursor.execute(query, (first_name, last_name, gender, address, contact, email, current_date))
            passenger_id = my_cursor.lastrowid
            conn.commit()

        # Find available flight
        query = """
         SELECT id, available_seats FROM AVAILABLE_FLIGHTS
         WHERE departure_location=%s AND destination_location=%s AND flight_date=%s
         """
        my_cursor.execute(query, (departure_location, destination_location, flight_date))
        flight = my_cursor.fetchone()

        if not flight:
            messagebox.showerror("Error", "No flight available for the selected criteria.")
            return

        flight_id, available_seats = flight

        if available_seats <= 0:
            messagebox.showerror("Error", "No available seats on the selected flight.")
            return

        # Insert reservation
        query = "INSERT INTO RESERVATIONS (passenger_id, flight_id, reservation_date) VALUES (%s, %s, %s)"
        my_cursor.execute(query, (passenger_id, flight_id, current_date))
        conn.commit()


        messagebox.showinfo("Success", "Reservation successful!")
        self.reset_form()

        conn.close()

    def save_new_passenger(self):
        first_name = self.var_first_name.get()
        last_name = self.var_last_name.get()
        gender = self.var_gender.get()
        address = self.var_address.get()
        contact = self.var_contact.get()
        email = self.var_email.get()
        last_active = datetime.now().date()

        conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
        my_cursor = conn.cursor()


        query = """
        INSERT INTO PASSENGERS (First_name, Last_name, Gender, Address, Contact, email, Last_active)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        my_cursor.execute(query, (first_name, last_name, gender, address, contact, email, last_active))
        self.passenger_id = my_cursor.lastrowid
        conn.commit()
        conn.close()

    def reset_form(self):
        self.var_first_name.set("")
        self.var_last_name.set("")
        self.var_gender.set("")
        self.var_address.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_flight_date.set("")
        self.var_departure_location.set("")
        self.var_destination_location.set("")
        self.additional_info_frame.destroy()

    def leave(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Win2(root)
    root.mainloop()
