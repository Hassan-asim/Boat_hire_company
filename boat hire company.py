import tkinter as tk
from tkinter import simpledialog, messagebox

class BoatRentalGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x100")
        self.master.title("Boat Rental System")

        # Initialize boat data
        self.boat_data = {i: {"available": True, "return_time": 10, "money": 0, "hours": 0} for i in range(1, 11)}

        # Create buttons for each operation
        self.rent_boat_button = tk.Button(master, text="Rent a Boat", command=self.rent_boat)
        self.rent_boat_button.pack()
        self.check_availability_button = tk.Button(master, text="Check Boat Availability", command=self.check_availability)
        self.check_availability_button.pack()
        self.daily_report_button = tk.Button(master, text="Generate Daily Report", command=self.generate_daily_report)
        self.daily_report_button.pack()

    def rent_boat(self):
        # Find available boats
        available_boats = [boat for boat, data in self.boat_data.items() if data["available"]]
        if not available_boats:
            messagebox.showinfo("No Available Boats", "No boats are currently available.")
            return

        # Show available boats and get boat number from user
        boat_number = simpledialog.askinteger("Input", f"Enter boat number from available boats: {', '.join(map(str, available_boats))}")
        if boat_number not in available_boats:
            messagebox.showerror("Error", "Invalid boat number.")
            return

        # Get hire time from user
        rental_duration = simpledialog.askfloat("Input", "Enter rental duration in hours (0.5 or 1): ")
        if rental_duration not in [0.5, 1]:
            messagebox.showerror("Error", "Invalid rental duration.")
            return

        # Update boat data
        self.boat_data[boat_number]["available"] = False
        self.boat_data[boat_number]["return_time"] += rental_duration
        self.boat_data[boat_number]["hours"] += rental_duration
        self.boat_data[boat_number]["money"] += 20 if rental_duration == 1 else 12

        messagebox.showinfo("Success", f"Boat {boat_number} rented for {rental_duration} hours.")

    def check_availability(self):
        # Find next available boat
        available_boats = [boat for boat, data in self.boat_data.items() if data["available"]]
        if available_boats:
            messagebox.showinfo("Available Boats", f"Boats {', '.join(map(str, available_boats))} are available.")
        else:
            # Find earliest return time
            earliest_return = min(self.boat_data.items(), key=lambda x: x[1]["return_time"])
            messagebox.showinfo("Next Available Boat", f"No boats are currently available. Boat {earliest_return[0]} will be available at {earliest_return[1]['return_time']}.")

    def generate_daily_report(self):
        # Calculate total money and hours
        total_money = sum(boat["money"] for boat in self.boat_data.values())
        total_hours = sum(boat["hours"] for boat in self.boat_data.values())

        # Find unused and most used boats
        unused_boats = [boat for boat, data in self.boat_data.items() if data["hours"] == 0]
        most_used_boat = max(self.boat_data.items(), key=lambda x: x[1]["hours"])[0]

        # Display report
        report = f"Total money: ${total_money}\nTotal hours: {total_hours}\nUnused boats: {', '.join(map(str, unused_boats)) if unused_boats else 'None'}\nMost used boat: {most_used_boat}"
        messagebox.showinfo("Daily Report", report)

root = tk.Tk()
app = BoatRentalGUI(root)
root.mainloop()
