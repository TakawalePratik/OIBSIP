import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


conn = sqlite3.connect("bmi_data.db")
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS bmi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        weight REAL,
        height REAL,
        bmi REAL
    )
''')
conn.commit()


def save_bmi(date, weight, height, bmi):
    c.execute("INSERT INTO bmi (date, weight, height, bmi) VALUES (?, ?, ?, ?)",
                   (date, weight, height, bmi))
    conn.commit()

def plot_bmi():
    c.execute("SELECT date, bmi FROM bmi")
    data = c.fetchall()

    if not data:
        messagebox.showinfo("No Data", "No BMI data available.")
        return

    dates, bmis = zip(*data)
    x = np.arange(len(dates))

    fig, ax = plt.subplots()
    ax.plot(x, bmis, marker='o', linestyle='-', color='b')
    ax.set_xticks(x)
    ax.set_xticklabels(dates, rotation=45, ha="right")
    ax.set_xlabel("Date")
    ax.set_ylabel("BMI")
    ax.set_title("BMI Trend Over Time")

    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=root)
    cw = canvas.get_tk_widget()
    cw.grid(row=6, column=0, columnspan=3)

def calc_bmi():
    try:
        w = float(w_entry.get())
        h = float(h_entry.get())

        bmi = w / (h ** 2)
        date = d_entry.get()

        r_label.config(text=f"BMI: {bmi:.2f}")

        save_bmi(date, w, h, bmi)

        plot_bmi()

    except ValueError:
        messagebox.showerror("Error", "Invalid input."," Please enter numeric values for weight and height.")

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Date:").grid(row=0, column=0, padx=10, pady=10)
d_entry = tk.Entry(root)
d_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
w_entry = tk.Entry(root)
w_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Height (m):").grid(row=2, column=0, padx=10, pady=10)
h_entry = tk.Entry(root)
h_entry.grid(row=2, column=1, padx=10, pady=10)

calc_button = tk.Button(root, text="Calculate BMI", command=calc_bmi)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

r_label = tk.Label(root, text="")
r_label.grid(row=4, column=0, columnspan=2, pady=10)

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.grid(row=5, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root.mainloop()
    conn.close()
