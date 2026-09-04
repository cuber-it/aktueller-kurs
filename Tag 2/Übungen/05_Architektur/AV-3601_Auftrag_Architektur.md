# AV-3601 · Fachliche Regeln vom technischen Ablauf trennen

**Typ:** Story
**Komponente:** Anmietung
**Priorität:** Hoch
**Verweist auf:** AV-3594 (Verlängerung fälschlich abgelehnt, 3 Tage Analyse für 2 Stunden Korrektur)

---

## Story

**Als** Fachvertreterin
**möchte ich** nachvollziehen können, ob eine Regel richtig umgesetzt ist,
**damit** ich nicht darauf angewiesen bin, dass jemand drei Tage lang ein halbes System aufbaut, um eine Bedingung zu prüfen.

---

## Description

Die Regel „ein Mietvertrag darf nur einmal verlängert werden" steckt als Schritt 2 in einer siebenschrittigen Ablaufsteuerung.

| Schritt | Was geschieht | Art |
|---|---|---|
| 1 | Vorgang holen | technisch |
| 2 | **Prüfen, ob schon verlängert wurde** | **fachlich** |
| 3 | Konditionen abfragen | technisch |
| 4 | Neuen Zeitraum berechnen | **fachlich** |
| 5 | Vorgang speichern | technisch |
| 6 | Bestätigung senden | technisch |
| 7 | Meldung an Fakturierung | technisch |

**Vorfall AV-3594:** Eine Verlängerung wurde abgelehnt, obwohl der Rahmenvertrag zwei erlaubt. Die Analyse dauerte drei Tage, die Korrektur zwei Stunden.

**Warum die Analyse so lange dauerte:** Um die Regel einmal auszuführen, braucht es eine Datenbank mit passendem Vorgang, ein erreichbares Vertragssystem, funktionierenden Nachrichtenversand und eine erreichbare Fakturierung.

**Weiterer Befund:** Die Frage „darf verlängert werden" wird an **drei Stellen** beantwortet — in der Ablaufsteuerung, in der Bedienoberfläche und in der Partnerschnittstelle. Alle drei Fassungen unterscheiden sich.

**Auf die Frage an den Fachbereich**, ob die Regel richtig umgesetzt sei, gab es keine Antwort — man müsste den Ablauf lesen können.

**Nicht Gegenstand:** Die Regel selbst. Sie ist fachlich unstrittig; strittig ist nur, wo sie steht.

## Randbedingungen

- Die Ablaufsteuerung hatte 2016 vier Schritte, heute sieben
- Zwei der drei Fremdsysteme haben Attrappen für Testzwecke, der Nachrichtenversand nicht
- Eine Testumgebung mit Datenbestand existiert
- Ähnliche Ablaufsteuerungen gibt es für Ausgabe, Rückgabe und Stornierung

## Akzeptanzkriterien

- **AK1** – Die Regel „nur einmal verlängerbar" ist prüfbar, ohne dass Datenbank, Fremdsysteme oder Nachrichtenversand laufen.
- **AK2** – Es gibt genau **eine** Stelle, an der die Frage „darf verlängert werden" beantwortet wird.
- **AK3** – Für jeden Schritt der Ablaufsteuerung ist angegeben, ob er fachlich oder technisch ist.
- **AK4** – Fachliche Schritte enthalten keine Zugriffe auf Datenbank, Fremdsysteme oder Versand.
- **AK5** – Technische Schritte enthalten keine fachlichen Regeln.
- **AK6** – Ein Fachvertreter kann anhand der Benennung erkennen, wo eine Regel steht.
- **AK7** – Für die Sonderregelung aus dem Rahmenvertrag ist beschrieben, wie sie in die Regel eingeht.
- **AK8** – Die drei abweichenden Fassungen sind auf eine zurückgeführt.
- **AK9** – Das Vorgehen ist auf die Ablaufsteuerungen für Ausgabe, Rückgabe und Stornierung übertragbar.

## Hinweise

Weitere Attrappen erfüllen AK1 nicht. Sie verkürzen die Vorbereitung, ändern aber nichts daran, dass die Regel in technischer Umgebung steckt.

AK2 ist der Kern des Folgeschadens: Drei Fassungen bedeuten drei Gelegenheiten, unterschiedlich zu entscheiden.

AK6 ist der Prüfstein für die Benennung. Wenn ein Fachvertreter nicht sagen kann, wo eine Regel steht, ist die Trennung nicht gelungen.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Arbeiten Sie entlang der Frage:

**Was ist fachlich, und was ist Ablauf?**

---
---

# Addendum · Die Trennung zwischen Fachlichkeit und Ablauf

## Der Grundgedanke

> **Die Fachlichkeit hängt von nichts ab. Alles andere hängt von ihr ab.**

Fachliche Regeln eines Unternehmens gelten unabhängig davon, ob sie in einem System, auf Papier oder im Kopf einer Sachbearbeiterin liegen. Genau so sollte das Modell gebaut sein.

## Die vier Bausteine und ihre Abgrenzung

### Zugang zu Gegenständen oder Erzeugung

| | Zugang (Repository) | Erzeugung (Factory) |
|---|---|---|
| Beantwortet | „Hol mir das mit dieser Kennung" | „Erzeuge ein neues, gültiges" |
| Liefert | was es gibt | was es noch nicht gab |

**Fachlich formuliert:** Holen oder erzeugen.

**Wichtig:** Ein Zugang je Konsistenzklammer, nicht je Gegenstand. Was innen liegt, kommt über die Wurzel.

### Fachlogik oder Ablaufsteuerung

| | Domain Service | Application Service |
|---|---|---|
| Enthält | Fachlogik, die zu keinem einzelnen Gegenstand gehört | Ablaufsteuerung |
| Beispiel | Umbuchung zwischen zwei Konten | holen, Methode rufen, speichern, melden |
| Fachvertreter erkennt es | **ja** | nein |

**Der Prüfstein:** Würde der Fachbereich diese Regel kennen?

## Signale für fehlende Trennung

| Signal | Konkret |
|---|---|
| Eine Regel ist nur mit laufender Umgebung prüfbar | sie steckt zwischen technischen Schritten |
| Dieselbe Frage wird an mehreren Stellen beantwortet | es gibt keinen Ort für die Regel |
| Ein Fachvertreter kann nicht sagen, wo eine Regel steht | die Benennung folgt der Technik |
| Attrappen werden gebaut, um Fachlogik zu prüfen | ein Symptom, keine Lösung |
| Die Ablaufsteuerung wächst, die Regel bleibt darin | jeder neue Schritt liegt zwischen Regel und Ergebnis |

## Die zwei häufigen Fehler

**Der Zugang liefert Datenstrukturen statt Gegenstände.**
Dann liegt die Fachlogik wieder außerhalb, und der Gegenstand ist eine Datenablage.

**Der Domain Service wird zur Sammelstelle.**
Wenn dort alles landet, was nicht in einen Gegenstand passte, ist das Modell wieder ohne Verhalten — nur mit anderem Namen.

**Der Prüfstein:** Wenn ein Domain Service dreißig Methoden hat, ist etwas schiefgelaufen.

## Der Preis

- Mehr Struktur, mehr Übersetzung zwischen den Schichten
- Bei einfachen Anwendungen Aufwand ohne Gegenwert
- Wer keine Regeln hat, braucht nichts zu schützen
