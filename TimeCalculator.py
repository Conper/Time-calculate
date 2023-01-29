import datetime
import time
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("800x550")
window.resizable(False,False)
window.configure(background="#91a3e1")
tk.Wm.wm_title(window, "Time Calculator")
year = tk.StringVar(window)
month = tk.StringVar(window)
day = tk.StringVar(window)
result = tk.StringVar(window)
res = tk.StringVar(window)


def calcul():
    year1 = int(year.get())
    month1 = int(month.get())
    day1 = int(day.get())
    date = datetime.datetime(year1, month1, day1)
    difference = date - datetime.datetime.now()
    res.set(difference)


tk.Label(
    window,
    text="CALCULATOR DAYS 🕔",
    fg="Black",
    bg="#ffcc99",
    font=("Calibri", 35),
    bd=2,
    relief="solid"
).pack(fill=tk.BOTH)

year_l = tk.Label(
    window,
    text="Year:",
    fg="White",
    bg="#0066cc",
    font=("Calibri", 30),
    bd=2,
    relief="solid",
    padx=40,
    pady=20
    ).place(x=50, y=90)

month_l = tk.Label(
    window,
    text="Month:",
    fg="White",
    bg="#0066cc",
    font=("Calibri", 30),
    bd=2,
    relief="solid",
    padx=40,
    pady=20
    ).place(x=50, y=190)

day_l = tk.Label(
    window,
    text="Day:",
    fg="White",
    bg="#0066cc",
    font=("Calibri", 30),
    bd=2,
    relief="solid",
    padx=40,
    pady=20
    ).place(x=50, y=290)

year_e = tk.Entry(
    window,
    bg="#6666ff",
    fg="White",
    font=("Calibri", 30),
    bd=2,
    relief="solid",
    justify="center",
    width=15,
    textvariable=year
).place(x=400, y=90, height=75)

month_e = tk.Entry(
    window,
    bg="#6666ff",
    fg="White",
    font=("Calibri", 30),
    bd=2,
    relief="solid",
    justify="center",
    width=15,
    textvariable=month
).place(x=400, y=190, height=75)

day_e = tk.Entry(
    window,
    bg="#6666ff",
    fg="White",
    font=("Calibri", 30),
    bd=2,
    relief="solid",
    justify="center",
    width=15,
    textvariable=day
).place(x=400, y=300, height=75)

tk.Button(
    window,
    text="Calculate",
    bg="#6666ff",
    fg="White",
    font=("Calibri", 30),
    bd=10,
    border=5,
    relief="raised",
    width=10,
    command=calcul
).place(x=480, y=407)

result = tk.Label(
    window,
    textvariable=res,
    bg="#99ff66",
    fg="Black",
    font=("Calibri", 22),
    bd=2,
    relief="solid",
    width=26,
).place(x=50, y=420, height=80)

window.mainloop()