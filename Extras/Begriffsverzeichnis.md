# Begriffsverzeichnis

Die Fachbegriffe des Kurses, mit Verweis auf die Einheit, in der sie eingeführt werden.

Gegliedert nach Zusammenhang, nicht alphabetisch.

---

## Grundbegriffe

**Domäne** · 1-1
Der fachliche Bereich, in dem gearbeitet wird. Existiert unabhängig von jeder Software.

**Modell** · 1-2
Eine zweckgebundene Vereinfachung der Domäne. Enthält, was für die Aufgabe nötig ist, und lässt den Rest weg.
*Nicht zu verwechseln mit dem Datenmodell — das beschreibt Speicherung.*

**Problemraum** · 1-1
Was das Unternehmen tut. Wird durch das Geschäft bestimmt. Einheit: die Subdomain.

**Lösungsraum** · 1-1
Wie die Software geschnitten ist. Wird durch den Entwurf bestimmt. Einheit: der Bounded Context.

**Strategisches Design** · 1-1
Grenzen, Sprache und Beziehungen im Großen. Gegenstand von Tag 1.

**Taktisches Design** · 2-1
Der Bau des Modells innerhalb einer Kontextgrenze. Gegenstand von Tag 2.

---

## Sprache

**Ubiquitous Language** · 1-3
Die gemeinsame Sprache von Fachbereich und Entwicklung — verbindlich in Gesprächen, Dokumenten und im Code. Gilt **innerhalb eines Bounded Context**.

**Glossar** · 1-4
Die Aufzeichnung der Ubiquitous Language. Nur je Kontext möglich; über Grenzen hinweg entstehen Oberdefinitionen.

---

## Grenzen

**Bounded Context** · 1-5
Ein Bereich, in dem ein Modell und eine Sprache gelten. Innerhalb ist jeder Begriff eindeutig; außerhalb gilt er nicht.

**Bounded Context Canvas** · 1-5
Arbeitsblatt zur Beschreibung eines Kontextes: Zweck, Einordnung, fachliche Entscheidungen, Sprache, Nachrichten, Abgrenzung.

**Subdomain** · 1-6
Ein fachlicher Teilbereich der Domäne. Liegt im **Problemraum**.

**Core Domain** · 1-6
Die Subdomain, mit der sich das Unternehmen unterscheidet. Selbst bauen, mit den besten Leuten.

**Supporting Subdomain** · 1-6
Notwendig, aber branchenüblich. Sparsam bauen oder zukaufen.

**Generic Subdomain** · 1-6
Überall gleich, Standardprodukte vorhanden. Standard nehmen und nicht anpassen.

---

## Beziehungen zwischen Kontexten

**Context Map** · 1-7
Übersicht der Kontexte und ihrer Beziehungen. Zeigt, wer nachziehen muss, wenn sich beim anderen etwas ändert.

**Customer / Supplier** · 1-7
Der Abnehmer kann Anforderungen stellen, es gibt Absprache und Vorlauf.

**Conformist** · 1-7
Der Abnehmer übernimmt das fremde Modell unverändert, weil er keinen Einfluss hat. Eine Wahl, kein Versäumnis.

**Anticorruption Layer** · 1-7, 2-7
Übersetzung an der Grenze. Verhindert, dass fremde Begriffe in eigene Kontexte durchsickern. Arbeitet in **beide** Richtungen.

**Open Host Service** · 1-7
Der Lieferant bietet eine veröffentlichte Schnittstelle für viele Abnehmer.

**Published Language** · 1-7
Ein gemeinsames Austauschformat, auf das sich mehrere geeinigt haben.

**Shared Kernel** · 1-7
Zwei Kontexte teilen sich einen Modellausschnitt. Jede Änderung muss abgestimmt werden, Releases sind gekoppelt. Das teuerste Muster.

**Partnership** · 1-7
Zwei Teams stehen und fallen gemeinsam. Koordinierte Planung und Auslieferung.

**Separate Ways** · 1-7
Keine Verbindung. Eine Entscheidung, keine Lücke.

---

## Bausteine des Modells

**Entity** · 2-2
Etwas, das dieselbe Sache bleibt, auch wenn sich alle Merkmale ändern.

**Value Object** · 2-2
Etwas, das vollständig durch seine Werte bestimmt ist. Zwei mit gleichen Werten sind austauschbar. Wird ersetzt, nicht geändert.

**Aggregate** · 2-3
Eine Klammer um Dinge, die gemeinsam gültig bleiben müssen.

**Invariante** · 2-3
Die Regel, die immer gelten muss. Ohne Invariante kein Aggregate.

**Aggregate Root** · 2-3
Die eine Entity, über die von außen zugegriffen wird.

**Konsistenzgrenze** · 2-3
Innerhalb gilt die Regel sofort. Außerhalb darf sie zeitweise verletzt sein.

**Domain Event** · 2-4
Eine Tatsache aus der Fachwelt, in der Vergangenheit formuliert. Berichtet, fordert nicht.

**Command** · 2-4
Eine Aufforderung an einen bestimmten Empfänger. Kann abgelehnt werden.

---

## Umsetzung

**Repository** · 2-6
Der Zugang zu Aggregaten. Verbirgt, woher sie kommen. Eines je Aggregate, nicht je Entity.

**Factory** · 2-6
Erzeugt ein Aggregate in gültigem Zustand.

**Domain Service** · 2-6
Fachlogik, die zu keinem einzelnen Gegenstand gehört.

**Application Service** · 2-6
Ablaufsteuerung: holen, Methode rufen, speichern, melden. Enthält **keine** Fachlogik.

**Hexagonal · Onion · Clean Architecture** · 2-6
Drei Namen für denselben Gedanken: Das Modell hängt von nichts ab, alles andere hängt von ihm ab.

---

## Methoden

**Event Storming** · 2-5
Werkstattmethode zur gemeinsamen Erhebung einer Domäne. Beginnt mit dem, was geschehen ist.

**Hotspot** · 2-5
Ein markierter Streitpunkt oder eine offene Frage. Das wertvollste Ergebnis eines Durchlaufs.

**Big Picture · Process Level · Design Level** · 2-5
Drei Detailstufen des Event Storming.

---

## Ablösung

**Strangler Fig** · 2-7
Neues wächst um das Alte herum; nach und nach wird umgeleitet, bis das Alte nichts mehr trägt.

**Umschaltkriterium** · 2-7
Eine überprüfbare Bedingung, bei deren Eintritt das Altsystem abgeschaltet wird. Ein Termin ist kein Kriterium.

---

## Begriffe, die oft verwechselt werden

| | |
|---|---|
| **Subdomain / Bounded Context** | Problemraum gegen Lösungsraum |
| **Entity / Value Object** | Identität über die Zeit oder nicht |
| **Aggregate / Entity** | Konsistenzklammer gegen einzelnes Ding |
| **Domain Event / Command** | geschehen gegen gefordert |
| **Repository / Factory** | holen gegen erzeugen |
| **Domain Service / Application Service** | Fachlogik gegen Ablaufsteuerung |
| **Domain Event / Event Sourcing** | melden gegen speichern |
| **Bounded Context / Microservice** | Modellgrenze gegen Betriebseinheit |
