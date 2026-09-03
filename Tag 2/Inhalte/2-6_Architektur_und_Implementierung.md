# 2-6 · Architektur und Implementierung

Die Bausteine aus 2-1 bis 2-4 beschreiben das Modell. Jetzt geht es darum, **wo es liegt** — und wie es davor geschützt wird, von Technik durchdrungen zu werden.

Der gemeinsame Gedanke aller hier genannten Architekturformen: **Das Modell hängt von nichts ab. Alles andere hängt von ihm ab.**

- **Repository** – Der Zugang zu Aggregaten. Verbirgt, woher sie kommen; das Modell weiß nichts von Speicherung.
- **Ein Repository je Aggregate** – Nicht je Entity. Was innen liegt, wird über die Wurzel geholt.
- **Factory** – Erzeugt ein Aggregate in gültigem Zustand, wenn das aufwendig ist. Bei einfacher Erzeugung nicht nötig.
- **Repository oder Factory** – Holen oder erzeugen. Ein Repository gibt zurück, was es gibt; eine Factory bringt Neues hervor.
- **Domain Service** – Fachlogik, die zu keinem einzelnen Ding gehört. Eine Umbuchung zwischen zwei Konten gehört keinem der beiden.
- **Application Service** – Steuert den Ablauf: Aggregate holen, Methode aufrufen, speichern, Ereignis melden. Enthält **keine** Fachlogik.
- **Die Unterscheidung** – Fachlogik oder Ablaufsteuerung. Wer im Application Service rechnet, hat das Modell umgangen.
- **Schichten** – Fachlichkeit innen, Technik außen. Die Abhängigkeiten zeigen nach innen.
- **Hexagonal, Onion, Clean** – Verschiedene Namen für denselben Gedanken: Das Modell kennt weder Datenbank noch Oberfläche noch Fremdsysteme.
- **Warum das lohnt** – Ein Modell ohne technische Abhängigkeiten ist prüfbar, ohne dass etwas gestartet werden muss.
- **Häufiger Fehler** – Das Repository gibt Datenstrukturen statt Aggregate zurück. Dann liegt die Fachlogik wieder außerhalb.
- **Zweiter Fehler** – Domain Services als Sammelstelle. Wenn dort die ganze Fachlogik landet, ist das Modell wieder anämisch.
- **Der Preis** – Mehr Struktur, mehr Übersetzung zwischen den Schichten. Bei einfachen Anwendungen ist das Aufwand ohne Gegenwert.
