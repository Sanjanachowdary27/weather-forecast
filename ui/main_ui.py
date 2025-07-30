import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from search.search_feature import search_by_date, search_by_range
from ml.predictor import predict_next_30_days
from monsoon.monsoon_check import predict_monsoon

# === Initialize Window ===
root = tk.Tk()
root.title("🌦️ Weather Forecast System")
root.geometry("1020x720")
root.configure(bg="#f0f4f8")

# === Modern Style ===
style = ttk.Style()
style.theme_use("clam")

style.configure("TNotebook.Tab", font=("Segoe UI", 11, "bold"), padding=[10, 6])
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TLabel", font=("Segoe UI", 11), background="#f0f4f8")
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("TFrame", background="#f0f4f8")

# === Create Notebook (Tabs) ===
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

# === Utility: Placeholder Function ===
def add_placeholder(entry_widget, placeholder_text):
    def on_focus_in(event):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, tk.END)
            entry_widget.config(foreground="black")

    def on_focus_out(event):
        if not entry_widget.get():
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(foreground="gray")

    entry_widget.insert(0, placeholder_text)
    entry_widget.config(foreground="gray")
    entry_widget.bind("<FocusIn>", on_focus_in)
    entry_widget.bind("<FocusOut>", on_focus_out)

# ====================== TAB 1: SEARCH ======================
tab_search = ttk.Frame(notebook)
notebook.add(tab_search, text="Search")

tk.Label(tab_search, text="Search by Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
date_entry = ttk.Entry(tab_search, width=30)
add_placeholder(date_entry, "2025-06-15")
date_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")

ttk.Button(tab_search, text="Search Date", command=lambda: handle_search("date")).grid(row=1, column=1, padx=10)

tk.Label(tab_search, text="Search by Date Range:").grid(row=2, column=0, padx=10, pady=(20, 5), sticky="w")
range_start = ttk.Entry(tab_search, width=30)
add_placeholder(range_start, "Start Date (YYYY-MM-DD)")
range_start.grid(row=3, column=0, padx=10, pady=2)

range_end = ttk.Entry(tab_search, width=30)
add_placeholder(range_end, "End Date (YYYY-MM-DD)")
range_end.grid(row=3, column=1, padx=10, pady=2)

ttk.Button(tab_search, text="Search Range", command=lambda: handle_search("range")).grid(row=4, column=0, padx=10, pady=5)

output_search = scrolledtext.ScrolledText(tab_search, width=120, height=25, font=("Courier New", 10), wrap="word", bg="#fefefe")
output_search.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# ====================== TAB 2: FORECAST ======================
tab_forecast = ttk.Frame(notebook)
notebook.add(tab_forecast, text="30-Day Forecast")

ttk.Button(tab_forecast, text="Generate Forecast", command=lambda: handle_forecast()).pack(pady=10)
forecast_output = scrolledtext.ScrolledText(tab_forecast, width=120, height=30, font=("Courier New", 10), wrap="word", bg="#fefefe")
forecast_output.pack(pady=10)

# ====================== TAB 3: MONSOON ======================
tab_monsoon = ttk.Frame(notebook)
notebook.add(tab_monsoon, text="☔ Monsoon Checker")

tk.Label(tab_monsoon, text="Enter Weather Conditions:", font=("Segoe UI", 13, "bold")).pack(pady=(20, 10))

entry_temp = ttk.Entry(tab_monsoon, width=30)
add_placeholder(entry_temp, "Temperature (°C)")
entry_temp.pack(pady=5)

entry_hum = ttk.Entry(tab_monsoon, width=30)
add_placeholder(entry_hum, "Humidity (%)")
entry_hum.pack(pady=5)

entry_wind = ttk.Entry(tab_monsoon, width=30)
add_placeholder(entry_wind, "Wind Speed (km/h)")
entry_wind.pack(pady=5)

ttk.Button(tab_monsoon, text="☔ Predict Monsoon", command=lambda: handle_monsoon()).pack(pady=10)

monsoon_result = tk.Label(tab_monsoon, text="", font=("Segoe UI", 12), bg="#f0f4f8")
monsoon_result.pack(pady=10)

# ====================== Functions ======================

def handle_search(mode):
    try:
        if mode == "date":
            date = date_entry.get()
            result = search_by_date(date)
        else:
            start = range_start.get()
            end = range_end.get()
            result = search_by_range(start, end)

        output_search.delete(1.0, tk.END)
        if result.empty:
            output_search.insert(tk.END, "No matching weather data found.")
        else:
            output_search.insert(tk.END, result.to_string(index=False))

    except Exception as e:
        messagebox.showerror("Error", str(e))

def handle_forecast():
    try:
        df = predict_next_30_days()
        forecast_output.delete(1.0, tk.END)
        forecast_output.insert(tk.END, df.to_string(index=False))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def handle_monsoon():
    try:
        temp = float(entry_temp.get())
        hum = float(entry_hum.get())
        wind = float(entry_wind.get())

        rainfall, percent, is_monsoon = predict_monsoon(temp, hum, wind)

        monsoon_result.config(
            text=f"🌧️ Predicted Rainfall: {rainfall} mm\n💧 Monsoon Likelihood: {percent}%\n☔ Monsoon: {'Yes' if is_monsoon else 'No'}",
            fg="green" if is_monsoon else "blue"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

# === Run GUI ===
root.mainloop()
