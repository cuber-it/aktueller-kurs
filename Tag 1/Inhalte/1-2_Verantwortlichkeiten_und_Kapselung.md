# 1-2 · Verantwortlichkeiten & Kapselung

Eine Klasse ist nicht deshalb sinnvoll, weil mehrere Daten zusammengehören. Ihr Wert entsteht, wenn sie eine **klar erkennbare Verantwortung** übernimmt und die dafür notwendigen Details hinter einer stabilen Schnittstelle verbirgt.

- **Verantwortung** – Ein Objekt sollte einen nachvollziehbaren Zweck im System besitzen. Methoden und Zustand dienen diesem Zweck.
- **Kohäsion** – Stark zusammengehörige Daten und Operationen gehören zusammen. Je weniger Gründe eine Klasse hat, sich zu ändern, desto leichter lässt sie sich verstehen und pflegen.
- **Kapselung** – Nicht die Sichtbarkeit einzelner Attribute ist das Ziel, sondern der Schutz von Annahmen und Implementierungsentscheidungen vor unnötigen Abhängigkeiten.
- **Information Hiding** – Außenstehender Code sollte nur wissen müssen, was für die Zusammenarbeit erforderlich ist. Interne Datenstrukturen und technische Details bleiben austauschbar.
- **Tell, don't ask** – Statt Zustand auszulesen, extern Entscheidungen zu treffen und anschließend wieder Zustand zu verändern, kann die Verantwortung häufig beim betroffenen Objekt bleiben.
- **Feature Envy** – Greift eine Methode überwiegend auf Daten eines anderen Objekts zu, kann die Verantwortung falsch zugeordnet sein.
- **God Object** – Klassen, die Konfiguration, Datenzugriff, Steuerung, Fachlogik und Hilfsfunktionen gleichzeitig übernehmen, erzeugen hohe Kopplung und viele Änderungsgründe.
- **Testcode ist Code** – Auch Page Objects, Testhelfer und Framework-Komponenten benötigen klar geschnittene Verantwortlichkeiten. „Ist nur Testcode“ rechtfertigt keine beliebige Struktur.

## Entscheidungsfrage

Bei jeder Klasse sollte sich beantworten lassen:

**Wofür ist dieses Objekt verantwortlich – und welche Änderung sollte genau hier stattfinden?**

Kann die Antwort nur als Aufzählung vieler unabhängiger Aufgaben formuliert werden, ist der Schnitt wahrscheinlich zu groß.

> **Merksatz:** Eine Klasse braucht eine klare Verantwortung – nicht nur gemeinsame Daten.
