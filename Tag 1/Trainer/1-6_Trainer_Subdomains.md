# 1-6 · Trainer-Ergänzungsmaterial: Subdomains

## Kernidee für den Trainer

Diese Einheit beantwortet die Frage, die im Canvas offen blieb: **Was macht eine Core Domain aus?**

Sie ist zugleich die Einheit mit dem größten unmittelbaren Nutzen für Teilnehmer in Führungs- oder Architekturrollen — denn sie liefert ein Kriterium für Investitionsentscheidungen, das die meisten Häuser nicht haben.

Der Kernsatz:

> **Wichtig und unterscheidend sind zweierlei.**

Die Buchhaltung ist unverzichtbar und unterscheidet niemanden.

## Die Prüffrage — beide Hälften

> **Würde ein Wettbewerber, der dies genauso gut kann wie wir, uns gefährlich — und können es alle?**

| Antwort | Kategorie |
|---|---|
| gefährlich, und er kann es nicht | **Core** |
| gefährlich, aber alle können es | **Supporting** |
| nicht gefährlich | **Generic** |

**Die zweite Hälfte ist entscheidend.** Ohne sie wird auch die Rohstoffbestellung zur Core Domain — wer schlecht bestellt, hat keine Ware. Erst „können es alle?" trennt.

Diesen Punkt ausdrücklich vorführen, sonst ordnet die Gruppe zu viel als Core ein.

## Was kein Kriterium ist

Diese Liste an die Tafel. Jeder Punkt kommt in der Übung als Begründungsversuch vor:

| Scheinkriterium | Warum es nicht trägt |
|---|---|
| Umsatzanteil | die Buchhaltung verarbeitet 100 Prozent des Umsatzes |
| Datenmenge | sagt nichts über Bedeutung |
| Bisheriger Aufwand | zirkulär — man begründet die Vergangenheit mit sich selbst |
| Nutzerzahl | die Zeiterfassung nutzen alle |
| Kompliziertheit | Kompliziertheit ist kein Wert |
| Gefühlte Wichtigkeit | jede Abteilung hält ihres für zentral |

**Trainerfrage:**

> „Die Kautionsabwicklung ist wirklich kompliziert. Macht sie das zur Core Domain?"

Nein. Kompliziertheit ist kein Wert.

## Der Sonderfall als Falle — der praktisch wertvollste Punkt

Im Fallbeispiel: Die Kautionsabwicklung ist branchenuntypisch. Deshalb wurde eine **ganze Buchhaltung** selbst gebaut — drei Jahre, vier bis sechs Entwickler.

**Die Auflösung:**

| Teil | Kategorie | Vorgehen |
|---|---|---|
| Kautionsabwicklung (was geschieht mit einer Kaution) | Supporting | selbst, klein, eigenständig |
| Buchhaltung (Konten, Steuer, Mahnwesen) | Generic | Standardprodukt |

Die Kautionsabwicklung entscheidet fachlich und erzeugt Buchungssätze. Die Buchhaltung bucht, was sie bekommt — das kann jedes Standardprodukt.

**Der Merksatz:**

> Wenn ein Sonderfall einen ganzen Generic-Bereich in die Eigenentwicklung zieht, ist die Grenze falsch gezogen.

Dieser Punkt kommt im Kleinbeispiel (Bäckerei, Restmengenerfassung an der Kasse) noch einmal — dieselbe Struktur, andere Größe. Wer beides zeigt, macht das Muster sichtbar.

## Wissen in Köpfen

Der Befund aus dem Fallbeispiel: Die Erfüllungsquote von 0,8 Prozent entsteht durch vier Disponenten, die täglich nachsteuern. Zwei gehen binnen fünf Jahren.

**Die Zuspitzung für die Gruppe:**

> „Das Verkaufsargument des Unternehmens hängt an vier Personen. Ist das eine Core Domain?"

Ja — und ein ungesichertes Vermögen. Was den Unterschied ausmacht, gehört in Software.

**Die praktische Folge:** Bevor das System ersetzt wird, muss das Wissen erhoben werden. Wer erst baut und dann fragt, baut das alte System nach.

## Subdomain gegen Bounded Context

Die häufigste Verwechslung im ganzen Kurs. Ausdrücklich behandeln:

| | Subdomain | Bounded Context |
|---|---|---|
| Raum | **Problemraum** | **Lösungsraum** |
| Beschreibt | was das Unternehmen tut | wie die Software geschnitten ist |
| Bestimmt durch | das Geschäft | den Entwurf |
| Ändert sich | mit dem Geschäftsmodell | mit dem Entwurf |

**Sie fallen nicht notwendig zusammen.** Eine Core Domain kann über mehrere Kontexte verteilt sein; ein Kontext kann Teile mehrerer Subdomains bedienen.

**Trainerfrage:**

> „Kann eine Core Domain in drei Bounded Contexts liegen?"

Ja. Deckungsgleichheit ist wünschenswert und ein Zeichen dafür, dass der Entwurf der Fachlichkeit folgt — erzwingen lässt sie sich nicht.

## Falsche Einordnung ist kein Korrekturauftrag

Wichtig für die Glaubwürdigkeit: Der Vorschlag in der Lösung korrigiert **nicht alles**.

- Zeiterfassung und Dokumentenarchiv bleiben, obwohl falsch eingeordnet — sie sind gebaut und bezahlt.
- Die Buchhaltung bleibt vorerst — sie funktioniert und bindet nur zwei Entwickler.

**Der Unterschied:** Ein Befund ist eine Lehre für künftige Entscheidungen. Handlungsbedarf entsteht bei laufenden Kosten, bei Risiko oder bei einer ohnehin anstehenden Änderung.

Wer das nicht sagt, hinterlässt Teilnehmer, die im eigenen Haus einen Umbau fordern, der sich nicht rechnet.

## Die Übung

Zehn Bereiche einordnen. Erfahrungsgemäß:

- Die Verfügbarkeitsdisposition wird sofort als Core erkannt — die Aussage der Vertriebsleitung ist eindeutig.
- Die Kautionsabwicklung wird oft als Core eingestuft, weil sie besonders ist. Hier eingreifen: besonders ist nicht unterscheidend.
- Aufgabe 5 (Widerspruch Kaution/Buchhaltung) ist der Kern. Zeit dafür lassen.
- Aufgabe 8 (die neue App) ist der Transfer: Wie entscheidet man **vor** dem Bauen?

## Typische Fragen

**„Was, wenn wir keine Core Domain haben?"**
Dann ist das Unternehmen austauschbar — oder die Analyse ist unvollständig. Beides ist ein Befund, den man ernst nehmen sollte.

**„Kann sich die Einordnung ändern?"**
Ja, mit dem Geschäftsmodell. Nicht mit dem Entwurf. Anlass zur Überprüfung ist eine Veränderung im Wettbewerb, nicht ein Kalendertermin.

**„Wir haben ein Standardprodukt stark angepasst — was nun?"**
Der schlechteste Zustand: Lizenzkosten und Entwicklungsaufwand. Prüfen, ob der eigene Prozess anpassbar wäre.

## Zeitgerüst

| Teil | Minuten |
|---|---|
| Die drei Kategorien, Prüffrage | 10 |
| Fallbeispiel lesen lassen | 10 |
| Was kein Kriterium ist | 5 |
| Übung: zehn Bereiche | 15 |
| Auswertung, Sonderfall-Falle | 12 |

## Übergang

> „Wir haben Kontexte, Sprachen und Einordnungen. Was fehlt, ist die Frage, wie diese Kontexte miteinander umgehen — und was passiert, wenn sich bei einem etwas ändert."
