# Abschlusstest · Domain-Driven Design

**40 Fragen · Bearbeitungszeit 45 Minuten**

Je Frage ist genau **eine** Antwort richtig. Kreuzen Sie an.

**Zur Selbstkontrolle:** Die Lösungen liegen im zugehörigen Dokument. Jede Erläuterung nennt die Einheit, in der das Thema behandelt wurde — so können Sie gezielt nachlesen, statt alles zu wiederholen.

| Punkte | Bewertung |
|---|---|
| 36–40 | sehr sicher |
| 30–35 | sicher |
| 24–29 | Grundlagen sitzen |
| unter 24 | Wiederholung empfohlen |

Der Test enthält drei Arten von Fragen:

- **Begriff** — was bedeutet etwas
- **Anwendung** — welches Konzept passt zur Situation
- **Entscheidung** — was wäre zu tun

---

## Teil A · Grundlagen und Modell

**1.** Was beschreibt der Problemraum?


- a) Wie die Software geschnitten wird
- b) Welche Fehler im Betrieb auftreten
- c) Was das Unternehmen fachlich tut
- d) Welche Technik eingesetzt wird


**2.** Ein Kollege sagt: „Wir machen DDD, deshalb bauen wir Microservices." Was ist daran falsch?


- a) DDD schreibt einen Monolithen vor
- b) Microservices sind mit DDD unvereinbar
- c) DDD trifft keine Aussage über Verteilung
- d) Bounded Contexts sind immer größer als Services


**3.** Was macht ein Modell aus?


- a) Es bildet die Wirklichkeit vollständig ab
- b) Es entspricht dem normalisierten Datenbankschema
- c) Es enthält alle Angaben, die gespeichert werden
- d) Es ist eine Auswahl für einen bestimmten Zweck


**4.** Ein Berater erhebt für ein neues System, welche Formulare und Listen ein Fachbereich führt. Was ist der Einwand?


- a) Formulare sind veraltet
- b) Listen gehören nicht zur Domäne
- c) Er erhebt Daten statt Entscheidungen
- d) Der Fachbereich kennt seine Formulare nicht


**5.** Welche Frage führt am ehesten zu einem brauchbaren Modell?


- a) Welche Entscheidungen treffen Sie?
- b) Welche Daten haben Sie?
- c) Welche Felder brauchen Sie?
- d) Welche Berichte erstellen Sie?


**6.** Ein Modell enthält 61 Merkmale, im Mittel 19 davon gefüllt. Was ist der wahrscheinlichste Grund?


- a) Die Daten sind unvollständig erfasst
- b) Das Modell bedient mehrere Zwecke zugleich
- c) Die Datenbank ist zu groß
- d) Es fehlt eine Eingabeprüfung


---

## Teil B · Sprache und Grenzen

**7.** Wo gilt eine Ubiquitous Language?


- a) Im gesamten Unternehmen
- b) Innerhalb eines Bounded Context
- c) In der Entwicklungsabteilung
- d) In allen Systemen eines Herstellers


**8.** Zwei Bereiche verwenden dasselbe Wort für Verschiedenes. Warum ist das gefährlicher als zwei Wörter für dieselbe Sache?


- a) Es kostet mehr Speicherplatz
- b) Es verletzt die Normalisierung
- c) Es fällt niemandem auf
- d) Es lässt sich nicht dokumentieren


**9.** Bereich A führt einen Kunden mit 5 Angaben, Bereich B denselben mit 20. Was folgt daraus?


- a) Dieselbe Sache, zwei Sichten
- b) Eine Kontextgrenze ist nötig
- c) Bereich A arbeitet unvollständig
- d) Die Begriffe müssen vereinheitlicht werden


**10.** Derselbe Konzernkunde wird im Vertrieb als 1 gezählt, an der Station als 340. Was folgt daraus?


- a) Dieselbe Sache, zwei Sichten
- b) Ein Zählfehler in einem der Bereiche
- c) Ein Widerspruch — Kontextgrenze
- d) Eine fehlende Aggregation


**11.** Ein Einigungsworkshop soll eine gemeinsame Definition von „Kunde" festlegen. Warum scheitert das meist?


- a) Die Teilnehmer sind unvorbereitet
- b) Die Bedeutungen folgen aus der Arbeit
- c) Es fehlt eine Moderation
- d) Der Begriff ist zu allgemein


**12.** Ein Glossar enthält den Eintrag: „Kunde: Je nach Kontext Vertragspartner, Nutzer oder Empfänger." Was ist das Problem?


- a) Der Eintrag ist zu kurz
- b) Er ist nicht alphabetisch eingeordnet
- c) Es fehlt ein Beispiel
- d) Er dokumentiert die Mehrdeutigkeit


**13.** Welcher Bestandteil eines Glossareintrags verhindert erfahrungsgemäß die meisten Fehler?


- a) Die Abgrenzung zu Verwandtem
- b) Die formale Definition
- c) Das Anlagedatum
- d) Der Verweis auf die Quelle


**14.** Ein Glossar wurde in acht Monaten elfmal aufgerufen. Was ist die wahrscheinlichste Ursache?


- a) Die Einträge sind falsch
- b) Es ist zu kurz
- c) Die Mitarbeiter sind nicht geschult
- d) Es liegt nicht am Ort der Arbeit


**15.** Ein Kontext soll beschrieben werden. Welcher Zwecksatz trägt?


- a) Alles, was am Tresen passiert
- b) Vorgänge verwalten und Fahrzeuge disponieren
- c) Alles rund um die Vermietung
- d) Verantwortet den Mietvorgang bis zum Abschluss


**16.** Mit welcher Frage prüfen Sie, ob eine Aufgabe in einen Kontext gehört?


- a) Ändert sie sich mit dem Übrigen?
- b) An welchem Ort findet sie statt?
- c) Wer braucht ihr Ergebnis?
- d) Wer hat sie ursprünglich gebaut?


**17.** Welches Feld eines Bounded Context Canvas verhindert, dass der Kontext wächst?


- a) Der Zweck
- b) Die Ubiquitous Language
- c) Die eingehenden Nachrichten
- d) Die Abgrenzung


---

## Teil C · Subdomains und Beziehungen

**18.** Womit unterscheidet sich eine Core Domain von einer Supporting Subdomain?


- a) Wettbewerber können sie nicht
- b) Sie verarbeitet mehr Daten als andere
- c) Sie hat deutlich mehr Nutzer
- d) Sie ist technisch komplizierter


**19.** Ein Unternehmen hat die Buchhaltung selbst gebaut und die Verfügbarkeitsdisposition zugekauft. Die Disposition ist das Verkaufsargument. Was ist der Befund?


- a) Die Buchhaltung ist zu teuer
- b) Der Zukauf war zu früh
- c) Der Aufwand liegt am falschen Ort
- d) Beides ist Supporting


**20.** Welches ist **kein** Kriterium für die Einordnung als Core Domain?


- a) Es verarbeitet den gesamten Umsatz
- b) Der Wettbewerb kann es nicht
- c) Es steht im Verkaufsgespräch
- d) Ein gleichwertiger Wettbewerber wäre gefährlich


**21.** Eine besondere Kautionsregelung hat dazu geführt, dass eine ganze Buchhaltung selbst gebaut wurde. Was war der Fehler?


- a) Die Kautionsregelung ist zu kompliziert
- b) Die Buchhaltung ist Core Domain
- c) Es fehlte ein Standardprodukt
- d) Der Sonderfall wurde nicht abgetrennt


**22.** Wie sollte mit einer Generic Subdomain umgegangen werden?


- a) Standard nehmen und nicht anpassen
- b) Standard nehmen und anpassen
- c) Selbst bauen, aber sparsam
- d) Zukaufen und erweitern


**23.** Eine Context Map zeigt vor allem …


- a) welche Daten fließen
- b) wer nachziehen muss
- c) welche Systeme existieren
- d) welche Technik verwendet wird


**24.** „Auf deren Format haben wir keinen Einfluss, und wir übernehmen es unverändert." Welches Muster?


- a) Customer / Supplier
- b) Shared Kernel
- c) Anticorruption Layer
- d) Conformist


**25.** Zwei Kontexte teilen sich einen Modellausschnitt. Was ist der Preis?


- a) Höherer Speicherbedarf
- b) Gekoppelte Releases und Abstimmung
- c) Doppelte Datenhaltung
- d) Verlust der Ubiquitous Language


**26.** Ein Fremdformat wird an 31 Stellen in drei Kontexten ausgewertet. Was fehlt?


- a) Eine Dokumentation
- b) Eine Versionsverwaltung
- c) Eine Übersetzung an der Grenze
- d) Ein Standardformat


---

## Teil D · Bausteine

**27.** Ein Fahrzeug bekommt ein neues Kennzeichen und einen neuen Halter. Es bleibt dasselbe Fahrzeug. Wie ist es einzuordnen?


- a) Value Object
- b) Entity
- c) Aggregate
- d) Domain Event


**28.** Welche Frage entscheidet zwischen Entity und Value Object?


- a) Muss es dasselbe sein?
- b) Wird es gespeichert?
- c) Ist es wichtig?
- d) Wie groß ist es?


**29.** Eine Anschrift hat eine Kennung, ein Änderungsdatum und einen Gültigkeitszeitraum bekommen. Was ist die wahrscheinlichere Erklärung?


- a) Anschriften sind Entities
- b) Der Gültigkeitszeitraum ist falsch
- c) Es fehlt eine Historientabelle
- d) Die Zuordnung trägt die Geschichte


**30.** Was rechtfertigt eine Aggregatgrenze?


- a) Die Dinge gehören sachlich zusammen
- b) Eine Regel muss sofort gelten
- c) Sie werden gemeinsam angezeigt
- d) Sie liegen in derselben Tabelle


**31.** Ein Aggregate umfasst alle Fahrzeuge und Vorgänge einer Station. Was ist die Folge?


- a) Bessere Konsistenz bei allen Vorgängen
- b) Geringerer Speicherbedarf
- c) Vorgänge behindern sich gegenseitig
- d) Einfachere Auswertungen


**32.** Welche Frage klärt, ob zwei Dinge in dieselbe Klammer gehören?


- a) Was passiert bei kurzer Abweichung?
- b) Werden sie gemeinsam angezeigt?
- c) Wer hat sie ursprünglich angelegt?
- d) Wie oft ändern sie sich im Jahr?


**33.** Ein Vorgang ändert in einem Schritt drei Aggregate. Was folgt daraus?


- a) Die Aggregate sind zu klein geschnitten
- b) Falsch geschnitten oder Ereignis fehlt
- c) Die Reihenfolge der Schritte stimmt nicht
- d) Es fehlt eine gemeinsame Transaktion


**34.** Welche Formulierung ist ein Domain Event?


- a) Rechnung erstellen
- b) Datensatz gespeichert
- c) Vorgang wurde abgeschlossen
- d) Kaution freigeben


**35.** Warum soll der Sender eines Ereignisses seine Empfänger nicht kennen?


- a) Weil er sonst ständig geändert wird
- b) Aus Gründen des Datenschutzes
- c) Weil Empfänger sich nicht anmelden können
- d) Weil die Reihenfolge sonst festliegt


**36.** Eine Rechnung darf einen Tag später kommen, aber nicht ausbleiben. Wie ist der Empfänger einzuordnen?


- a) Nachrangig
- b) Zeitnah
- c) Zwingend
- d) Sofort


---

## Teil E · Umsetzung und Ablösung

**37.** Was gehört **nicht** in einen Application Service?


- a) Ein Aggregate holen
- b) Eine fachliche Regel prüfen
- c) Ein Ereignis melden
- d) Ein Aggregate speichern


**38.** Eine Regel lässt sich nur prüfen, wenn Datenbank und zwei Fremdsysteme laufen. Was folgt daraus?


- a) Es fehlen Attrappen
- b) Die Regel ist zu kompliziert
- c) Die Testumgebung ist unvollständig
- d) Die Regel steckt in technischem Ablauf


**39.** Welche Aussage ist ein Umschaltkriterium?


- a) Sobald Stufe 3 fertig ist
- b) Bis zum Jahresende
- c) Wenn alle zufrieden sind
- d) Nach 30 Tagen ohne Rückfall


**40.** Ein Anticorruption Layer arbeitet …


- a) nur vom Alt- zum Neusystem
- b) in beide Richtungen
- c) nur vom Neu- zum Altsystem
- d) nur bei Fremdsystemen


---

*Ende des Tests. Die Lösungen finden Sie im zugehörigen Dokument.*
