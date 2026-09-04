# Pro und Contra · Die Trennung von Fachlichkeit und Ablauf

Bewertet wird der Vorschlag aus dem Lösungspapier: Regel „darf verlängert werden" als Methode am Vorgang, Preisrechner und Schadensbewertung als eigene Fachbausteine, Angaben werden vor der Entscheidung beschafft, eine Antwort für alle Fragesteller.

---

## Pro

**Die Regel ist ohne Umgebung prüfbar**
Aus drei Tagen Vorbereitung werden Minuten. Ein Vorgang wird erzeugt, die Frage gestellt, die Antwort angesehen — ohne Datenbank, Fremdsystem oder Versand.

**Eine Antwort statt drei**
Ablauf, Bedienoberfläche und Partnerschnittstelle rufen dieselbe Methode. Die drei abweichenden Fassungen können nicht wieder entstehen.

**Der Fachbereich kann prüfen**
Eine Liste von Fällen mit Bewertung ist lesbar. „Kratzer 3 cm → kein Schaden" versteht jeder; eine Ablaufsteuerung nicht.

**Die Reihenfolge-Falle wurde gefunden**
Der eigentliche Fehler aus AV-3594 lag darin, dass die Konditionen **nach** der Prüfung abgefragt wurden. Das fiel erst beim Trennen auf.

**Die vollständige Regel wurde formuliert**
„Standard eins, laut Rahmenvertrag mehr, ohne Rahmenvertrag eins" — vorher stand nur „schon verlängert ja/nein" da. Die Sonderregelung war seit Jahren nicht abgebildet.

**Die Regel liefert eine Begründung**
Nicht nur ja/nein. Die Oberfläche kann anzeigen, warum nicht; die Partnerschnittstelle einen Ablehnungsgrund melden.

**Die Grenze nach außen wurde sichtbar**
Die Konditionenabfrage liefert Angaben aus einem fremden Modell. Dass sie übersetzen sollte, fiel bei der Einordnung auf — und ist die Vorlage für Tag 2, Einheit 7.

---

## Contra

**Mehr Bausteine, mehr Stellen**
Aus einer Ablaufsteuerung werden eine Steuerung, zwei bis drei Fachbausteine und die vorhandenen Zugänge. Wer nur wissen will, was bei einer Verlängerung geschieht, muss mehr ansehen.

**Die Übergabe von Angaben ist Schreibarbeit**
Die Höchstzahl muss geholt und weitergereicht werden. Vorher stand die Abfrage einfach im Ablauf. Die Abhängigkeit wird sichtbar — und kostet Zeilen.

**Die Trennung allein löst nichts**
Der Fund aus Aufgabe 2 — Reihenfolge — ist keine automatische Folge. Wer trennt und die Reihenfolge belässt, hat denselben Fehler mit mehr Struktur.

**Die Einordnung der Schadensbewertung ist strittig**
Der Vorschlag wählt einen eigenen Baustein; beim Befund wäre ebenfalls vertretbar. Solche Fälle kosten Diskussionszeit ohne eindeutiges Ergebnis.

**Die Umstellung betrifft vier Abläufe**
Verlängerung, Ausgabe, Rückgabe, Stornierung. AK9 verlangt Übertragbarkeit — das ist vierfacher Aufwand bei laufendem Betrieb.

**Bei einfachen Abläufen ist es Überbau**
Drei technische Schritte ohne Regel brauchen keine Trennung. Wer das Prinzip überall durchzieht, baut Struktur für nichts.

**Zwei Prüfungen statt einer**
Die zweistufige Lösung (fragen, dann durchführen mit erneuter Prüfung) ist richtig und wirkt doppelt gemoppelt. Das muss erklärt werden, sonst wird die zweite Prüfung beim nächsten Umbau wegoptimiert.

---

## Bewertung

Der Fall trägt die Trennung, weil **die Analyse länger dauerte als die Korrektur** — drei Tage gegen zwei Stunden. Das ist ein messbarer Beleg dafür, dass die Regel am falschen Ort steht.

Gegenprobe — *bei der eingebetteten Regel bleiben, bleiben Nachteile?* Ja: Weitere Attrappen verkürzen die Vorbereitung, ändern aber nichts an den drei Fassungen. Und die nächste Regel, die sich ändert, kostet wieder drei Tage.

**Die Grenzen:**

1. **Die Reihenfolge ist ein eigener Punkt.** Sie gehört ausdrücklich geprüft, nicht als Nebenfolge erwartet. Sonst wiederholt sich der Fehler in den drei anderen Abläufen.

2. **Die vollständige Regel war der eigentliche Fund.** Dass die Sonderregelung seit Jahren fehlte, hat mit der Trennung nur mittelbar zu tun — sie machte es sichtbar. Andere Regeln gehören ebenso überprüft.

3. **Die zweistufige Prüfung braucht eine Begründung im Code.** Sonst wird sie beim nächsten Umbau als Doppelung entfernt, und die Zusicherung fällt weg.

---

## Diskussionsfragen

1. Der eigentliche Fehler war die Reihenfolge. Was sagt das über die Ursache?
2. Wie verhindern Sie, dass die zweite Prüfung wegoptimiert wird?
3. Schadensbewertung — eigener Baustein oder beim Befund? Woran machen Sie es fest?
4. Vier Abläufe, vierfacher Aufwand. Womit fangen Sie an?
5. Wann wäre die eingebettete Regel die richtige Wahl gewesen?
