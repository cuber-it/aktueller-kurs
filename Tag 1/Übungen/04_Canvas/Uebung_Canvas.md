# Übung · Bounded Context Canvas

Sie beschreiben den Kontext **Anmietung** — den größten und unschärfsten der vier.

---

## Material A · Die vierzehn Aufgaben

Aus dem Workshop AV-2398. Die sechs strittigen sind markiert.

| # | Aufgabe | Strittig |
|---|---|---|
| 1 | Reservierung entgegennehmen und verwalten | |
| 2 | Fahrzeug ausgeben, Mietvertrag erstellen | |
| 3 | Fahrzeug zurücknehmen, Vorgang abschließen | |
| 4 | Verlängerung bei laufendem Vorgang | |
| 5 | Fahrerlaubnis prüfen (externer Prüfdienst) | **ja** |
| 6 | Kaution sperren und freigeben | **ja** |
| 7 | Zusatzleistungen buchen (Navi, Kindersitz, Zweitfahrer) | |
| 8 | Preis für Zusatzleistungen berechnen | **ja** |
| 9 | Schaden bei Rückgabe aufnehmen | **ja** |
| 10 | Schadensfotos speichern und weiterleiten | **ja** |
| 11 | Verfügbarkeitsanzeige für die Webseite | **ja** |
| 12 | Buchungen aus dem Partnernetzwerk entgegennehmen | |
| 13 | Firmenkonditionen anwenden | |
| 14 | Vorgangshistorie für Rückfragen bereithalten | |

## Material B · Aussagen zu den strittigen Aufgaben

**Zu 5 (Fahrerlaubnis):** Der Prüfdienst wird auch von der Vertragsverwaltung genutzt — bei Rahmenverträgen wird einmal jährlich für alle hinterlegten Fahrer geprüft.

**Zu 6 (Kaution):** Die Sperrung geschieht bei Ausgabe, die Freigabe bei Rückgabe. Die buchhalterische Behandlung — durchlaufender Posten, Verrechnung mit Schäden — liegt bei der Fakturierung.

**Zu 8 (Preis Zusatzleistungen):** Die Preise stehen im Rahmenvertrag oder in einer Preisliste. Die Preisliste pflegt der Vertrieb.

**Zu 9 und 10 (Schaden):** Der Schaden wird an der Station aufgenommen. Die Fotos gehen an die Werkstatt zur Beurteilung und an die Schadensplattform der Versicherung. Ob ein Schaden dem Mieter berechnet wird, entscheidet die Fakturierung nach Beurteilung durch die Werkstatt.

**Zu 11 (Verfügbarkeitsanzeige):** Zeigt auf der Webseite, welche Fahrzeugkategorien an welcher Station buchbar sind. Braucht Fahrzeugbestand (Flotte) und bestehende Reservierungen (Anmietung).

## Material C · Wer mit wem Information austauscht

Ohne Bewertung der Beziehung — nur, was fließt:

| Von | Nach | Was |
|---|---|---|
| Vertragsverwaltung | Anmietung | Konditionen, Preise |
| Anmietung | Fakturierung | abgeschlossene Vorgänge |
| Anmietung | Flotte | Ausgabe, Rückgabe |
| Flotte | Anmietung | Fahrzeugbestand |
| Partnernetzwerk | Anmietung | Buchungen |

## Material D · Die Glossareinträge

Aus Übung 2, Kontext Anmietung:

Vorgang · Mietvertrag · Verlängerung · Mieter · Firmenkonditionen · Fahrzeug · Rückläufer · Reserviert · Kaution

---

## Aufgabe

**1.** Formulieren Sie den **Zweck** des Kontextes in **einem Satz**. Der Satz muss ein fachliches Ergebnis benennen, keinen Ort und keine Aufzählung.

**2.** Prüfen Sie die acht unstrittigen Aufgaben gegen Ihren Zwecksatz. Passen alle? Wenn nicht: Welche fällt heraus?

**3.** Entscheiden Sie die sechs strittigen Aufgaben. Verwenden Sie für jede die Prüffrage:

   > *Würde eine Änderung an dieser Aufgabe auch die übrigen Aufgaben des Kontextes betreffen?*

   Notieren Sie je Aufgabe: Entscheidung, Begründung, und falls sie woandershin gehört, wohin.

**4.** Füllen Sie das Canvas aus:

   | Feld | Ihre Antwort |
   |---|---|
   | Name | |
   | Zweck | (aus Aufgabe 1) |
   | Strategische Einordnung | Core, Supporting oder Generic? Begründen Sie |
   | Fachliche Entscheidungen | Was entscheidet dieser Kontext selbst? |
   | Ubiquitous Language | (Verweis auf Material D, ergänzen falls nötig) |
   | Eingehende Nachrichten | Was, von wem? |
   | Ausgehende Nachrichten | Was, an wen? |
   | **Nicht zuständig für** | Was gehört ausdrücklich nicht hierher, und wohin dann? |

**5.** Aufgabe 9 und 10 gehören zusammen (Schaden aufnehmen, Fotos weiterleiten), werden aber möglicherweise unterschiedlich entschieden. Ist das ein Problem?

**6.** Nach Ihrer Entscheidung: Wie viele Aufgaben bleiben im Kontext? Ist er damit ausgewogen im Vergleich zu den anderen drei?

**7.** Ein neuer Entwickler fragt: „Gehört die Auswertung, welche Zusatzleistungen sich lohnen, in diesen Kontext?" Beantworten Sie die Frage anhand Ihres Canvas.

---

## Hinweise zur Bearbeitung

- Der Zwecksatz ist der schwierigste Teil. Wenn Sie „und" brauchen, ist es noch keine Klammer.
- „Es passiert an der Station" ist keine Begründung. Der Ort ist nicht die Fachlichkeit.
- Es ist zulässig, eine Aufgabe als offen auszuweisen — aber dann mit dem Kriterium, nach dem später entschieden wird.
