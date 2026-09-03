# Pro und Contra · Die vier Klammern

Bewertet wird der Vorschlag aus dem Lösungspapier: Mietvorgang, Fahrzeugverfügbarkeit, Reservierung und Stammdaten als getrennte Klammern; Reservierungen auf Kategorien statt Einzelfahrzeuge; R5 als Warnung statt Regel.

---

## Pro

**Der Vorfall wäre nicht eingetreten**
Vier Mitarbeiter, die verschiedene Fahrzeuge ausgeben, berühren acht verschiedene Klammern. Keine Wartezeit, keine 90 Sekunden, keine elf abgewanderten Kunden.

**Der Engpass wächst nicht mehr mit der Größe**
Frankfurt-Flughafen mit 90 Fahrzeugen ist genauso schnell wie eine Station mit zwölf. Die Klammer ist ein Fahrzeug, nicht der Hof.

**Selten Geändertes blockiert nichts mehr**
Eine Änderung der Öffnungszeiten betrifft nur die Stammdaten. Das Tagesgeschäft läuft weiter.

**Die Verfügbarkeitsanzeige stört nicht**
Sie liest, ohne zu ändern. In der alten Lösung behandelte auch das Lesen die ganze Station als Einheit.

**Jede Klammer hat eine benannte Regel**
Drei von vier lassen sich mit einer Sofort-Regel begründen. Bei der vierten steht ausdrücklich, dass sie eine Ordnungs- und keine Konsistenzentscheidung ist.

**Die Reservierung auf Kategorien bildet die Wirklichkeit ab**
Der Kunde bucht „Kompakt", nicht ein bestimmtes Kennzeichen. Der Vorschlag modelliert, wie es fachlich ohnehin läuft — und löst dabei R1 innerhalb einer kleinen Klammer.

**Zwei Bestandteile entfallen ersatzlos**
Rückläufer sind ein Zustand des Fahrzeugs, kein eigenes Ding. Die Mitarbeiterzuordnung gehört in einen anderen Kontext. Beide waren nur dort, weil die Station als Sammelbecken diente.

---

## Contra

**Die Gesamtsicht ist aufwendiger**
„Zeig mir die Station" war ein Zugriff, jetzt sind es mehrere. Für Übersichten, Auswertungen und die Stationsleitungs-Ansicht muss jemand die Zusammenstellung bauen.

**Widersprüchliche Zustände sind möglich**
Zwischen dem Anlegen einer Reservierung und dem Nachziehen der Auslastung kann eine Station überbucht erscheinen oder nicht, obwohl sie es ist. Fachlich vertretbar, aber eine Abweichung von „das System weiß immer alles".

**R5 wurde herabgestuft, gestützt auf eine einzige Aussage**
„Das ist eine Planungsgröße" kam von einer Stationsleitung. Ob alle 140 Stationen das so sehen, ist ungeprüft. Wenn eine davon Überbuchung als Ausschlusskriterium sieht, trägt der Vorschlag dort nicht.

**Die Lösung von R1 hängt an einer Entwurfsentscheidung**
Sie funktioniert, weil Reservierungen auf Kategorien gehen. Sollte künftig ein Kunde ein bestimmtes Fahrzeug reservieren können — bei Sonderfahrzeugen naheliegend —, bricht die Begründung.

**Mehr Zugriffe je Vorgang**
Eine Ausgabe holt Vorgang und Fahrzeug einzeln. Das ist mehr Aufwand als ein Zugriff auf die Station — nur eben ohne Wartezeit.

**Die Umstellung ist erheblich**
Alles, was heute die Station als Einheit behandelt, muss umgebaut werden. Bei laufendem Betrieb, über 140 Stationen.

**Vier Klammern könnten zu wenige sein**
Der Mietvorgang enthält Zusatzleistungen, Kaution und Zeitraum. Ob dort weitere Grenzen liegen, ist nicht geprüft.

---

## Bewertung

Der Fall trägt die Zerlegung, weil **der Schaden eingetreten ist** und die Ursache benannt werden kann: Eine Klammer, die neunzig Fahrzeuge umfasst, obwohl die Regel eines betrifft.

Gegenprobe — *bei der großen Klammer bleiben, bleiben Nachteile?* Ja: Mehr Rechenleistung half ein halbes Jahr, die Verlegung des Nachtlaufs beseitigte einen Verursacher von sechs, und die Zeitüberschreitung macht aus Wartezeit gescheiterte Ausgaben.

**Die Grenzen:**

1. **R5 gehört breiter abgefragt.** Eine Aussage aus einer Station trägt keine Entscheidung für 140. Die Frage „was passiert bei Überbuchung" gehört mehreren Stationsleitungen gestellt.

2. **Die Kategorien-Reservierung gehört abgesichert.** Wenn Sonderfahrzeuge künftig einzeln reservierbar sein sollen, ist der Schnitt hinfällig. Das gehört vorher geklärt, nicht nachträglich entdeckt.

3. **Die Gesamtsicht ist nicht Teil des Vorschlags.** Die Stationsleitung braucht eine Übersicht; wie sie entsteht, ist offen. Das ist typisch für kleine Klammern und braucht eine eigene Antwort.

---

## Diskussionsfragen

1. Wie bauen Sie die Stationsübersicht, ohne die Klammern wieder zusammenzuführen?
2. R5 stützt sich auf eine Aussage. Wen würden Sie zusätzlich fragen?
3. Was, wenn ein Kunde ein bestimmtes Fahrzeug reservieren will?
4. Zwischen den Klammern ist die Welt zeitweise widersprüchlich. Wie erklären Sie das der Geschäftsführung?
5. Wann wäre die große Klammer die richtige Wahl gewesen?
