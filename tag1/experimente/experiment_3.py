import decimal
import json
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


class KontoApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Kontoverwaltung")
        self.geometry("1000x650")
        self.minsize(800, 550)

        self.dateipfad: Path | None = None
        self.seiten: dict[str, ttk.Frame] = {}

        self.name = tk.StringVar()
        self.alter = tk.StringVar()
        self.adresse = tk.StringVar()
        self.kontostand = tk.StringVar(value="0,00")
        self.betrag = tk.StringVar(value="3500,00")

        self.status = tk.StringVar(value="Bereit")
        self.uebersicht = tk.StringVar()
        self.kontoanzeige = tk.StringVar()
        self.aktive_seite = tk.StringVar()

        self._stil_erstellen()
        self._menue_erstellen()
        self._oberflaeche_erstellen()
        self._tasten_belegen()

        self.protocol("WM_DELETE_WINDOW", self.beenden)
        self.seite_anzeigen("Übersicht")

    def _stil_erstellen(self) -> None:
        stil = ttk.Style(self)
        if "vista" in stil.theme_names():
            stil.theme_use("vista")

        stil.configure("Titel.TLabel", font=("Segoe UI", 22, "bold"))
        stil.configure("Untertitel.TLabel", font=("Segoe UI", 11))
        stil.configure("Saldo.TLabel", font=("Segoe UI", 30, "bold"))
        stil.configure("Navigation.TButton", padding=(15, 12))
        stil.configure("Aktion.TButton", padding=(12, 8))

    def _menue_erstellen(self) -> None:
        menueleiste = tk.Menu(self)

        datei = tk.Menu(menueleiste, tearoff=False)
        datei.add_command(
            label="Neu", accelerator="Strg+N", command=self.neu
        )
        datei.add_command(
            label="Öffnen …", accelerator="Strg+O", command=self.oeffnen
        )
        datei.add_command(
            label="Speichern", accelerator="Strg+S", command=self.speichern
        )
        datei.add_command(
            label="Speichern unter …",
            command=lambda: self.speichern(unter=True),
        )
        datei.add_separator()
        datei.add_command(label="Beenden", command=self.beenden)
        menueleiste.add_cascade(label="Datei", menu=datei)

        ansicht = tk.Menu(menueleiste, tearoff=False)
        for seite in ("Übersicht", "Personendaten", "Konto"):
            ansicht.add_command(
                label=seite,
                command=lambda ziel=seite: self.seite_anzeigen(ziel),
            )
        menueleiste.add_cascade(label="Ansicht", menu=ansicht)

        konto = tk.Menu(menueleiste, tearoff=False)
        konto.add_command(label="Betrag gutschreiben", command=self.gutschreiben)
        menueleiste.add_cascade(label="Konto", menu=konto)

        hilfe = tk.Menu(menueleiste, tearoff=False)
        hilfe.add_command(
            label="Über Kontoverwaltung",
            command=lambda: messagebox.showinfo(
                "Über Kontoverwaltung",
                "Kontoverwaltung 1.0\n\n"
                "Python · Tkinter · Decimal\n\n"
                "Beispielanwendung zur Verwaltung eines Datensatzes.",
                parent=self,
            ),
        )
        menueleiste.add_cascade(label="Hilfe", menu=hilfe)

        self.config(menu=menueleiste)

    def _oberflaeche_erstellen(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        werkzeugleiste = ttk.Frame(self, padding=(10, 8))
        werkzeugleiste.grid(row=0, column=0, sticky="ew")

        for text, aktion in (
            ("Neu", self.neu),
            ("Öffnen", self.oeffnen),
            ("Speichern", self.speichern),
        ):
            ttk.Button(
                werkzeugleiste, text=text, command=aktion
            ).pack(side="left", padx=(0, 6))

        hauptbereich = ttk.Frame(self)
        hauptbereich.grid(row=1, column=0, sticky="nsew")
        hauptbereich.columnconfigure(1, weight=1)
        hauptbereich.rowconfigure(0, weight=1)

        navigation = ttk.Frame(hauptbereich, padding=15)
        navigation.grid(row=0, column=0, sticky="ns")

        ttk.Label(
            navigation, text="KONTOVERWALTUNG", font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(5, 20))

        for seite in ("Übersicht", "Personendaten", "Konto"):
            ttk.Button(
                navigation,
                text=seite,
                style="Navigation.TButton",
                command=lambda ziel=seite: self.seite_anzeigen(ziel),
            ).pack(fill="x", pady=4)

        inhalt = ttk.Frame(hauptbereich, padding=25)
        inhalt.grid(row=0, column=1, sticky="nsew")
        inhalt.columnconfigure(0, weight=1)
        inhalt.rowconfigure(0, weight=1)

        for name in ("Übersicht", "Personendaten", "Konto"):
            seite = ttk.Frame(inhalt)
            seite.grid(row=0, column=0, sticky="nsew")
            seite.columnconfigure(0, weight=1)
            self.seiten[name] = seite

        self._uebersicht_erstellen()
        self._personenseite_erstellen()
        self._kontoseite_erstellen()

        statusleiste = ttk.Frame(self, padding=(12, 6))
        statusleiste.grid(row=2, column=0, sticky="ew")
        statusleiste.columnconfigure(0, weight=1)

        ttk.Label(statusleiste, textvariable=self.status).grid(
            row=0, column=0, sticky="w"
        )
        ttk.Label(statusleiste, textvariable=self.aktive_seite).grid(
            row=0, column=1, sticky="e"
        )

    def _seitenkopf(self, seite: ttk.Frame, titel: str, text: str) -> None:
        ttk.Label(seite, text=titel, style="Titel.TLabel").pack(
            anchor="w", pady=(0, 8)
        )
        ttk.Label(seite, text=text, style="Untertitel.TLabel").pack(
            anchor="w", pady=(0, 25)
        )

    def _uebersicht_erstellen(self) -> None:
        seite = self.seiten["Übersicht"]
        self._seitenkopf(
            seite, "Übersicht", "Personendaten und aktueller Kontostand."
        )

        karte = ttk.LabelFrame(seite, text="Aktueller Datensatz", padding=20)
        karte.pack(fill="x")

        ttk.Label(
            karte,
            textvariable=self.uebersicht,
            font=("Segoe UI", 12),
            justify="left",
            wraplength=550,
        ).pack(anchor="w")

        ttk.Separator(karte).pack(fill="x", pady=20)

        ttk.Label(karte, text="Kontostand").pack(anchor="w")
        ttk.Label(
            karte, textvariable=self.kontoanzeige, style="Saldo.TLabel"
        ).pack(anchor="w", pady=(5, 0))

        ttk.Button(
            seite,
            text="Personendaten bearbeiten",
            style="Aktion.TButton",
            command=lambda: self.seite_anzeigen("Personendaten"),
        ).pack(anchor="w", pady=20)

    def _personenseite_erstellen(self) -> None:
        seite = self.seiten["Personendaten"]
        self._seitenkopf(
            seite, "Personendaten", "Name, Alter und Adresse erfassen."
        )

        formular = ttk.LabelFrame(seite, text="Person", padding=20)
        formular.pack(fill="x")
        formular.columnconfigure(1, weight=1)

        for zeile, (titel, variable) in enumerate(
            (
                ("Name", self.name),
                ("Alter", self.alter),
                ("Adresse", self.adresse),
            )
        ):
            ttk.Label(formular, text=titel).grid(
                row=zeile, column=0, sticky="w", padx=(0, 20), pady=10
            )
            ttk.Entry(formular, textvariable=variable).grid(
                row=zeile, column=1, sticky="ew", pady=10
            )

        ttk.Button(
            seite,
            text="Eingaben prüfen",
            style="Aktion.TButton",
            command=self.eingaben_pruefen,
        ).pack(anchor="w", pady=20)

    def _kontoseite_erstellen(self) -> None:
        seite = self.seiten["Konto"]
        self._seitenkopf(
            seite, "Konto", "Kontostand erfassen und eine Gutschrift buchen."
        )

        formular = ttk.LabelFrame(seite, text="Kontodaten", padding=20)
        formular.pack(fill="x")
        formular.columnconfigure(1, weight=1)

        for zeile, (titel, variable) in enumerate(
            (
                ("Kontostand (€)", self.kontostand),
                ("Gutschrift (€)", self.betrag),
            )
        ):
            ttk.Label(formular, text=titel).grid(
                row=zeile, column=0, sticky="w", padx=(0, 20), pady=10
            )
            ttk.Entry(formular, textvariable=variable).grid(
                row=zeile, column=1, sticky="ew", pady=10
            )

        ttk.Button(
            seite,
            text="Gutschrift buchen",
            style="Aktion.TButton",
            command=self.gutschreiben,
        ).pack(anchor="w", pady=20)

        ttk.Label(seite, text="Aktueller Kontostand").pack(anchor="w")
        ttk.Label(
            seite, textvariable=self.kontoanzeige, style="Saldo.TLabel"
        ).pack(anchor="w", pady=8)

    def _tasten_belegen(self) -> None:
        for taste, aktion in (
            ("<Control-n>", self.neu),
            ("<Control-o>", self.oeffnen),
            ("<Control-s>", self.speichern),
        ):
            self.bind(taste, lambda event, funktion=aktion: funktion())

    @staticmethod
    def _geld_lesen(text: str) -> decimal.Decimal:
        try:
            wert = decimal.Decimal(text.strip().replace(",", "."))
            if not wert.is_finite():
                raise ValueError
            gerundet = wert.quantize(decimal.Decimal("0.01"))
            if wert != gerundet:
                raise ValueError
            return gerundet
        except (decimal.DecimalException, ValueError) as fehler:
            raise ValueError(
                "Geldbeträge bitte ohne Tausendertrennzeichen und "
                "mit höchstens zwei Nachkommastellen eingeben."
            ) from fehler

    @staticmethod
    def _geld_formatieren(wert: decimal.Decimal) -> str:
        return f"{wert:,.2f}".translate(str.maketrans(",.", ".,")) + " €"

    def _daten_lesen(self) -> dict[str, str | int]:
        try:
            alter = int(self.alter.get())
        except ValueError as fehler:
            raise ValueError("Bitte das Alter als ganze Zahl eingeben.") from fehler

        if alter < 0:
            raise ValueError("Das Alter darf nicht negativ sein.")

        return {
            "name": self.name.get().strip(),
            "alter": alter,
            "adresse": self.adresse.get().strip(),
            "kontostand": str(self._geld_lesen(self.kontostand.get())),
        }

    def _anzeigen_aktualisieren(self) -> None:
        self.uebersicht.set(
            f"Name: {self.name.get().strip() or '—'}\n\n"
            f"Alter: {self.alter.get().strip() or '—'}\n\n"
            f"Adresse: {self.adresse.get().strip() or '—'}"
        )
        try:
            saldo = self._geld_lesen(self.kontostand.get())
            self.kontoanzeige.set(self._geld_formatieren(saldo))
        except ValueError:
            self.kontoanzeige.set("Ungültiger Betrag")

    def seite_anzeigen(self, name: str) -> None:
        self._anzeigen_aktualisieren()
        self.seiten[name].tkraise()
        self.aktive_seite.set(name)

    def eingaben_pruefen(self) -> None:
        try:
            self._daten_lesen()
        except ValueError as fehler:
            messagebox.showerror("Eingaben prüfen", str(fehler), parent=self)
            return

        self._anzeigen_aktualisieren()
        self.status.set("Eingaben sind gültig.")

    def gutschreiben(self) -> None:
        try:
            saldo = self._geld_lesen(self.kontostand.get())
            betrag = self._geld_lesen(self.betrag.get())
            if betrag <= 0:
                raise ValueError("Die Gutschrift muss größer als null sein.")
            ergebnis = self._geld_lesen(str(saldo + betrag))
        except (ValueError, decimal.DecimalException) as fehler:
            messagebox.showerror("Gutschrift", str(fehler), parent=self)
            return

        self.kontostand.set(str(ergebnis).replace(".", ","))
        self._anzeigen_aktualisieren()
        self.status.set(
            f"Gutschrift über {self._geld_formatieren(betrag)} gebucht."
        )

    def neu(self) -> None:
        if not messagebox.askyesno(
            "Neuer Datensatz",
            "Aktuelle Eingaben verwerfen und einen neuen Datensatz anlegen?",
            parent=self,
        ):
            return

        self.dateipfad = None
        self.name.set("")
        self.alter.set("")
        self.adresse.set("")
        self.kontostand.set("0,00")
        self.betrag.set("3500,00")
        self.title("Kontoverwaltung")
        self.seite_anzeigen("Personendaten")
        self.status.set("Neuer Datensatz")

    def oeffnen(self) -> None:
        pfad = filedialog.askopenfilename(
            parent=self,
            title="Kontodaten öffnen",
            filetypes=[("Kontodaten", "*.json")],
        )
        if not pfad:
            return

        try:
            daten = json.loads(Path(pfad).read_text(encoding="utf-8"))
            if not isinstance(daten, dict):
                raise ValueError("Die Datei enthält keinen gültigen Datensatz.")

            name = daten["name"]
            alter = daten["alter"]
            adresse = daten["adresse"]
            if (
                not isinstance(name, str)
                or type(alter) is not int
                or alter < 0
                or not isinstance(adresse, str)
                or not isinstance(daten["kontostand"], str)
            ):
                raise ValueError("Die Datei enthält ungültige Personendaten.")

            saldo = self._geld_lesen(daten["kontostand"])
        except (OSError, ValueError, KeyError) as fehler:
            messagebox.showerror(
                "Öffnen fehlgeschlagen", str(fehler), parent=self
            )
            return

        if not messagebox.askyesno(
            "Kontodaten öffnen",
            "Aktuelle Eingaben durch den geladenen Datensatz ersetzen?",
            parent=self,
        ):
            return

        self.name.set(name)
        self.alter.set(str(alter))
        self.adresse.set(adresse)
        self.kontostand.set(str(saldo).replace(".", ","))
        self.dateipfad = Path(pfad)
        self.title(f"Kontoverwaltung – {self.dateipfad.name}")
        self.seite_anzeigen("Übersicht")
        self.status.set(f"Geöffnet: {self.dateipfad.name}")

    def speichern(self, unter: bool = False) -> None:
        try:
            daten = self._daten_lesen()
        except ValueError as fehler:
            messagebox.showerror("Speichern", str(fehler), parent=self)
            return

        ziel = self.dateipfad
        if unter or ziel is None:
            pfad = filedialog.asksaveasfilename(
                parent=self,
                title="Kontodaten speichern",
                defaultextension=".json",
                initialfile=ziel.name if ziel else "konto.json",
                filetypes=[("Kontodaten", "*.json")],
            )
            if not pfad:
                return
            ziel = Path(pfad)

        try:
            ziel.write_text(
                json.dumps(daten, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        except OSError as fehler:
            messagebox.showerror(
                "Speichern fehlgeschlagen", str(fehler), parent=self
            )
            return

        self.dateipfad = ziel
        self.title(f"Kontoverwaltung – {ziel.name}")
        self.status.set(f"Gespeichert: {ziel.name}")

    def beenden(self) -> None:
        if messagebox.askyesno(
            "Beenden",
            "Programm beenden? Nicht gespeicherte Änderungen gehen verloren.",
            parent=self,
        ):
            self.destroy()


if __name__ == "__main__":
    app = KontoApp()
    app.mainloop()
