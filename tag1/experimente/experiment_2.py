import decimal
import tkinter as tk
from tkinter import messagebox, ttk


def verarbeiten() -> None:
    try:
        name = name_eingabe.get().strip()
        adresse = adresse_eingabe.get().strip()
        alter = int(alter_eingabe.get())
        kontostand = decimal.Decimal(
            kontostand_eingabe.get().strip().replace(",", ".")
        )

        if alter < 0 or not kontostand.is_finite():
            raise ValueError

        kontostand += decimal.Decimal("3500.00")

        ausgabe.set(f"{name}, {adresse}, {alter}, {kontostand:.2f} €")

    except (ValueError, decimal.InvalidOperation):
        messagebox.showerror(
            "Ungültige Eingabe",
            "Bitte Alter als ganze, nicht negative Zahl und "
            "Kontostand als gültige Zahl eingeben.",
            parent=fenster,
        )


fenster = tk.Tk()
fenster.title("Kontostand berechnen")
fenster.geometry("560x300")

formular = ttk.Frame(fenster, padding=20)
formular.grid(row=0, column=0, sticky="nsew")

fenster.columnconfigure(0, weight=1)
fenster.rowconfigure(0, weight=1)
formular.columnconfigure(1, weight=1)

ttk.Label(formular, text="Name:").grid(
    row=0, column=0, sticky="w", pady=5
)
name_eingabe = ttk.Entry(formular)
name_eingabe.grid(row=0, column=1, sticky="ew", pady=5)

ttk.Label(formular, text="Alter:").grid(
    row=1, column=0, sticky="w", pady=5
)
alter_eingabe = ttk.Entry(formular)
alter_eingabe.grid(row=1, column=1, sticky="ew", pady=5)

ttk.Label(formular, text="Adresse:").grid(
    row=2, column=0, sticky="w", pady=5
)
adresse_eingabe = ttk.Entry(formular)
adresse_eingabe.grid(row=2, column=1, sticky="ew", pady=5)

ttk.Label(formular, text="Kontostand (€):").grid(
    row=3, column=0, sticky="w", padx=(0, 15), pady=5
)
kontostand_eingabe = ttk.Entry(formular)
kontostand_eingabe.grid(row=3, column=1, sticky="ew", pady=5)

ttk.Button(
    formular,
    text="3.500 € hinzufügen",
    command=verarbeiten,
).grid(row=4, column=0, columnspan=2, pady=15)

ausgabe = tk.StringVar()
ttk.Label(formular, textvariable=ausgabe, wraplength=500).grid(
    row=5, column=0, columnspan=2, sticky="w"
)

fenster.bind("<Return>", lambda event: verarbeiten())
name_eingabe.focus_set()

fenster.mainloop()
