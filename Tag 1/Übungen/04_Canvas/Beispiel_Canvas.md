# Beispiel · Ein Canvas in klein

Ein Kontext mit fünf Aufgaben, vollständig ausgefüllt.

---

## Die Ausgangslage

Eine Kfz-Werkstatt mit angeschlossenem Ersatzteillager. Der Kontext heißt **Auftragsabwicklung**.

Sechs Aufgaben liegen dort:

| # | Aufgabe |
|---|---|
| 1 | Auftrag annehmen, Termin vereinbaren |
| 2 | Fahrzeug annehmen, Schäden dokumentieren |
| 3 | Arbeitsschritte planen und zuweisen |
| 4 | Ersatzteile bestellen |
| 5 | Arbeitszeiten erfassen |
| 6 | Fahrzeug übergeben, Auftrag abschließen |

---

## Schritt 1 · Der Zwecksatz

Erster Versuch:

> „Aufträge annehmen, durchführen und abschließen"

Enthält zwei „und" — das ist eine Aufzählung, keine Klammer.

Zweiter Versuch:

> **„Die Auftragsabwicklung verantwortet den Werkstattauftrag von der Annahme bis zur Fahrzeugübergabe."**

Ein fachliches Ergebnis (der abgeschlossene Auftrag), eine erkennbare Grenze (Annahme bis Übergabe), kein Ort, kein „und".

## Schritt 2 · Aufgaben gegen den Zweck prüfen

Für jede die Frage: *Würde eine Änderung daran die übrigen Aufgaben betreffen?*

| # | Prüfung | Ergebnis |
|---|---|---|
| 1 | Ändert sich die Terminvergabe, ändert sich der Auftragsbeginn | **ja** |
| 2 | Die Dokumentation bestimmt, was zu tun ist | **ja** |
| 3 | Die Planung strukturiert den Auftrag | **ja** |
| 4 | **Eine Änderung im Bestellwesen berührt den Auftragsablauf nicht** | **nein** |
| 5 | Die Zeiterfassung bestimmt, wann der Auftrag fertig ist | **ja** |
| 6 | Ende des Auftrags | **ja** |

**Aufgabe 4 fällt heraus.**

## Schritt 3 · Wohin gehört die Ersatzteilbestellung?

**Prüfungen:**

| Frage | Antwort |
|---|---|
| Kommen ihre Begriffe im Glossar vor? | nein — Lieferant, Bestellmenge, Lieferzeit stehen nicht dort |
| Nutzt ein anderer Bereich dieselbe Fähigkeit? | ja — der Teileverkauf über den Tresen bestellt ebenfalls |
| Legt sie fest oder wendet sie an? | sie legt fest — welcher Lieferant, welche Menge |

Alle drei sprechen für einen eigenen Kontext.

**Entscheidung:** Ein Kontext **Teilebeschaffung**. Die Auftragsabwicklung meldet einen Bedarf und bekommt eine Zusage mit Termin.

## Schritt 4 · Das Canvas

| Feld | Inhalt |
|---|---|
| **Name** | Auftragsabwicklung |
| **Zweck** | Verantwortet den Werkstattauftrag von der Annahme bis zur Fahrzeugübergabe |
| **Strategische Einordnung** | Core Domain — das Kerngeschäft der Werkstatt |
| **Fachliche Entscheidungen** | Ist der Auftrag durchführbar? · Welche Arbeitsschritte sind nötig? · Ist der Auftrag fertig? · Kann übergeben werden? |
| **Ubiquitous Language** | Auftrag, Arbeitsschritt, Annahmeprotokoll, Fertigmeldung, Übergabe |
| **Eingehende Nachrichten** | Terminwunsch (Kunde) · Teilezusage mit Termin (Teilebeschaffung) · Fahrzeughistorie (Fahrzeugakte) |
| **Ausgehende Nachrichten** | Teilebedarf (Teilebeschaffung) · Abgeschlossener Auftrag (Fakturierung) · Durchgeführte Arbeiten (Fahrzeugakte) |
| **Nicht zuständig für** | Bestellung und Lieferantenwahl → Teilebeschaffung · Rechnungsstellung → Fakturierung · Fahrzeughistorie führen → Fahrzeugakte · Preise für Arbeitswerte festlegen → Kalkulation |

## Schritt 5 · Der Test

Ein neuer Mitarbeiter fragt: *„Gehört die Auswertung, welche Teile am häufigsten gebraucht werden, hierher?"*

**Antwort anhand des Canvas:** Der Zweck betrifft den einzelnen Auftrag von Annahme bis Übergabe. Eine Auswertung über Teileverbrauch betrifft keinen einzelnen Auftrag, sondern die Bevorratung — das ist Teilebeschaffung.

**Zwei Sätze, klare Antwort.** Das ist der Zweck des Canvas.

---

## Was dieses Beispiel zeigt

**Der erste Zwecksatz war falsch.** „Annehmen, durchführen und abschließen" klingt richtig, ist aber eine Aufzählung. Der zweite Versuch trägt, weil er ein Ergebnis nennt.

**Eine von sechs Aufgaben fiel heraus.** Das ist ein typisches Verhältnis. Kontexte sammeln Aufgaben, die zufällig dort landeten.

**Drei Prüfungen zeigten dasselbe.** Fremde Begriffe, andere Nutzer, festlegen statt anwenden — wenn mehrere Kriterien in dieselbe Richtung zeigen, ist die Entscheidung sicher.

**„Nicht zuständig für" hat vier Einträge.** Mehr als das Canvas an anderer Stelle enthält. Das ist normal und nützlich — die Abgrenzung ist die Arbeit.

---

## Zum Vergleich: ein Zwecksatz, der nicht trägt

> „Die Auftragsabwicklung kümmert sich um alles rund um den Werkstattauftrag."

**Warum das nicht funktioniert:** „Alles rund um" ist keine Grenze. Unter diesem Satz gehört die Ersatzteilbestellung dazu — sie ist ja „rund um" den Auftrag. Ebenso die Rechnung, die Fahrzeughistorie und die Kalkulation.

Ein Zwecksatz muss **ausschließen** können. Wenn er alles einschließt, hilft er nicht.
