# 1-5 · Abhängigkeiten & Testbarkeit

Objekte arbeiten mit anderen Objekten zusammen. Diese **Abhängigkeiten** bestimmen wesentlich, wie leicht Code verstanden, verändert und isoliert getestet werden kann.

- **Abhängigkeit** – Ein Objekt benötigt eine Funktion, einen Dienst oder ein anderes Objekt, um seine Aufgabe zu erfüllen.
- **Versteckte Abhängigkeit** – Wird eine konkrete Abhängigkeit innerhalb einer Methode erzeugt oder global beschafft, ist sie für den Aufrufer kaum sichtbar und schwer austauschbar.
- **Explizite Abhängigkeit** – Übergabe über Konstruktor oder Methode macht sichtbar, was ein Objekt zum Arbeiten benötigt.
- **Dependency Injection** – Ein Objekt erhält seine Kollaborateure von außen, statt sie selbst auszuwählen und zu erzeugen. Dafür ist in Python kein DI-Framework erforderlich.
- **Dependency Inversion** – Fachlich höherliegender Code sollte möglichst nicht von unnötigen technischen Details abhängen. Kleine Verträge können die Richtung der Abhängigkeiten stabilisieren.
- **Austauschbarkeit** – Explizite Abhängigkeiten erlauben alternative Implementierungen, Test Doubles oder unterschiedliche technische Adapter.
- **Testbarkeit als Designsignal** – Muss ein Test umfangreiche globale Zustände, Dateisysteme, GUI-Objekte oder Netzwerkdienste vorbereiten, kann dies auf ungünstig geschnittene Abhängigkeiten hinweisen.
- **Nicht alles injizieren** – Triviale Werte oder stabile Implementierungsdetails künstlich zu abstrahieren erhöht Komplexität, ohne einen relevanten Vorteil zu schaffen.

## Leitfrage

**Kann ich am Konstruktor bzw. an der öffentlichen API erkennen, was dieses Objekt zum Arbeiten benötigt?**

Wenn wichtige Abhängigkeiten erst tief in der Implementierung sichtbar werden, steigt die Kopplung und sinkt die Kontrollierbarkeit.

> **Merksatz:** Gute Abhängigkeiten sind sichtbar, kontrollierbar und austauschbar.
