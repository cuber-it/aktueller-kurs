# 1-7 · Trainer-Ergänzungsmaterial: Context Mapping

## Kernidee für den Trainer

Die letzte Einheit des Tages und die, die alles zusammenführt: Kontexte stehen, Sprachen sind festgehalten, Einordnungen getroffen — jetzt geht es um ihr Verhältnis zueinander.

Der Kernsatz, der jede Beziehung bestimmt:

> **Wer muss nachziehen, wenn sich beim anderen etwas ändert — und wie viel Einfluss hat er darauf?**

Alles Weitere ist eine Ableitung daraus. Wer die Muster als Vokabelliste lehrt, verliert die Gruppe; wer sie aus dieser einen Frage herleitet, braucht sie nicht auswendig zu lernen.

## Was eine Context Map nicht ist

Früh abgrenzen, sonst zeichnet die Gruppe eine Systemlandschaft:

| Verwechslung | Unterschied |
|---|---|
| Systemlandschaft | zeigt Systeme und Technik, nicht Modellbeziehungen |
| Schnittstellenliste | zeigt **dass** etwas fließt, nicht **wie** die Abhängigkeit beschaffen ist |
| Architekturdiagramm | zeigt Bausteine, nicht wer bei Änderungen nachzieht |
| Datenflussdiagramm | die Abhängigkeitsrichtung kann der Datenrichtung **entgegengesetzt** sein |

**Der letzte Punkt verdient eine eigene Minute.** Bei einem Open Host Service liefert der Lieferant Daten und bestimmt trotzdem das Format. Datenrichtung und Abhängigkeitsrichtung sind zweierlei.

## Die Muster aus der Prüffrage herleiten

Nicht als Liste vortragen. Stattdessen die zwei Fragen stellen und die Muster daraus entstehen lassen:

**Frage 1: Ist die Abhängigkeit gegenseitig?**

- Ja, beide ändern dasselbe → **Shared Kernel** oder **Partnership**
- Nein, einer liefert → weiter

**Frage 2: Wie viel Einfluss hat der Abnehmer?**

- Einfluss durch Absprache → **Customer / Supplier**
- Kein Einfluss, Format wird übernommen → **Conformist**
- Kein Einfluss, aber an der Grenze übersetzt → **Anticorruption Layer**

**Open Host Service** und **Published Language** sind die Sicht des Lieferanten: Er bedient viele Abnehmer über eine veröffentlichte Schnittstelle statt jeden einzeln.

**Separate Ways** ist eine Entscheidung, keine Lücke — gehört in die Map.

## Conformist ist keine Schande

Wichtiger Punkt, weil Teilnehmer sonst überall einen Anticorruption Layer bauen wollen.

Bei einem stabilen Standardformat von geringer Bedeutung ist eine Übersetzung Aufwand ohne Gegenwert.

**Der Fehler im Fallbeispiel war nicht Conformist.** Der Fehler war:

1. Conformist ist **entstanden** statt entschieden worden — aus Zeitdruck.
2. Das Fremdformat wandert **über die Anbindung hinaus** in vier Kontexte.

**Der Merksatz:**

> Conformist und Anticorruption Layer schließen einander nicht aus. Man fügt sich dem Format **und** übersetzt es an der Grenze.

## Der Befund mit den 31 Stellen

Das eindrücklichste Material der Einheit:

| Kontext | Stellen | Fachlich begründet |
|---|---|---|
| Anmietung | 12 | ja |
| Fakturierung | 9 | ja |
| Flotte | 6 | teilweise |
| Werkstatt | 4 | **niemand konnte erklären, warum** |

**Trainerfrage:**

> „Was hätte die vier Stellen in der Werkstatt verhindert?"

Antwort: eine Grenze. Mit einem Anticorruption Layer wäre eine Stelle betroffen gewesen statt 31 — und die Formatumstellung hätte drei Wochen gedauert statt elf.

## Shared Kernel — das teuerste Muster

Ausdrücklich als teuer kennzeichnen:

| Preis | |
|---|---|
| Koordination | jede Änderung am geteilten Teil muss abgestimmt werden |
| Releases | gekoppelt |
| Zuständigkeit | der geteilte Teil gehört keinem allein |
| Tempo | der langsamere Kontext bestimmt es für beide |

**Es entsteht leicht und ist schwer wieder loszuwerden.**

Die Prüffrage: Brauchen beide wirklich dasselbe **Modell**, oder nur dieselben **Objekte** in verschiedener Sicht?

Im Übungsmaterial ist die Antwort strittig — Anmietung und Flotte teilen Fahrzeugdaten, brauchen aber Verschiedenes davon. Das ist gewollt: Die Gruppe soll die Abwägung führen, nicht eine Antwort abschreiben.

## Die zwei Fragen an die Werkstatt

Aufgabe 6 der Übung ist eine Gesprächsführungsaufgabe und in der Praxis wertvoll:

**Was funktioniert:**
- „Welche **Entscheidung** treffen Sie anhand dieses Wertes?" — sucht die fachliche Information hinter dem technischen Feld
- „Was würden Sie tun, wenn es das Feld nicht gäbe?" — prüft, ob die Auswertung überhaupt gebraucht wird

**Was nicht funktioniert:**
- „Warum werten Sie den Partnerstatus aus?" — die Antwort lautet „weil er da ist"

Diesen Unterschied vorführen. Er ist übertragbar auf jede Anforderungserhebung.

## Die Übung

Acht Kontexte, sieben Beziehungen. Erfahrungsgemäß:

- Die Muster werden schnell zugeordnet, wenn die Herleitung über die zwei Fragen sitzt.
- Die Einstufung von Anmietung → Fakturierung spaltet: Customer/Supplier (Absprache wäre möglich) oder Conformist (findet nicht statt)? Beides vertretbar — die Diskussion ist der Wert.
- Aufgabe 7 (Zahlungsdienstleister) ist der Transfer: Die Map zeigt die Beziehung, aber nicht, ob eine Grenze existiert. Genau diese Frage wurde beim Partnernetzwerk nicht gestellt.

**Wenn Zeit bleibt:** Aufgabe 8 — welche zwei Beziehungen zuerst ändern? Das führt zu Risiko- und Nutzenabwägung statt Aufwandsbetrachtung.

## Aktualität

Der Punkt, an dem die meisten Maps sterben.

> **Durch Anlass, nicht durch Turnus.**

Eine Map, die jährlich überarbeitet wird, ist meist veraltet. Eine, die bei jeder neuen Anbindung ergänzt wird — **bevor** entwickelt wird —, bleibt brauchbar.

## Typische Fragen

**„Wie detailliert soll die Map sein?"**
Eine Seite. Was nicht darauf passt, wird vor einer Änderung nicht gelesen.

**„Zeigt sie auch, wie eng die Kopplung ist?"**
Nein, und das ist eine echte Schwäche. Zwischen zwei Kontexten fließen wenige Felder, zwischen zwei anderen ein ganzes Modell — beide sind eine Linie. Wer das ergänzt, überfrachtet die Map. Ein offener Punkt.

**„Wer besitzt die Map?"**
Ungelöst in den meisten Häusern. Ohne Eigentümer verfällt sie.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Was eine Map ist und was nicht | 8 |
| Fallbeispiel lesen lassen | 10 |
| Muster aus den zwei Fragen herleiten | 12 |
| Übung: Map zeichnen | 15 |
| Auswertung, Conformist ohne Grenze | 10 |

## Tagesabschluss

Die letzte Einheit von Tag 1. Ein Rückblick lohnt:

> „Wir haben heute keinen Code geschrieben. Trotzdem haben wir Entscheidungen getroffen, die bestimmen, wie der Code morgen aussieht — wo Grenzen verlaufen, welche Sprache gilt, wo Aufwand hingehört. Morgen bauen wir das Modell **innerhalb** eines Kontextes."

**Die Rückmeldefrage für den Tag** — beantwortbar, ohne jemanden zu kritisieren:

> „Welchen Begriff aus Ihrem eigenen System würden Sie morgen als Erstes überprüfen?"
