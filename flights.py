from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from datetime import datetime

class Win3:
    def __init__(self, root):
        self.root = root
        self.root.title("Flights")
        self.root.geometry("1120x550+326+226")

        lbl_title = Label(self.root, text="Fly Management", font=("times new roman", 15, "bold"), bg="black", fg="white")
        lbl_title.place(x=0, y=0, width=1120, height=50)

        # ======================================================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Flights",
                                    font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=350, height=250)

        # Entry fields and labels for flight details
        lbl_flight_number = Label(labelframeleft, text="Flight Number:", font=("times new roman", 12, "bold"))
        lbl_flight_number.grid(row=0, column=0, padx=2, pady=5, sticky=W)
        self.entry_flight_number = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_flight_number.grid(row=0, column=1, padx=2, pady=5)

        lbl_departure_location = Label(labelframeleft, text="Departure Location:", font=("times new roman", 12, "bold"))
        lbl_departure_location.grid(row=1, column=0, padx=2, pady=5, sticky=W)
        self.entry_departure_location = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_departure_location.grid(row=1, column=1, padx=2, pady=5)

        lbl_destination_location = Label(labelframeleft, text="Destination Location:", font=("times new roman", 12, "bold"))
        lbl_destination_location.grid(row=2, column=0, padx=2, pady=5, sticky=W)
        self.entry_destination_location = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_destination_location.grid(row=2, column=1, padx=2, pady=5)

        lbl_date = Label(labelframeleft, text="Date:", font=("times new roman", 12, "bold"))
        lbl_date.grid(row=3, column=0, padx=2, pady=5, sticky=W)
        self.entry_date = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_date.grid(row=3, column=1, padx=2, pady=5)

        lbl_airline_name = Label(labelframeleft, text="Airline Name:", font=("times new roman", 12, "bold"))
        lbl_airline_name.grid(row=4, column=0, padx=2, pady=5, sticky=W)
        self.entry_airline_name = ttk.Entry(labelframeleft, width=20, font=("times new roman", 12))
        self.entry_airline_name.grid(row=4, column=1, padx=2, pady=5)

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=5, y=180, width=330, height=40)
        btnnadd = Button(btn_frame, text="Add", font=("arial", 11, "bold"), command=self.add_flight, bg="black",
                        fg="white", width=6)
        btnnadd.grid(row=0, column=0, padx=1)

        btn_refresh = Button(btn_frame, text="Reset", font=("arial", 11, "bold"), command=self.reset, bg="black",
                           fg="white", width=6)
        btn_refresh.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", font=("arial", 11, "bold"), command=self.delete_flight, bg="black",
                           fg="white", width=6)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_raport = Button(btn_frame, text="Raport", font=("arial", 11, "bold"), command=self.generate_report,
                            bg="black",
                            fg="white", width=6)
        btn_raport.grid(row=0, column=3, padx=1)

        btn_raport1 = Button(btn_frame, text="X", font=("arial", 11, "bold"), command=self.delete,
                            bg="black",
                            fg="white", width=6)
        btn_raport1.grid(row=0, column=4, padx=1)


        # Frame for recent flights
        recent_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Recent Flights", font=("times new roman", 12, "bold"))
        recent_frame.place(x=360, y=50, width=750, height=490)

        scroll_x = ttk.Scrollbar(recent_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(recent_frame, orient=VERTICAL)
        self.recent_flights_table = ttk.Treeview(recent_frame, columns=("Flight Number", "Departure Location", "Destination Location", "Date", "Available Seats", "Airline Name"),
                                                 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.recent_flights_table.xview)
        scroll_y.config(command=self.recent_flights_table.yview)

        self.recent_flights_table.heading("Flight Number", text="Flight Number")
        self.recent_flights_table.heading("Departure Location", text="Departure Location")
        self.recent_flights_table.heading("Destination Location", text="Destination Location")
        self.recent_flights_table.heading("Date", text="Date")
        self.recent_flights_table.heading("Available Seats", text="Available Seats")
        self.recent_flights_table.heading("Airline Name", text="Airline Name")

        self.recent_flights_table["show"] = "headings"
        self.recent_flights_table.column("Flight Number", width=100)
        self.recent_flights_table.column("Departure Location", width=150)
        self.recent_flights_table.column("Destination Location", width=150)
        self.recent_flights_table.column("Date", width=100)
        self.recent_flights_table.column("Available Seats", width=100)
        self.recent_flights_table.column("Airline Name", width=150)

        self.recent_flights_table.pack(fill=BOTH, expand=1)

        self.refresh_flights()

    def add_flight(self):
        # Pobierz wartości z formularza
        flight_number = self.entry_flight_number.get()
        departure_location = self.entry_departure_location.get()
        destination_location = self.entry_destination_location.get()
        flight_date = self.entry_date.get()
        airline_name = self.entry_airline_name.get()

        # Sprawdź, czy wszystkie pola są wypełnione
        if flight_number == "" or departure_location == "" or destination_location == "" or flight_date == "" or airline_name == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            # Połącz się z bazą danych
            conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
            my_cursor = conn.cursor()

            # Sprawdź, czy podana linia lotnicza istnieje w tabeli AIRLINES
            my_cursor.execute("SELECT id, total_seats FROM AIRLINES WHERE airline_name = %s", (airline_name,))
            airline = my_cursor.fetchone()

            if airline is None:
                messagebox.showerror("Error", "Airline not found")
                conn.close()
                return

            # Pobierz airline_id i total_seats
            airline_id = airline[0]
            total_seats = airline[1]


            query = """
            INSERT INTO AVAILABLE_FLIGHTS (flight_number, departure_location, destination_location, flight_date, available_seats, airline_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (flight_number, departure_location, destination_location, flight_date, total_seats, airline_id)
            my_cursor.execute(query, values)


            conn.commit()
            conn.close()


            self.refresh_flights()

            messagebox.showinfo("Success", "Flight added successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def delete(self):
        self.root.destroy()


    def delete_flight(self):
        if self.entry_flight_number.get() == "":
            messagebox.showerror("Error", "Flight number field is required for deleting")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
                my_cursor = conn.cursor()

                # Usuń lot z bazy danych
                query = "DELETE FROM available_flights WHERE flight_number = %s"
                values = (self.entry_flight_number.get(),)
                my_cursor.execute(query, values)

                conn.commit()
                self.refresh_flights()
                conn.close()

                messagebox.showinfo("Success", "Flight deleted successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"MySQL Error: {str(e)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

    def generate_report(self):
        try:
            # Tworzenie ramki raportu
            report_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Flight Report",
                                      font=("times new roman", 12, "bold"))
            report_frame.place(x=5, y=300, width=350, height=100)


            report_table = ttk.Treeview(report_frame,
                                        columns=("Flight Number", "Available Seats"),
                                        show="headings")
            report_table.heading("Flight Number", text="Flight Number")
            report_table.heading("Available Seats", text="Available Seats")

            report_table.column("Flight Number", width=50)
            report_table.column("Available Seats", width=50)

            conn = mysql.connector.connect(host="localhost", user="root", database="plane_management")
            my_cursor = conn.cursor()

            query = """
                SELECT flight_number, available_seats
                FROM AVAILABLE_FLIGHTS
                WHERE available_seats IN (
                    SELECT MIN(available_seats) AS min_seats
                    FROM AVAILABLE_FLIGHTS

                    UNION ALL

                    SELECT MAX(available_seats) AS max_seats
                    FROM AVAILABLE_FLIGHTS
                );
            """
            my_cursor.execute(query)
            rows = my_cursor.fetchall()

            # Wstawianie danych do tabeli raportu
            for row in rows:
                report_table.insert("", END, values=row)

            report_table.pack(fill=BOTH, expand=1)

            # Dodanie ramki dla informacji o najbliższym i najdalszym dniu lotu
            dates_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Flight Dates",
                                     font=("times new roman", 12, "bold"))
            dates_frame.place(x=5, y=400, width=350, height=100)

            # Zapytanie dla najbliższego i najdalszego dnia lotu
            min_max_query = """
                  SELECT MIN(flight_date) AS min_date, MAX(flight_date) AS max_date
                  FROM AVAILABLE_FLIGHTS;
                  """

            my_cursor.execute(min_max_query)
            min_max_data = my_cursor.fetchone()

            # Wyświetlenie informacji o najbliższym i najdalszym dniu lotu
            min_date_label = Label(dates_frame, text=f"Closest Departure Date: {min_max_data[0]}",
                                   font=("times new roman", 12))
            min_date_label.grid(row=0, column=0, padx=10, pady=5)

            max_date_label = Label(dates_frame, text=f"Furthest Departure Date: {min_max_data[1]}",
                                   font=("times new roman", 12))
            max_date_label.grid(row=1, column=0, padx=10, pady=5)


            conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"MySQL Error: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
    def refresh_flights(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="new_password", database="plane_management")
        my_cursor = conn.cursor()
        query = """
        SELECT AF.flight_number, AF.departure_location, AF.destination_location, AF.flight_date, AF.available_seats, A.airline_name
        FROM AVAILABLE_FLIGHTS AF
        INNER JOIN AIRLINES A ON AF.airline_id = A.id
        ORDER BY AF.id DESC
        LIMIT 5
        """
        my_cursor.execute(query)
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.recent_flights_table.delete(*self.recent_flights_table.get_children())
            for row in rows:
                self.recent_flights_table.insert("", END, values=row)
            conn.commit()
        conn.close()


    def reset(self):
        self.entry_flight_number.delete(0, 'end')
        self.entry_departure_location.delete(0, 'end')
        self.entry_destination_location.delete(0, 'end')
        self.entry_date.delete(0, 'end')
        self.entry_airline_name.delete(0, 'end')



if __name__ == "__main__":
    root = Tk()
    obj = Win3(root)
    root.mainloop()
