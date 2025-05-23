import datetime as dt
from datetime import datetime
today_date = dt.date.today()

import tkinter as tk
from tkinter import messagebox #Para las advertencias

code: dict = {
    "AA-646": {
        "origen": "Singapur",
        "destination": "Colombia",
        "seat_list": ["A24","A25","B38","C40"],
        "schedule": (23,50)
    },
    "BB-656": {
        "origen": "Singapur",
        "destination": "Colombia",
        "seat_list": ["A24","A25","B38","C40"],
        "schedule": (20,50)
    }
}

def actualizarInfo():
    display.delete(1.0, tk.END)
    ordenated = sorted(code.items(), key=lambda x: x[1]["schedule"])
    for key, datas in ordenated:
        linea=(
            f"{key}\n"
            f"Origen: {datas['origen']}\n"
            f"Destino: {datas['destination']}\n"
            f"Asientos: {', '.join(datas['seat_list'])}\n"
            f"Horario: {datas['schedule'][0]:02d}:{datas['schedule'][1]:02d}\n\n"
        )
        display.insert(tk.END,linea)

def search_flight ():
    letters = letters_entry.get().upper()
    numbers = numbers_entry.get()
    codes = letters+"-"+numbers
    for flight in code:
        if codes == flight:
            display.insert(tk.END,code[flight])
            break
        else:
            messagebox.showerror("Error","Non-existent flight")

def flight_manegement():
    letters = letters_entry.get().upper()
    numbers = numbers_entry.get()
    codes = letters+"-"+numbers
    schedule_str = date_label_entry.get()
    schedule_obj = datetime.strptime(schedule_str, "%d/%m/%Y") # 2025-05-07 00:00:00
    if schedule_obj != today_date:
        hour = hour_entry.get()
        minutes = minutes_entry.get()
        hours_tuple: tuple = (int(hour),int(minutes))
        if hours_tuple[0] >= 0 and hours_tuple[0] <= 23:
                if hours_tuple[1] >= 0 and hours_tuple[0] <= 59:
                    origen = origin_entry.get()
                    destination= destination_entry.get()
                    seat_list: list = []
                    seats = seats_entry.get()
                    seat_list.append(seats)
                    code[codes]={
                                "origen": origen,
                                "destination": destination,
                                "seat_list": seat_list,
                                "schedule": hours_tuple
                    }
                    messagebox.showinfo("Flight correctly save", display.insert(tk.END,code[codes]))
                    actualizarInfo()
                    return 
                else:
                    messagebox.showerror("Error","Minutes incorrect")
                    return
        else:
                messagebox.showerror("Error","Hours incorrect")
                return
    else:
            messagebox.showerror("Error","Date incorrect")
            return

def seats ():
    for name, flight in code.items():
        print(flight['seat_list'])
        seat = wish_seats_entry.get()
        for f in flight['seat_list']:
            if seat == f:
                flight['seat_list'].remove(seat)
                messagebox.showinfo("Seat correctly save", flight['seat_list'])
                actualizarInfo()
                return
            else:
                messagebox.showerror("Error","Seat not available")
                break

def occupation ():
    seat_oc: int = 50
    count: int = 0
    for name, seat in code.items():
        for f in seat['seat_list']:
            count += 1
    porcent = count / seat_oc
    porcent = porcent * 100
    messagebox.showinfo("The free occupation porcent of the flight", porcent)


def report_generator():
    report = open("report.txt", "w")
    ordenated = sorted(code.items(), key=lambda x: x[1]["schedule"])
    for key, datas in ordenated:
        report.write(
            f"{key}\n"
            f"Origen: {datas['origen']}\n"
            f"Destino: {datas['destination']}\n"
            f"Asientos: {', '.join(datas['seat_list'])}\n"
            f"Horario: {datas['schedule'][0]:02d}:{datas['schedule'][1]:02d}\n\n"
        )


root = tk.Tk() 
root.title("FLIGHTS MANEGEMENT") #El nombre que aparecera en la parte izq superior

letters_label = tk.Label(root, text="Code's letters")
letters_label.grid(row=0,column=1)
letters_entry = tk.Entry(root)
letters_entry.grid(row=0,column=2)

numbers_label = tk.Label(root, text="Code's numbers")
numbers_label.grid(row=1,column=1)
numbers_entry = tk.Entry(root)
numbers_entry.grid(row=1,column=2)

date_label = tk.Label(root, text= "Flight's date")
date_label.grid(row=2,column=1)
date_label_entry = tk.Entry(root)
date_label_entry.grid(row=2,column=2)

seats_label = tk.Label(root, text= "Seats")
seats_label.grid(row=3,column=1)
seats_entry = tk.Entry(root)
seats_entry.grid(row=3,column=2)

hour_label = tk.Label(root, text= "Hour")
hour_label.grid(row=4,column=1)
hour_entry = tk.Entry(root)
hour_entry.grid(row=4,column=2)

minutes_label = tk.Label(root, text= "Minutes")
minutes_label.grid(row=5,column=1)
minutes_entry = tk.Entry(root)
minutes_entry.grid(row=5,column=2)

origin_label = tk.Label(root, text= "Origin city")
origin_label.grid(row=6,column=1)
origin_entry= tk.Entry(root)
origin_entry.grid(row=6,column=2)

destination_label = tk.Label(root, text= "Destination city")
destination_label.grid(row=7,column=1)
destination_entry= tk.Entry(root)
destination_entry.grid(row=7,column=2)

wish_seats_label = tk.Label(root, text= "Wish seats")
wish_seats_label.grid(row=8,column=1)
wish_seats_entry = tk.Entry(root)
wish_seats_entry.grid(row=8,column=2)

flight_manegement_buttom = tk.Button(root,text="Flight manegement", anchor="center",command=flight_manegement)
flight_manegement_buttom.grid(row=7,column=0)

seat_buttom = tk.Button(root,text="Seat manegement", anchor="center",command=seats)
seat_buttom.grid(row=8,column=0)

occupation_buttom = tk.Button(root,text="Occupation manegenment", anchor="center",command=occupation)
occupation_buttom.grid(row=9,column=0)

report_buttom = tk.Button(root,text="Report generator", anchor="center",command=report_generator)
report_buttom.grid(row=9,column=3)

search_buttom = tk.Button(root,text="Search flight", anchor="center",command=search_flight)
search_buttom.grid(row=8,column=3)

display = tk.Text(root, height=20, width=120)
display.grid(row=11, column=0, columnspan=5)


root.mainloop() # Sin esa línea, la ventana aparecería por una fracción de segundo y se cerraría de inmediato.