"""Optionaler Ausblick: Kontaktverwaltung mit Tkinter und einer Klasse.

Klassen und GUI-Ereignisse gehen über die Grundlagen von Tag 3 hinaus.
Die Konsolenaufgabe kommt ohne diese Techniken aus.
"""

import csv
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


FIELDS = ["Name", "Vorname", "Tel", "PLZ", "Ort", "Strasse"]


class RoloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ROLO 1.0")

        self.rolo = []
        self.filename = Path(__file__).resolve().parents[1] / "ausgabe" / "rolo.csv"

        self.create_widgets()

    def create_widgets(self):
        input_frame = ttk.LabelFrame(self.root, text="Eintrag")
        input_frame.pack(fill="x", padx=10, pady=10)

        self.entries = {}

        for i, field in enumerate(FIELDS):
            ttk.Label(input_frame, text=field).grid(row=i, column=0, sticky="w", padx=5, pady=3)
            entry = ttk.Entry(input_frame, width=40)
            entry.grid(row=i, column=1, sticky="ew", padx=5, pady=3)
            self.entries[field] = entry

        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill="x", padx=10, pady=5)

        ttk.Button(button_frame, text="Neu", command=self.new_entry).pack(side="left", padx=3)
        ttk.Button(button_frame, text="Löschen", command=self.delete_entry).pack(side="left", padx=3)
        ttk.Button(button_frame, text="Laden", command=self.load_file).pack(side="left", padx=3)
        ttk.Button(button_frame, text="Speichern", command=self.save_file).pack(side="left", padx=3)
        ttk.Button(
            button_frame, text="Speichern & Ende", command=self.quit_and_save
        ).pack(side="left", padx=3)

        search_frame = ttk.LabelFrame(self.root, text="Suche")
        search_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(search_frame, text="Feld").pack(side="left", padx=5)

        self.search_field = ttk.Combobox(search_frame, values=FIELDS, state="readonly", width=15)
        self.search_field.set("Name")
        self.search_field.pack(side="left", padx=5)

        ttk.Label(search_frame, text="Suchwert").pack(side="left", padx=5)

        self.search_value = ttk.Entry(search_frame, width=30)
        self.search_value.pack(side="left", padx=5)

        ttk.Button(search_frame, text="Suchen", command=self.find_entry).pack(side="left", padx=5)
        ttk.Button(
            search_frame, text="Alles anzeigen", command=self.refresh_table
        ).pack(side="left", padx=5)

        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(table_frame, columns=FIELDS, show="headings")

        for field in FIELDS:
            self.tree.heading(field, text=field)
            self.tree.column(field, width=120)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def new_entry(self):
        row = {}

        for field in FIELDS:
            value = self.entries[field].get().strip()
            if not value:
                messagebox.showwarning("Fehler", f"{field} fehlt.")
                return
            row[field] = value

        if any(kontakt["Tel"] == row["Tel"] for kontakt in self.rolo):
            messagebox.showwarning("Fehler", "Telefonnummer ist bereits vorhanden.")
            return

        self.rolo.append(row)
        self.clear_entries()
        self.refresh_table()

    def delete_entry(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning("Fehler", "Kein Eintrag ausgewählt.")
            return

        if not messagebox.askyesno("Löschen", "Ausgewählten Kontakt löschen?"):
            return

        index = int(selected[0])
        del self.rolo[index]

        self.clear_entries()
        self.refresh_table()

    def find_entry(self):
        feld = self.search_field.get()
        wert = self.search_value.get().strip()

        if not feld or not wert:
            messagebox.showwarning("Fehler", "Feld und Suchwert angeben.")
            return

        matches = [
            row for row in self.rolo
            if row.get(feld, "").casefold() == wert.casefold()
        ]

        self.refresh_table(matches)

    def load_file(self):
        filename = filedialog.askopenfilename(
            title="ROLO laden",
            filetypes=[("CSV-Dateien", "*.csv"), ("Alle Dateien", "*.*")]
        )

        if not filename:
            return

        try:
            with open(filename, newline="", encoding="utf-8") as quelle:
                reader = csv.DictReader(quelle)
                if not reader.fieldnames or not set(FIELDS) <= set(reader.fieldnames):
                    raise ValueError("Die CSV-Datei enthält nicht alle benötigten Spalten.")
                kontakte = []
                telefonnummern = set()
                for row in reader:
                    kontakt = {field: (row.get(field) or "").strip() for field in FIELDS}
                    if not all(kontakt.values()) or kontakt["Tel"] in telefonnummern:
                        raise ValueError("Kontakte sind unvollständig oder Telefonnummern doppelt.")
                    kontakte.append(kontakt)
                    telefonnummern.add(kontakt["Tel"])
        except (OSError, UnicodeError, csv.Error, ValueError) as fehler:
            messagebox.showerror("Laden fehlgeschlagen", str(fehler))
            return

        self.rolo = kontakte
        self.filename = Path(filename)
        self.refresh_table()
        messagebox.showinfo("OK", "Datei geladen.")

    def save_file(self):
        filename = filedialog.asksaveasfilename(
            title="ROLO speichern",
            defaultextension=".csv",
            filetypes=[("CSV-Dateien", "*.csv"), ("Alle Dateien", "*.*")]
        )

        if not filename:
            return

        try:
            self.write_csv(filename)
        except (OSError, UnicodeError, csv.Error) as fehler:
            messagebox.showerror("Speichern fehlgeschlagen", str(fehler))
            return
        self.filename = Path(filename)
        messagebox.showinfo("OK", "Datei gespeichert.")

    def quit_and_save(self):
        if self.rolo or self.filename.is_file():
            try:
                self.write_csv(self.filename)
            except (OSError, UnicodeError, csv.Error) as fehler:
                messagebox.showerror("Speichern fehlgeschlagen", str(fehler))
                return

        self.root.destroy()

    def write_csv(self, filename):
        filename = Path(filename)
        filename.parent.mkdir(parents=True, exist_ok=True)
        with filename.open("w", newline="", encoding="utf-8") as fd:
            writer = csv.DictWriter(fd, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(self.rolo)

    def refresh_table(self, data=None):
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Die Tabellen-ID bleibt der Index in der vollständigen Kontaktliste.
        for index, row in enumerate(self.rolo):
            if data is not None and row not in data:
                continue
            self.tree.insert(
                "",
                "end",
                iid=str(index),
                values=[row.get(field, "") for field in FIELDS]
            )

    def on_select(self, event):
        selected = self.tree.selection()

        if not selected:
            return

        index = int(selected[0])
        row = self.rolo[index]

        for field in FIELDS:
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, row.get(field, ""))

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    RoloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
