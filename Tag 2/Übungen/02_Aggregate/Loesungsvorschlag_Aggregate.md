# Lösungsvorschlag · Wo verlaufen die Klammern?

**Vorbemerkung:** Ein Vorschlag. Bei mehreren Grenzen sind zwei Schnitte vertretbar — bewertet wird, ob jede Klammer eine benannte Regel hat.

---

## 1 · Die Regeln bewertet

| # | Regel | Einordnung | Begründung |
|---|---|---|---|
| R1 | Nicht gleichzeitig ausgegeben und reserviert | **sofort** | „Das darf nie passieren" — direkter Kundenschaden |
| R2 | Ein Vorgang hat genau ein Fahrzeug | **sofort** | Ohne diese Zuordnung ist der Vorgang unvollständig |
| R3 | Rückläufer erst nach Aufbereitung ausgeben | **zeitnah** | „Fünf Minuten sind egal, ich korrigiere hinterher" |
| R4 | Zusatzleistungen passen zum Vorgang | **sofort** | Betrifft nur den einen Vorgang, dort ist es trivial einzuhalten |
| R5 | Reservierungen überschreiten die Fahrzeugzahl nicht | **zeitnah** | „Planungsgröße", fällt am Vortag auf |
| R6 | Außerhalb der Öffnungszeiten keine Ausgabe | **irgendwann** | „Um 18:03 statt 18:00 kräht kein Hahn" |
| R7 | Mitarbeiter genau einer Station zugeordnet | **irgendwann** | Betrifft die Abrechnung, nicht das Tagesgeschäft |

**Nur drei von sieben Regeln müssen sofort gelten.** Das ist der Befund, der alles Weitere trägt.

---

## 2 · Unsichere Fälle und die Fragen dazu

### R2 · Ein Vorgang, ein Fahrzeug

Die Aussage „klar, sonst wüsste ich ja nicht, was er hat" klingt eindeutig, beantwortet die Frage aber nicht.

**Die Frage:** „Gibt es Fälle, in denen ein Vorgang das Fahrzeug wechselt?"

Vermutlich ja — bei einer Panne wird ein Ersatzfahrzeug gestellt. Dann ist die Regel nicht „genau ein Fahrzeug", sondern „genau ein Fahrzeug **zur Zeit**". Das ändert die Klammer nicht, aber das Modell.

### R4 · Zusatzleistungen passen zum Vorgang

„Was gebucht ist, muss auf der Rechnung stehen" ist eine Aussage über die **Rechnung**, nicht über den Vorgang.

**Die Frage:** „Muss die Zusatzleistung im selben Moment beim Vorgang stehen, oder genügt es, wenn sie bis zur Abrechnung dort ist?"

Antwort bestimmt, ob die Regel sofort oder zeitnah gilt.

### R7 · Mitarbeiterzuordnung

„Sonst wird die Abrechnung schwierig" — das ist ein Monatsthema, kein Sekundenthema.

**Die Frage:** „Was passiert, wenn ein Mitarbeiter für zwei Stunden zwei Stationen zugeordnet ist?"

Vermutlich nichts, außer bei der Monatsabrechnung.

---

## 3 · Die Klammern

### Klammer A · Mietvorgang

| | |
|---|---|
| Enthält | ein Vorgang, sein Fahrzeug (als Verweis), seine Zusatzleistungen, sein Zeitraum, seine Kaution |
| Regel | R2 (ein Fahrzeug), R4 (Zusatzleistungen passen) |
| Exemplare je Station | 30–70, jedes einzeln |

### Klammer B · Fahrzeugverfügbarkeit

| | |
|---|---|
| Enthält | ein Fahrzeug, sein Zustand (verfügbar, ausgegeben, Rückläufer, in Aufbereitung) |
| Regel | R1 (nicht gleichzeitig ausgegeben und reserviert), R3 (erst nach Aufbereitung) |
| Exemplare je Station | 40–90, jedes einzeln |

### Klammer C · Reservierung

| | |
|---|---|
| Enthält | eine Reservierung mit Zeitraum, Kategorie, Kunde |
| Regel | keine, die mehrere Reservierungen verbindet |
| Exemplare je Station | 100–300, jede einzeln |

### Klammer D · Stationsstammdaten

| | |
|---|---|
| Enthält | Anschrift, Telefon, Öffnungszeiten, Sonderregelungen |
| Regel | R6 — aber nur „irgendwann"; die Klammer ist eher eine Zusammenfassung selten geänderter Angaben |
| Exemplare | eine je Station |

**Vier Klammern.** Die Station als Ganzes gibt es nicht mehr.

---

## 4 · Prüfung jeder Klammer

| Klammer | Regel zwischen allen Teilen sofort? | Ergebnis |
|---|---|---|
| A Mietvorgang | ja — Fahrzeugzuordnung und Zusatzleistungen gehören zum selben Vorgang | trägt |
| B Fahrzeugverfügbarkeit | ja — der Zustand eines Fahrzeugs ist eindeutig | trägt |
| C Reservierung | keine Regel zwischen mehreren Reservierungen | jede einzeln — trägt |
| D Stammdaten | keine Sofort-Regel | **trägt nicht als Konsistenzklammer** |

**Klammer D ist streng genommen keine.** Es gibt keine Regel, die zwischen Anschrift und Öffnungszeiten sofort gelten muss.

**Warum sie trotzdem sinnvoll ist:** Sie fasst zusammen, was selten geändert wird und gemeinsam gepflegt wird. Das ist eine Ordnungsentscheidung, keine Konsistenzentscheidung — und sollte als solche benannt werden.

**Alternative:** Öffnungszeiten und Sonderregelungen als eigene Klammer, getrennt von Anschrift und Telefon. Vertretbar, aber ohne erkennbaren Gewinn.

---

## 5 · Bestandteile ohne Regel

| Bestandteil | Wohin |
|---|---|
| Rückläufer in Aufbereitung | **kein eigener Gegenstand** — es ist ein Zustand des Fahrzeugs (Klammer B) |
| Mitarbeiterzuordnung | **eigener Kontext** — sie betrifft Personalverwaltung, nicht Anmietung |

**Die Rückläufer waren nie ein eigenes Ding.** Sie sind Fahrzeuge in einem bestimmten Zustand. Dass sie in der alten Lösung getrennt geführt wurden, war eine Folge der Listenansicht am Tresen, nicht der Fachlichkeit.

**Die Mitarbeiterzuordnung gehört nicht hierher.** R7 betrifft die Abrechnung. Sie in der Anmietung zu führen war eine Folge davon, dass die Station als Sammelbecken diente.

---

## 6 · Regel R1 über Klammergrenzen

**In diesem Vorschlag liegen Fahrzeug (B) und Reservierung (C) in getrennten Klammern.** Die Regel „nicht gleichzeitig ausgegeben und reserviert" geht über die Grenze.

**Drei mögliche Wege:**

| Weg | Wie | Bewertung |
|---|---|---|
| **Prüfen beim Zugriff** | Vor der Ausgabe wird geprüft, ob eine Reservierung für dieses Fahrzeug besteht | einfach, nicht absolut sicher — zwischen Prüfung und Ausgabe liegt ein kurzer Zeitraum |
| **Zustand am Fahrzeug führen** | Eine Reservierung setzt das Fahrzeug auf „reserviert"; die Regel gilt dann **innerhalb** von Klammer B | sicher, aber die Reservierung muss das Fahrzeug ändern — zwei Klammern in einem Vorgang |
| **Fahrzeug und Reservierung in eine Klammer** | Rückkehr zur größeren Einheit | löst das Problem, bringt das alte zurück |

**Der Vorschlag wählt den zweiten Weg**, mit einer Einschränkung:

Eine Reservierung wird **ohne** konkretes Fahrzeug angelegt — sie nennt nur eine Kategorie. Erst am Vortag wird ein Fahrzeug zugeteilt, und **dann** wird dessen Zustand geändert.

**Damit ist R1 innerhalb von Klammer B**: Ein Fahrzeug hat genau einen Zustand, und „reserviert" und „ausgegeben" schließen sich aus.

**Der Nebeneffekt:** Reservierungen sind fachlich ohnehin auf Kategorien bezogen, nicht auf Einzelfahrzeuge. Der Kunde bucht „Kompakt", nicht „das Auto mit dem Kennzeichen X". Der Vorschlag bildet ab, wie es tatsächlich ist.

---

## 7 · Prüfung gegen den Vorfall

**Vier Mitarbeiter geben gleichzeitig verschiedene Fahrzeuge aus.**

| Mitarbeiter | Ändert |
|---|---|
| 1 | Vorgang 1 (Klammer A), Fahrzeug 1 (Klammer B) |
| 2 | Vorgang 2, Fahrzeug 2 |
| 3 | Vorgang 3, Fahrzeug 3 |
| 4 | Vorgang 4, Fahrzeug 4 |

**Keine Überschneidung.** Acht verschiedene Klammern, keine Wartezeit.

**Die Verfügbarkeitsanzeige** liest Klammer B — lesend, ohne zu ändern. Sie behindert nichts.

**Der Nachtlauf** ändert Reservierungen (Klammer C). Er berührt weder Vorgänge noch Fahrzeuge.

**Der Vorfall wäre nicht eingetreten.**

---

## 8 · Änderung der Öffnungszeiten

**Betroffen: nur Klammer D.**

Das Tagesgeschäft läuft weiter. AK4 ist erfüllt.

---

## 9 · Regel R5 über alle Fahrzeuge und Reservierungen

Das ist die schwierigste Frage der Übung — und der Punkt, an dem viele zur großen Klammer zurückkehren wollen.

**Die Regel:** Reservierungen dürfen die Fahrzeugzahl nicht überschreiten.

**Sie betrifft alle Fahrzeuge und alle Reservierungen einer Station.** In kleinen Klammern ist sie nicht durchsetzbar.

**Der Ausweg liegt in der Bewertung aus Aufgabe 1:** R5 ist **zeitnah**, nicht sofort. „Das ist eine Planungsgröße. Wenn wir kurzzeitig eine Reservierung zu viel haben, fällt das erst am Tag vorher auf."

**Der Vorschlag:**

| Was | Wie |
|---|---|
| Beim Anlegen einer Reservierung | Verfügbarkeit prüfen, aber nicht sperren — eine Empfehlung, keine Zusicherung |
| Laufend | Ein Auslastungswert je Station und Kategorie wird nachgezogen, wenn Reservierungen entstehen oder wegfallen |
| Bei Überschreitung | Meldung an die Disposition, keine Ablehnung |
| Am Vortag | Zuteilung konkreter Fahrzeuge; hier fällt eine Überbuchung auf und wird umdisponiert |

**Damit ist R5 keine Regel mehr, die eine Klammer rechtfertigt, sondern eine Beobachtung mit Warnung.**

Das entspricht der Aussage der Stationsleitung — und es entspricht der Wirklichkeit: Überbuchung wird in dieser Branche ohnehin durch Disposition aufgelöst, nicht durch Ablehnung.

---

## 10 · Der Preis

**Erstens: Widersprüchliche Zustände sind möglich.**
Zwischen dem Anlegen einer Reservierung und dem Nachziehen des Auslastungswerts kann die Station kurzzeitig überbucht erscheinen — oder nicht, obwohl sie es ist. Das ist fachlich vertretbar, aber es ist eine Abweichung von „das System weiß immer alles".

**Zweitens: Mehr Zugriffe für einen Vorgang.**
Eine Ausgabe berührt zwei Klammern statt einer. Statt einmal die Station zu laden, werden Vorgang und Fahrzeug einzeln geholt.

**Drittens: Die Gesamtsicht ist aufwendiger.**
„Zeig mir die Station" war vorher ein Zugriff. Jetzt sind es mehrere, und die Zusammenstellung muss jemand bauen.

**Viertens: Die Regel R1 hängt an einer Entwurfsentscheidung.**
Sie funktioniert nur, weil Reservierungen auf Kategorien statt auf Einzelfahrzeuge gehen. Ändert sich das fachlich, muss der Schnitt überdacht werden.

**Fünftens: Die Umstellung ist erheblich.**
Alles, was heute die Station als Einheit behandelt, muss umgebaut werden — bei laufendem Betrieb.

---

## Diskussionsanschluss

R5 wurde von einer Regel zu einer Warnung herabgestuft, gestützt auf eine Aussage der Stationsleitung. Was, wenn eine andere Stationsleitung das anders sieht?
