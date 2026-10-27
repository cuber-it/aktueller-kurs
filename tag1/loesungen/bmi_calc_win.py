import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def ask(prompt, default=""):
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring("Input", prompt, initialvalue=default)

def ausgabe(*args, sep=" ", end="\n"):
  root = tk.Tk()
  root.withdraw()
  text = sep.join(str(a) for a in args) + end
  messagebox.showinfo("Ausgabe", text)

# E
name = ask("Name: ")
groesse = ask("Grösse in m: ").replace(",", ".")
gewicht = ask("Gewicht in kg: ").replace(",", ".")

# V
bmi = None

groesse = float(groesse)
gewicht = float(gewicht)

bmi = gewicht / (groesse ** 2)

# A
ausgabe(f"Ist gut: {bmi:.2f} - {18.5 <= bmi <= 24.9}")
