
# ✈️ Flight Management System with Tkinter

This Python application is a basic flight management system using the Tkinter library for GUI interaction. It allows users to manage flights, search for specific flights, manage seats, calculate seat occupation, and generate a report of all flights.

## 🔧 Features

- **Flight Search**: Search for existing flights by code.
- **Flight Management**: Add a new flight if it doesn't already exist.
- **Seat Management**: Remove a selected seat from a flight.
- **Occupation Management**: Calculate the percentage of occupied seats (from a total of 50 seats).
- **Report Generator**: Export a report of all flights sorted by time into a `report.txt` file.
- **Flight Display**: Shows all flight information in a scrollable window.

## 🖥️ GUI Inputs

- **Flight Code**: Split into letters and numbers.
- **Date**: Format `DD/MM/YYYY`.
- **Hour and Minutes**: For flight schedule.
- **Origin and Destination**: Cities.
- **Seats**: Enter a seat (e.g., `A24`).
- **Wish Seats**: Input to book a seat.

## 🗂️ Code Data Structure

Flight data is stored in a Python dictionary called `code`. Each flight code maps to:
- `origen`: Origin city
- `destination`: Destination city
- `seat_list`: List of available seats
- `schedule`: Tuple of (hour, minutes)

## 📝 Example Code Snippet

```python
code = {
    "AA-646": {
        "origen": "Singapur",
        "destination": "Colombia",
        "seat_list": ["A24","A25","B38","C40"],
        "schedule": (23, 50)
    }
}
```

## 📋 Notes

- The app uses `messagebox` for error and information prompts.
- Seats are removed from flights once booked.
- The system only allows flight creation if the date is not today.
- `report.txt` is overwritten with each generation.

## 🧱 Requirements

- Python 3.6 or higher
- tkinter (standard with most Python installations)

## 🚀 To Run

1. Make sure you have Python installed.
2. Run the script with:
   ```bash
   python flight_management.py
   ```

## 📌 Tips

- Check console output for seat list debugging.
- Ensure date is entered in the correct format or errors may occur.
