import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# ---------------------------------------------------
# ✅ SAFE DATA LOADER WITH ERROR HANDLING
# ---------------------------------------------------
def load_data(filename="weatherr.csv"):
    if not os.path.exists(filename):
        messagebox.showerror("File Error", f"CSV file '{filename}' not found!")
        return {}

    data = {}

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            required_columns = {"City", "Day", "Temperature"}

            # ✅ check for missing columns
            if not required_columns.issubset(reader.fieldnames):
                messagebox.showerror(
                    "CSV Format Error",
                    f"CSV must contain columns: {required_columns}"
                )
                return {}

            for i, row in enumerate(reader, start=2):
                try:
                    city = row["City"].strip()
                    day = int(row["Day"])
                    temp = float(row["Temperature"])
                except Exception:
                    print(f"Skipping invalid row {i}: {row}")
                    continue

                if city not in data:
                    data[city] = {"days": [], "temps": []}

                data[city]["days"].append(day)
                data[city]["temps"].append(temp)

    except Exception as e:
        messagebox.showerror("Error", f"Error reading CSV: {e}")
        return {}

    # ✅ sort data by day for each city
    for city in data:
        combined = sorted(zip(data[city]["days"], data[city]["temps"]))
        data[city]["days"], data[city]["temps"] = zip(*combined)

    return data

weather_data = load_data()

# ---------------------------------------------------
# ✅ FUNCTION TO PLOT DATA
# ---------------------------------------------------
def show_graph():
    city = city_var.get()

    if not city:
        messagebox.showwarning("Selection Error", "Please select a city!")
        return

    if city not in weather_data:
        messagebox.showerror("Data Error", "No data available for selected city!")
        return

    days = np.array(weather_data[city]["days"])
    temps = np.array(weather_data[city]["temps"])

    if len(days) == 0:
        messagebox.showerror("Data Error", f"No temperature records for {city}.")
        return

    # ✅ NumPy Calculations
    avg = np.mean(temps)
    mx = np.max(temps)
    mn = np.min(temps)

    result_label.config(
        text=f"City: {city}\nAvg: {avg:.2f}°C | Max: {mx:.1f}°C | Min: {mn:.1f}°C"
    )

    # ✅ Plot Matplotlib Graph
    plt.figure(figsize=(5,4))
    plt.plot(days, temps, marker="o")
    plt.title(f"Temperature Trend - {city}")
    plt.xlabel("Day")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ---------------------------------------------------
# ✅ TKINTER USER INTERFACE
# ---------------------------------------------------
root = tk.Tk()
root.title("Weather Data Visualizer")
root.geometry("400x350")

tk.Label(root, text="Select City", font=("Arial", 12)).pack(pady=10)

city_var = tk.StringVar()
city_dropdown = ttk.Combobox(root, textvariable=city_var, state="readonly")

# ✅ Load city names only if data exists
city_dropdown["values"] = list(weather_data.keys()) if weather_data else []
city_dropdown.pack(pady=5)

tk.Button(root, text="Show Temperature Graph", command=show_graph).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
