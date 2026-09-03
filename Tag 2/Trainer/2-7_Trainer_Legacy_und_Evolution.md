# 2-7 · Trainer-Ergänzungsmaterial: Legacy und Evolution

## Kernidee für den Trainer

Die Einheit, auf die die Teilnehmer den ganzen Kurs gewartet haben — weil fast niemand auf der grünen Wiese baut.

Der Kern:

> **Grenze ziehen, dahinter neu bauen, schrittweise umleiten.**

Und die Verbindung zu Tag 1, die ausgesprochen gehört:

> **Kontextgrenzen sind die Schnittlinien für die Ablösung.** Wer sie kennt, weiß, wo er trennen kann.

Damit schließt sich der Bogen: Das strategische Design von gestern ist die Voraussetzung für die Ablösung von heute.

## Einstieg

**Die Handzeichenfrage:**

> „Wer von Ihnen arbeitet an einem System, das älter ist als fünf Jahre?"

Meist alle Hände.

> „Wer könnte es an einem Wochenende durch ein neues ersetzen?"

Keine.

**Der Anschluss:** Deshalb ist die Frage nicht, wie man es richtig baut, sondern wie man dorthin kommt, ohne den Betrieb anzuhalten.

## Anticorruption Layer — in beide Richtungen

Der Punkt, der regelmäßig fehlt.

Ein ACL wird meist als Schutz **vor** dem Altsystem erklärt. Solange beide laufen, muss aber auch das Neue dem Alten liefern — in dessen Begriffen.

| Richtung | Übersetzt |
|---|---|
| Alt → Neu | alte Begriffe in das neue Modell |
| Neu → Alt | neue Begriffe zurück in die alte Form |

**Trainerfrage:**

> „Wie lange laufen beide Systeme parallel?"

Antwort in der Praxis: länger als geplant. Deshalb ist die Rückrichtung keine Randnotiz.

## Strangler Fig

Das Bild kurz erklären: Die Würgefeige wächst um einen Baum herum, bis der Baum abstirbt und die Feige steht.

**Für die Software:** Neues wächst um das Alte, Aufrufe werden nach und nach umgeleitet, bis das Alte nichts mehr trägt.

**Der praktische Kern ist die Umleitung.** Sie braucht eine Stelle, an der entschieden wird, wer bedient — alt oder neu. Diese Stelle ist der eigentliche Bauteil.

## Wo anfangen

Der Teil mit dem meisten Widerspruch aus der Gruppe.

**Nicht beim Einfachsten**, obwohl das verlockend ist. Sondern:

| Kriterium | Warum |
|---|---|
| Wo der Schmerz ist | sonst fehlt der Rückhalt für ein mehrjähriges Vorhaben |
| Wo die Grenze klar verläuft | eine unklare Grenze macht die Übersetzung beliebig |
| **Core Domain zuerst** | dort lohnt der Aufwand; Generic Subdomains kauft man |

**Der Rückgriff auf Tag 1:** Wer die Subdomains eingeordnet hat, weiß, wo anzufangen ist. Wer es nicht getan hat, fängt beim Einfachsten an und löst das falsche Problem zuerst.

**Trainerfrage:**

> „Was wäre in Ihrem System das Erste — und warum?"

## Der Umschaltpunkt

Der Punkt, der in der Praxis am häufigsten fehlt und die teuersten Folgen hat.

> **Vorab festlegen, woran erkennbar ist, dass das Neue trägt.**

Ohne Kriterium läuft beides dauerhaft weiter. Es gibt Systeme, die seit zehn Jahren „in Ablösung" sind.

**Trainerfrage:**

> „Kennen Sie ein System, das seit Jahren abgelöst wird?"

Erfahrungsgemäß mehrere Meldungen. Das ist der überzeugendste Beleg.

## Die zwei Fehler

**Anbau ohne Grenze.** Das Neue wird an das Alte angebaut, ohne Übersetzung. Dann wandern die alten Begriffe mit, und nach zwei Jahren ist das Neue wie das Alte — nur neuer.

**Alles auf einmal.** Das Vorhaben wird zu groß, dauert zu lange, verliert Rückhalt und wird abgebrochen. Danach ist die Lage schlechter als vorher, weil zwei halbfertige Systeme laufen.

## Der Kursabschluss

Die letzten fünfzehn Minuten. Nicht zusammenfassen, was gesagt wurde — die sechs Merksätze aus dem Inhaltsdokument stehen dort und können vorgelesen werden.

**Wertvoller ist der Transfer.** Drei Fragen, jede einzeln beantworten lassen:

> „Was würden Sie nächste Woche als Erstes tun?"

> „Wo sind Sie unsicher geblieben?"

> „Was hätten Sie weggelassen?"

Die zweite und dritte Frage sind beantwortbar, ohne jemanden zu kritisieren — deshalb kommen sie ehrlicher zurück als eine Zufriedenheitsfrage.

**Die Antworten notieren.** Sie sind die beste Grundlage für die nächste Durchführung.

## Was man am Ende nicht tun sollte

- **Nicht überziehen.** Nach zwei Tagen ist die Aufnahmefähigkeit erschöpft.
- **Keine neuen Themen.** CQRS, Event Sourcing, Microservices — wenn sie kommen, kurz einordnen und auf Literatur verweisen.
- **Keine Zusammenfassung aller Bausteine.** Das wirkt wie Prüfungsvorbereitung.

## Zum Umgang mit gemischten Gruppen

**Die stärkste Einheit für Management.** Hier geht es um Vorgehen, Risiko und Reihenfolge — nicht um Technik.

Wenn Führungskräfte dabei sind, den Umschaltpunkt und das Anfangskriterium betonen. Das sind Entscheidungen, die sie treffen müssen.

## Typische Fragen

**„Wie lange dauert so eine Ablösung?"**
Länger als geplant. Realistisch sind bei einem gewachsenen System mehrere Jahre für die Core Domain.

**„Was, wenn das Alte während des Umbaus weiter geändert wird?"**
Das wird es. Deshalb muss der ACL beide Richtungen können, und deshalb ist ein Big-Bang-Neubau selten beherrschbar.

**„Lohnt sich das überhaupt?"**
Nicht überall. Bei einer Generic Subdomain kauft man ein Produkt. Die Frage gehört vor jeder Ablösung gestellt — und die Antwort steht in der Subdomain-Einordnung von gestern.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Handzeichenfrage, Einordnung | 6 |
| Anticorruption Layer, beide Richtungen | 8 |
| Strangler Fig, wo anfangen | 10 |
| Umschaltpunkt, die zwei Fehler | 8 |
| **Kursabschluss und Transferfragen** | **15** |

## Zum Schluss

Der letzte Satz des Kurses sollte nicht „Vielen Dank für Ihre Aufmerksamkeit" sein.

Ein Vorschlag:

> „DDD ist kein Werkzeugkasten, den man abarbeitet. Es ist eine Art, Fragen zu stellen. Wenn Sie nächste Woche in einer Besprechung fragen, was ein Begriff eigentlich bedeutet — dann hat der Kurs funktioniert."
